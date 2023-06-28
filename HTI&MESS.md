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


bilibili：

    https://www.bilibili.com/video/BV1JZ4y1c7ro?p=37&vd_source=2829d49eac20f9f8f390fa78f8754035
    http://bilibili.iiitab.com/
