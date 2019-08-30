---
title: JetBrains使用指南
summary: JetBrains使用指南
authors:
    - Zhiyuan Chen
date: 2019-08-30 19:15:03
categories: 
    - Document
    - Docker
    - Dockerfile
tags:
    - Document
    - Docker
    - Dockerfile
    - Containerized
---

# Dockerfile

Dockerfile可以说是Docker最重要的一部分。Docker依据Dockerfile的描述构建出一个又一个Docker镜像，使之得以运行。也是因此，我们可以将软件交付从数十GiB的代码缩减到数百KiB。

本文将简要介绍Dockerfile的内容，并将提供nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04的Dockerfile供大家分析。

## 指令

首先，我们从Dockerfile的指令开始。Dockerfile有十几种指令，只有其中四种指令会创建一个新的层。他们是**FROM**、**COPY**、**ADD**、**RUN**和**CMD**、**ENTRYPOINT**。对于其他所有指令，Docker都将会构建一个中间镜像，这既不会增加容器的大小，也不会对容器的性能产生任何影响。但是这四个指令在运行当中会创建新的层，在实践过程当中我们需要特别关注这些指令，错误的使用这些指令将可能造成容器未按期待运行。

### FROM

    FROM <image>[:<tag>] [AS <name>]
    FROM <image>[@<digest>] [AS <name>]

通常情况下，Dockerfile的第一行是FROM，也即代表其将基于一个另一个Docker（当然，极少数情况下也可能是scratch）构建。你可以将其理解为继承--子类将实现父类的全部功能。如果你希望对你的容器具有完全的掌控的话，你也可以省略掉FROM或者直接FROM scratch来构建一个基镜像。这将很可能耗去你大量的精力却无法带来任何收益，我们强烈推荐你不要这么做，除非你很确定你自己想做些什么。

在上古时代（Docker 17.05之前），Docker是不支持多个FROM语句的。即Docker是单一继承的。但Docker 17.05添加了多阶段构建（multi-stage builds）。如果你在容器当中需要编译什么东西的话，使用多阶段构建创建一个新的容器进行编译并将结果复制到本容器当中将对于降低容器大小非常有利。我们会在稍后的例子当中进行演示。

### LABEL

    LABEL <key>=<value>

LABEL对镜像进行标签，这个似乎没什么需要多说的。

### ARG 和 ENV

    ARG <name>[=<default value>]

    ENV <key> <value>
    ENV <key>=<value>

ARG指令设置参数，参数只能在构建镜像时使用，镜像创建完毕即丢失。ENV指令设置的则是环境变量，在容器创建好后仍然存在。这两个指令都对接下来的ADD、CMD、COPY、ENV、EXPOSE、ENTRYPOINT、FROM、LABEL、RUN、STOPSIGNAL、USER、VOLUME和WORKDIR生效。此外，对于Docker 1.4之后的版本来说，如果ONBUILD与上述十个指令联用，那他们也将对ONBUILD指令生效。对于Docker 1.13之后的版本来说，如果 docker build --build-arg 传递的参数在Dockerfile当中没有使用，Docker将会产生如下警告：

    [Warning] One or more build-args [foo] were not consumed.

这两个指令的区别主要在于作用域。如果需要在构建镜像时创建环境变量，也可这么写：

    ARG ZC="Zhiyuan Chen"
    ENV ${ZC}

Docker有如下的预定义参数，可以直接调用：
    HTTP_PROXY
    http_proxy
    HTTPS_PROXY
    https_proxy
    FTP_PROXY
    ftp_proxy
    NO_PROXY
    no_proxy

此外，ARG是唯一一个允许在第一个 FROM 指令之前出现的指令。

### WORKDIR 和 USER

    WORKDIR /path/to/workdir

    USER <user>[:<group>]
    USER <UID>[:<GID>]

WORKDIR指令设置当前的工作目录。该指令将对接下来的ADD、CMD、COPY、ENTRYPOINT和RUN指令产生影响。

USER指令设置当前的操作用户。该指令将对接下来的RUN、CMD和ENTRYPOINT指令产生影响。

### RUN

    RUN <command>
    RUN ["executable", "param1", "param2"]

