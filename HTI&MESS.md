    vm账号：Pink_Flatter@proton.me
    install url：https://customerconnect.vmware.com/downloads/info/slug/datacenter_cloud_infrastructure/vmware_vsphere/7_0
    Some learning notes:
        https://blog.51cto.com/u_748290/5526390     -   very clear
        https://blog.csdn.net/hl449006540/article/details/122159999     -   how to set ESXI
        https://www.cnblogs.com/haidragon/p/16843418.html       -   vCenter's vul exp notes
    register ID with some details:
        address: SACRAMENTO
        zip: 94203-0001
        state: California
        city: SACRAMENTO
        
如果打算构建一个基于VMware的虚拟化环境，需要先安装ESXi，然后再安装vCenter。

      ESXi是VMware的一种虚拟化操作系统，它可以直接安装在物理服务器上，并负责管理和运行虚拟机。
      ESXi提供了一系列功能，包括资源分配、网络管理、存储管理等，它是构建虚拟化环境的基础。
      vCenter是VMware的虚拟化管理平台，它提供了集中管理和监控虚拟化环境的功能。
      通过vCenter，你可以对多个ESXi主机进行集中管理，配置虚拟机、监控性能、实施高可用性和灾难恢复等。
      在安装过程中，你首先需要准备一台物理服务器，并在该服务器上安装ESXi操作系统。
      一旦ESXi安装完成并运行，你就可以使用ESXi主机上的vSphere客户端连接到ESXi主机，进行基本的配置和管理。
      然后，你可以安装vCenter服务器，它可以部署在物理服务器上，也可以作为虚拟机运行。
      vCenter服务器将允许你管理多个ESXi主机，并提供更高级的功能，如虚拟机迁移、负载均衡和资源调整等。
      总结起来，你需要先安装ESXi操作系统，然后再安装vCenter服务器来管理和监控你的虚拟化环境。

  
ESXi和vCenter可以安装在不同的操作系统上，具体取决于你的需求和环境。一些常见的选择：
  
      ESXi安装：ESXi是一种虚拟化操作系统，它通常直接安装在物理服务器上作为主机操作系统。
      你需要选择兼容的硬件并下载VMware提供的ESXi安装映像文件，然后将其刻录到光盘或制作成启动USB驱动器。
      在启动服务器时，选择从安装介质启动并按照安装向导进行安装。ESXi本身是一种裸机操作系统，不需要基于其他操作系统。

      vCenter安装：vCenter可以安装在物理服务器上，也可以作为虚拟机运行在支持的操作系统上。
      以下是不同部署方式的常见选择：
          物理服务器安装：
            你可以选择支持的操作系统，如Windows Server或Linux发行版（如CentOS、SUSE等），然后按照VMware提供的vCenter安装向导进行安装。
            这样部署的vCenter服务器将独立运行在物理服务器上。
          虚拟机安装：
            你可以在支持的虚拟化平台上创建一个虚拟机，并选择一个兼容的操作系统来安装vCenter。
            常见的虚拟化平台包括VMware ESXi、Microsoft Hyper-V、Oracle VirtualBox等。
            安装操作系统后，你可以按照VMware提供的vCenter安装向导来安装和配置vCenter。

      需要注意的是，vCenter的安装需求和兼容性可能会根据不同的版本和发布日期有所变化。
      因此，建议在安装前查阅VMware官方文档，以获取最新的安装要求和建议。
  
ESXi可以安装在虚拟机中。虽然ESXi通常作为物理服务器的操作系统来运行，但在特定的测试、实验或开发环境中，你也可以将ESXi安装在虚拟机中进行模拟和实践。

