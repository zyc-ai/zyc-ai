---
title: 配置OpenSSH以通过跳板机连接大中央资源
summary: Config OpenSSH to connect to GCR by jumpianer
authors:
    - Zhiyuan Chen
date: 2021-04-06 17:04:10
categories: 
    - MSRA
tags:
    - MSRA
    - Grand Central Resource
    - Jumptainer
---

!!! warning "警告"

    本文档没有活跃维护人，因此可能不是最新的。本文档的编辑者应当恰当的使用引用，以方便用户在本文内容失效时按照引用内容更新。

    本文档最后更新于2021年11月22日，这表示本文档最后一次被验证的日期。

## 摘要

出于“零信任”的设计，使用大中央资源（Grand Central Resources, GCR)需要通过跳板机（Jumptainer）进行连接。

本文简要介绍了如何配置OpenSSH以通过跳板机连接到大中央资源，并对一些常见故障提供解决方案。

## OpenSSH服务

[参考](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse)

### OpenSSH可用性

OpenSSH应该已经在您的机器上安装。您可以通过以下步骤验证OpenSSH的可用状态：

```shell
Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'

> Name  : OpenSSH.Client~~~~0.0.1.0
> State : NotPresent / Installed

> Name  : OpenSSH.Server~~~~0.0.1.0
> State : NotPresent / Installed
```

如果状态（State）为已安装（Installed），代表您已正确安装OpenSSH，您可能会想跳过本节；如果状态为未出现（NotPresent），代表您尚未安装OpenSSH，您可能会想遵循接下来的步骤安装：

### 安装OpenSSH

```shell
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

> Path          :
> Online        : True
> RestartNeeded : False
```

### 安装OpenSSH服务端$^*$

$^*$：SSH服务端的安装与启动是为了方便您远程连接本机，如果您没有相关需求，这个步骤可以被跳过。

```shell
# 安装OpenSSH服务端
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

> Path          :
> Online        : True
> RestartNeeded : False

# 启动OpenSSH服务端
Start-Service sshd

# 设置OpenSSH服务端的自动启动（可选）
Set-Service -Name sshd -StartupType Automatic

# 验证ssh的防火墙配置正确
Get-NetFirewallRule -Name *ssh*
# 您应该可以看到一条名为“OpenSSH-Server-In-TCP”的防火墙规则，这个规则应该已经被打开
# 如果不存在这个防火墙规则，您可能会想创建一条新的规则
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH-Server-In-TCP(sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
```

## SSH公钥

[参考](https://dev.azure.com/msresearch/GCR/_wiki/wikis/GCR.wiki/4099/SSH-Key-Management)

为了连接至大中央资源，您需要将您的SSH公钥上传至大中央资源。

大中央资源目前支持的密钥类型包括：

+ RSA
+ DSS
+ ED25519
+ ECDSA-nistp256/384/521

### 创建SSH密钥

[参考](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)

如果您还没有一个ssh密钥，您可能会先想运行以下指令创建一个`id_ed25519`$^*$密钥：

```shell
ssh-keygen -t ed25519 -C "v-sanzhang@microsoft.com"
```

$^*$：您也可以创建一个其他受支持的密钥。

创建密钥时会要求您对密钥进行加密，您可能不希望这么做。

### 上传SSH公钥

通过`cat ~/.ssh/id_ed25519.pub`以获取您的`id_ed25519`$^*$公钥的内容，并将其复制到[大中央资源公钥管理](https://aka.ms/gcrssh)。

$^*$：您的具体公钥的名称可能会有所不同。

## SSH身份验证代理

[参考](https://dev.azure.com/msresearch/GCR/_wiki/wikis/GCR.wiki/3938/GCR-Jumptainer-)

要验证SSH身份验证代理配置正确性，遵循以下步骤：

```shell
ssh-add -l

> 4096 SHA256:******************************************* C:\Users\v-sanzhang/.ssh/id_rsa (RSA)
> 256 SHA256:******************************************* v-sanzhang@microsoft.com (ED25519)
```

!!! error "The agent has no identities."

    如果输出为`The agent has no identities.`，代表您没有将SSH密钥添加至身份验证代理中。

    运行`ssh-add ~/.ssh/id_ed25519`以将SSH密钥添加至身份验证代理。

!!! error "Error connecting to agent: No such file or directory"

    如果输出为`Error connecting to agent: No such file or directory，代表SSH身份验证代理没有正常启动。

    运行`Start-Service ssh-agent`以启动SSH身份验证代理，或者
    运行`Set-Service ssh-agent -StartupType Automatic`以设置SSH身份验证代理的自动启动。

## SSH配置文件

以下展示了一个alias为`v-sanzhang`的同学的SSH配置文件。其中包括了一台Azure云主机（meow.southeastasia.cloudapp.azure.com）、一台Windows沙箱（Sandbox）主机（10.8.16.188）和一台Linux沙箱主机（10.8.17.188）。

```config
Host vm
  User v-sanzhang
  HostName meow.southeastasia.cloudapp.azure.com
  IdentityFile ~/.ssh/id_rsa
  Port 333

Host jumptainer
  HostName jumptainer.westus2.cloudapp.azure.com
  Port 22222

Host *
  User FAREAST.v-sanzhang
  ForwardAgent yes
  ForwardX11 yes
  Compression yes
  Protocol 2
  ServerAliveInterval 60
  NoHostAuthenticationForLocalhost yes
  IdentityFile ~/.ssh/id_ed25519

Host wdev
  HostName jumptainer.westus2.cloudapp.azure.com
  Port 22222
  LocalForward 8992 10.8.16.188:3389
  RequestTTY force
  RemoteCommand /usr/bin/watch -n 60 ls

Host dev
  HostName 10.8.17.188
  ProxyJump jumptainer
```

!!! "CreateProcessW failed error:2 posix_spawn: No such file or directory"

    如果您确定[SSH身份验证代理](#SSH身份验证代理)的配置正确，代表您的系统可能不支持`ProxyJump`指令。

    请将`ProxyJump jumptainer`替换为`ProxyCommand C:\\Windows\\System32\\OpenSSH\\ssh.exe -q -W %h:%p jumptainer`。

## 致谢

感谢`v-sanzhang`同学提供了自己的alias。
