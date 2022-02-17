---
title: 配置AVD以在任何设备上访问公司资源
summary: Config AVD to access company resources on any device
authors:
    - Zhiyuan Chen
date: 2022-02-16 18:36:21
categories: 
    - MSRA
tags:
    - MSRA
    - Remote
    - Azure vDesktop
---

!!! warning "警告"

    本文档没有活跃维护人，因此可能不是最新的。本文档的编辑者应当恰当的使用引用，以方便用户在本文内容失效时按照引用内容更新。

    本文档最后更新于2022年02月16日，这表示本文档最后一次被验证的日期。

## 摘要

出于“零信任”的设计，许多服务的访问都需要微软内网的连接。对于Windows用户而言，通过VPN连接微软内网需要将设备通过公司门户注册成为公司设备，这对于个人设备来说较为不方便。此外，iOS、Android和Linux用户难以使用VPN。

本文介绍了如何配置Azure vDesktop (AVD)以通过Remote Desktop连接到微软内网，并通过Jumpbox远程连接主机。

## 微软设备（MSFT Device）

微软设备是指微软所有的设备。加入AAD（Azure Active Directory）会将您的设备设置为微软设备，这将给您对微软资源的完全访问（包括对MSFT VPN的访问），同时也给公司对设备的所有控制权。将自己的加入AAD对于长期员工来说是十分方便的，但是对于短期实习生来说，这可能会引入额外的麻烦。

## AVD

AVD允许任何（包括非微软设备）访问微软资源。您可以用任何您想用的设备远程连接到您的电脑上来跑实验，不管是您的个人电脑，平板电脑抑或是手机，甚至是您家的台灯（如果它有一个支持HTML-5的浏览器的话）。

请访问[https://aka.ms/installavdclient](https://aka.ms/installavdclient)来安装一个Remote Desktop客户端。

打开Remote Desktop，登录到您的微软账户，应该可以看到如图所示的界面。选择一个离您最近的区域（一般来说是亚洲），选择vDesktop打开即可。

如果您没有看到任何设备，您需要首先加入AVD Enterprise。请访问[http://aka.ms/JoinAVDEnterprise](http://aka.ms/JoinAVDEnterprise)来加入AVD Enterprise。

### 使用AVD

AVD是一个共享机器，可用的软件包括：

+ Teams
+ Edge
+ Office全家桶 (Outlook, Word, Excel, Visio, PowerPoint, OneNote, Project, Publisher, Access)
+ Acrobat Reader
+ Power BI
+ 远程桌面连接（Remote Desktop Connection）
+ OneDrive
+ SAP GUI (SAP Business Intelligence add-ins for M365 Office apps, and SAP Login)

您 **不可以** 在AVD上安装任何软件。

### Jumpbox

尽管AVD允许您访问一定的公司资源，但您没有权限安装任何程序，甚至不能运行Powershell。但是您可以通过AVD远程连接到您的计算机。但我们更推荐通过Jumpbox（而非vDesktop）进行远程连接。

打开Jumpbox或者AVD上的Remote Desktop Connection，输入您的计算机名，然后点击“连接”。

## 致谢

感谢`v-jinzzhang`提供了远程连接的教程。