RUN指令有两种格式，第一种是shell格式，在Linux系统下默认使用 **/bin/sh -c** ， 在Windows系统下则默认使用 **cmd /S /C** 。第二种则是exec格式。需要注意的是，在exec格式之下，将由shell来处理环境变量而不是Docker，所以在Dockerfile当中定义的环境变量通常无效。一般情况下，我们不会使用第二种格式，除非必须显式指定shell。

RUN应该是使用最多的Dockerfile指令了，无论是下载还是运行，一切都少不了RUN的幕后黑手。这也导致RUN成了最容易出错的地方。

**&&**关键字允许你在一个RUN当中执行多条命令。由于RUN指令执行的过程当中会创建一个新的层，所以我们需要按照需求对指令进行合并或者拆分。

比如说在初始的apt-get当中，如果我们错误的将指令拆分成：

    RUN apt-get update          # layer x
    RUN apt-get install -y git  # layer x + 1

那么在执行完第一个指令之后，x层就会被缓存下来，随后倘若我们对第二行指令进行更改，那他可能就会获取到过时的软件。因此，apt-get一定要写成如下形式：

    RUN apt-get update && apt-get install -y \
        git

### COPY 和 ADD

    COPY [--chown=<user>:<group>] <src>... <dest>
    COPY <src> <dest>

这两个指令的功能非常相似，都是将文件从容器之外复制到容器之内。但COPY指令更简单也更透明一些，也更经常被使用。ADD指令增加了对url的支持使得其可以从网上下载文件，同时它也可以直接将文件解压。但是由于ADD指令从网上下载的文件会自动设置权限为600，而调整权限还需要一个RUN指令。不如直接通过RUN下载文件来的方便。因此，请只在需要解压文件的时候才使用ADD指令。

需要注意的是，<src>为源于Dockfile所在文件夹的相对路径，<dest>则是目标容器内的绝对路径。此外，这两个指令同时支持通配符，即

    COPY zc* /usr/local/docker

将会把当前目录下所有以zc开头的文件复制到容器的/usr/local/docker目录当中。

### EXPOSE

    EXPOSE <port> [<port>/<protocol>...]

EXPOSE指令暴露容器对应的端口。默认情况下，EXPOSE指令将假设TCP协议，如果使用UDP协议需要显式声明。

### VOLUME

    VOLUME ["/zc"]

VOLUME指令和前文所述的使用 docker run -v 但只指定容器内目录完全一样。他会给这个挂载随机一个名字，然后再本机/var/lib/docker/volumes目录之下创建一个与挂载名字相同的文件夹。也就是说，虽然它的名字叫卷，但创建的实际上是一个捆绑挂载……这个指令我从来没有用过，还专门为这篇文章查了半天资料顺带做了两个实验。我完全无法理解这种设计的用意，也强烈建议大家都不要使用。docker run命令多打两句能实现的要比他优雅的多，建议使用。值得一提的是，如果在VOLUME里和在 docker run 里同时挂载了目录，则只有 docker run 挂载的目录会生效。

### HEALTHCHECK 和 STOPSIGNAL

    HEALTHCHECK [OPTIONS] CMD command
    HEALTHCHECK NONE

    STOPSIGNAL signal

HEALTHCHECK指令告诉容器如何运行健康检查。如果容器的Dockerfile中指定了HEALTHCHECK方法，在运行 docker ps 命令时，容器的状态一栏中会显示容器当前是否健康。

STOPSIGNAL指令重写在 docker stop 命令执行时发送给容器的信号。

HEALTHCHECK指令有如下参数：

    --interval=DURATION     # 两次健康检查的间隔，默认30秒。
    --timeout=DURATION      # 健康检查的超时，默认30秒。
    --start-period=DURATION # 容器启动多久之后开始健康检查，默认0秒。
    --retries=N             # 健康检查失败之后显示容器不健康时经过多少次重试，默认3次。

### ONBUILD

    ONBUILD [INSTRUCTION]

ONBUILD指令后跟其他指令。ONBUILD指令的内容将不会在这个Docker构建的时候执行，但是如果其他Docker继承这个Docker，ONBUILD后跟的指令会在FROM结束之后立即执行。