--------------
    gRPC和RPC都是远程过程调用（Remote Procedure Call）技术的一种，都允许一个程序在本地执行另一个位置的程序或服务的函数或过程。这两者之间有一些关联性，但也有重要的不同之处。
    
    RPC：RPC是一种通信方法，允许在网络上的不同系统之间进行函数调用。使用RPC，一个客户端应用程序可以像调用本地函数一样调用一个在远程服务器上运行的函数。这种方法隐藏了网络通信的细节，使得开发者可以像在单一系统中一样进行编程。RPC使用多种协议，包括HTTP，XML，JSON，或者更底层的协议如TCP/IP。
    
    gRPC：gRPC是Google开发的一种开源RPC系统，旨在为分布式系统提供高效、高性能的通信。gRPC使用HTTP/2作为传输协议，支持传统的请求-响应模式以及双向流式通信。gRPC使用Protocol Buffers (protobuf)作为接口定义语言和消息交换格式，提供了更高效的序列化和反序列化操作。此外，gRPC还支持多种编程语言，使得它能够在各种不同的系统和平台上使用。
    
    因此，gRPC是RPC的一个实现，但它使用了一些现代的技术和协议，提供了更高的性能和更强的灵活性。

--------------
RPC（Remote Procedure Call）和DCERPC（Distributed Computing Environment / Remote Procedure Call）都是允许一台计算机（客户端）请求另一台计算机（服务器）执行过程或函数的技术。DCERPC实际上是RPC的一种实现。

RPC：RPC是一种概
念，其核心思想是允许程序调用另一台计算机上的过程（函数），就像在本地调用一样。这个概念是通用的，并且可以在各种网络和传输协议上实现。RPC隐藏了底层网络通信的复杂性，使开发人员可以像编写本地程序一样编写分布式程序。

DCERPC：DCERPC是由Open Software Foundation为分布式计算环境（DCE）项目开发的一种RPC实现。它为远程过程调用提供了一种标准化和完善的方法，包括数据表示（使用NDR，网络数据表示）和协议细节，同时还提供了一些高级功能，如安全性和并发控制。
因此，DCERPC是RPC的一种具体实现，它遵循了RPC的基本概念，但为了满足特定的需求和场景，提供了一些额外的特性和功能。

-------------------------



bilibili：

    https://www.bilibili.com/video/BV1JZ4y1c7ro?p=37&vd_source=2829d49eac20f9f8f390fa78f8754035
    http://bilibili.iiitab.com/




## rpc、grpc、dcerpc

### （猜想）dcerpc 是否应用在 rest API 上？

**结论：**否，DCERPC协议和REST API是两种不同的技术，虽然它们都应用在分布式环境中进行通信，但它们在vCenter server中是独立的，工作在不同层级中。

    DCERPC是一种专门用于在分布式计算环境中进行远程过程调用的协议。在这种环境中，不同的系统或应用程序之间需要进行复杂的交互和数据共享。
    REST API是一种建立在HTTP协议上的，用于构建分布式系统和web服务的架构风格。它使用标准的HTTP方法（如GET，POST，DELETE等）来执行操作，并通常使用JSON或XML作为数据交换格式。

    在VMware vCenter Server的上下文中，DCERPC协议可能被用于在vCenter Server与其他系统（例如，管理的ESXi主机）之间进行底层的，复杂的交互。
    而REST API则通常被用于提供一个更高层次的，更易于使用的接口，供客户端应用程序（例如，vSphere Client或第三方管理工具）与vCenter Server进行交互。

### gRPC和DCERPC都是RPC（远程过程调用）的一种实现。

这些协议都遵循RPC的基本理念：允许一台计算机（客户端）调用另一台计算机（服务器）上的过程或函数。但是，它们各自的实现有所不同，针对的需求也有所不同。

    RPC：RPC是一个概念或者说是一个框架，其核心思想是在网络上的不同系统之间进行函数调用。该概念是通用的，并且可以在各种不同的网络和传输协议上实现。
    DCERPC：DCERPC是RPC的一种具体实现，由Open Software Foundation为分布式计算环境（DCE）项目开发。它在RPC的基础上添加了一些高级特性，如安全性和并发控制。
    gRPC：gRPC是Google开发的一种开源RPC系统，它使用HTTP/2作为传输协议，使用Protocol Buffers作为接口定义语言和消息交换格式。
    gRPC提供了一种高效，高性能的通信方式，支持多种编程语言，适用于在各种不同的系统和平台上使用。

可以将RPC视为一个更高级别的抽象，而gRPC和DCERPC则是这个抽象的具体实现。