### CMD 和 ENTRYPOINT

    CMD ["executable","param1","param2"]
    CMD command param1 param2
    CMD ["param1","param2"]

    ENTRYPOINT ["executable", "param1", "param2"]
    ENTRYPOINT command param1 param2

CMD指令和ENTRYPOINT指令几乎没有区别，他们的作用都是在容器构建之后执行其中的命令。他们也都有两种格式--shell和exec，正如RUN指令一样。区别在于CMD指令多一种参数模式，在参数模式下，CMD指令后跟的参数将作为默认参数传递给ENTRYPOINT指令执行。即下列两个命令在实际上是等价的：

    ENTRYPOINT ["/start.sh"]
    CMD ["aptly", "api", "serve"]

    ENTRYPOINT["/start.sh", "aptly", "api", "serve"]

他们的区别除此之外主要在于CMD指令会更容易的在 docker run 命令当中被重写，而ENTRYPOINT需要显式指定 --entrypoint 参数才能重写。

ENTRYPOINT指令和CMD指令之间的具体区别在网上五花八门，却很少有正确的。可以肯定的是，ENTRYPOINT指令的优先级要比CMD指令更高。这里按照Docker官方的说法：

**使用容器作为可执行文件时，应使用ENTRYPOINT指令。CMD应当被用于为ENTRYPOINT指令提供默认参数，或在容器中执行ad-hoc命令。**

下表列出了ENTRYPOINT指令和CMD指令不同组合时的实际执行情况：

|                           |No ENTRYPOINT              |ENTRYPOINT exec_entry p1_entry |ENTRYPOINT [“exec_entry”, “p1_entry”]          |
|---------------------------|---------------------------|-------------------------------|-----------------------------------------------|
|No CMD                     |error, not allowed	        |/bin/sh -c exec_entry p1_entry	|exec_entry p1_entry                            |
|CMD [“exec_cmd”, “p1_cmd”]	|exec_cmd p1_cmd	        |/bin/sh -c exec_entry p1_entry	|exec_entry p1_entry exec_cmd p1_cmd            |
|CMD [“p1_cmd”, “p2_cmd”]	|p1_cmd p2_cmd	            |/bin/sh -c exec_entry p1_entry	|exec_entry p1_entry p1_cmd p2_cmd              |
|CMD exec_cmd p1_cmd        |/bin/sh -c exec_cmd p1_cmd	|/bin/sh -c exec_entry p1_entry	|exec_entry p1_entry /bin/sh -c exec_cmd p1_cmd |

最后，还有一点需要强调：

**Dockerfile应至少指定一个CMD或ENTRYPOINT命令！**

## nvidia/cuda

了解了Docerfile的组成部分，让我们看看别人家都是怎么写Dockerfile的。以下是nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04及其继承的Dockerfile。

### 10.1-cudnn7-devel-ubuntu18.04

    ARG IMAGE_NAME
    FROM ${IMAGE_NAME}:10.1-devel-ubuntu18.04
    LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

    ENV CUDNN_VERSION 7.6.3.30
    LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

    RUN apt-get update && apt-get install -y --no-install-recommends \
        libcudnn7=$CUDNN_VERSION-1+cuda10.1 \
    libcudnn7-dev=$CUDNN_VERSION-1+cuda10.1 \
    && \
        apt-mark hold libcudnn7 && \
        rm -rf /var/lib/apt/lists/*

### 10.1-devel-ubuntu18.04

    ARG IMAGE_NAME
    FROM ${IMAGE_NAME}:10.1-runtime-ubuntu18.04
    LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

    RUN apt-get update && apt-get install -y --no-install-recommends \
            cuda-nvml-dev-$CUDA_PKG_VERSION \
            cuda-command-line-tools-$CUDA_PKG_VERSION \
    cuda-libraries-dev-$CUDA_PKG_VERSION \
            cuda-minimal-build-$CUDA_PKG_VERSION \
            libnccl-dev=$NCCL_VERSION-1+cuda10.1 \
    && \
        rm -rf /var/lib/apt/lists/*

    ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs

### 10.1-runtime-ubuntu18.04

    ARG IMAGE_NAME
    FROM ${IMAGE_NAME}:10.1-base-ubuntu18.04
    LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

    ENV NCCL_VERSION 2.4.8

    RUN apt-get update && apt-get install -y --no-install-recommends \
        cuda-libraries-$CUDA_PKG_VERSION \
    cuda-nvtx-$CUDA_PKG_VERSION \
    libnccl2=$NCCL_VERSION-1+cuda10.1 && \
        apt-mark hold libnccl2 && \
        rm -rf /var/lib/apt/lists/*

### 10.1-base-ubuntu18.04

    FROM ubuntu:18.04
    LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

    RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg2 curl ca-certificates && \
        curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub | apt-key add - && \
        echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 /" > /etc/apt/sources.list.d/cuda.list && \
        echo "deb https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list && \
        apt-get purge --autoremove -y curl && \
    rm -rf /var/lib/apt/lists/*

    ENV CUDA_VERSION 10.1.243

    ENV CUDA_PKG_VERSION 10-1=$CUDA_VERSION-1

    # For libraries in the cuda-compat-* package: https://docs.nvidia.com/cuda/eula/index.html#attachment-a
    RUN apt-get update && apt-get install -y --no-install-recommends \
            cuda-cudart-$CUDA_PKG_VERSION \
    cuda-compat-10-1 && \
    ln -s cuda-10.1 /usr/local/cuda && \
        rm -rf /var/lib/apt/lists/*

    # Required for nvidia-docker v1
    RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
        echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

    ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
    ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64

    # nvidia-container-runtime
    ENV NVIDIA_VISIBLE_DEVICES all
    ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
    ENV NVIDIA_REQUIRE_CUDA "cuda>=10.1 brand=tesla,driver>=384,driver<385 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411"

### ubuntu:18.04

    FROM scratch
    ADD ubuntu-bionic-core-cloudimg-amd64-root.tar.gz /
    # verify that the APT lists files do not exist
    RUN [ -z "$(apt-get indextargets)" ]
    # (see https://bugs.launchpad.net/cloud-images/+bug/1699913)

    # a few minor docker-specific tweaks
    # see https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap
    RUN set -xe \
        \
    # https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L40-L48
        && echo '#!/bin/sh' > /usr/sbin/policy-rc.d \
        && echo 'exit 101' >> /usr/sbin/policy-rc.d \
        && chmod +x /usr/sbin/policy-rc.d \
        \
    # https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L54-L56
        && dpkg-divert --local --rename --add /sbin/initctl \
        && cp -a /usr/sbin/policy-rc.d /sbin/initctl \
        && sed -i 's/^exit.*/exit 0/' /sbin/initctl \
        \
    # https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L71-L78
        && echo 'force-unsafe-io' > /etc/dpkg/dpkg.cfg.d/docker-apt-speedup \
        \
    # https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L85-L105
        && echo 'DPkg::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' > /etc/apt/apt.conf.d/docker-clean \
        && echo 'APT::Update::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' >> /etc/apt/apt.conf.d/docker-clean \
        && echo 'Dir::Cache::pkgcache ""; Dir::Cache::srcpkgcache "";' >> /etc/apt/apt.conf.d/docker-clean \
        \
    # https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L109-L115
        && echo 'Acquire::Languages "none";' > /etc/apt/apt.conf.d/docker-no-languages \
        \
    # https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L118-L130
        && echo 'Acquire::GzipIndexes "true"; Acquire::CompressionTypes::Order:: "gz";' > /etc/apt/apt.conf.d/docker-gzip-indexes \
        \
    # https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L134-L151
        && echo 'Apt::AutoRemove::SuggestsImportant "false";' > /etc/apt/apt.conf.d/docker-autoremove-suggests

    # make systemd-detect-virt return "docker"
    # See: https://github.com/systemd/systemd/blob/aa0c34279ee40bce2f9681b496922dedbadfca19/src/basic/virt.c#L434
    RUN mkdir -p /run/systemd && echo 'docker' > /run/systemd/container

    # overwrite this with 'CMD []' in a dependent Dockerfile
    CMD ["/bin/bash"]
