# vSphere
vCenter-ESXI-vul

官网：https://marketplace.vmware.com/vsx/solutions

dell插件：https://www.dell.com/support/home/zh-cn/drivers/driversdetails?driverid=k7cpk ----- download：https://www.dell.com/support/home/zh-cn/drivers/driversdetails?driverid=k7cpk

华为插件：https://support.huawei.com/enterprise/en/doc/EDOC1000082514

Hitachi插件：https://marketplace.cloud.vmware.com/services/details/hitachi-storage-plug-in-for-vmware-vcenter-1-1?slug=true



补丁对比分析 jar包分析：

https://xz.aliyun.com/t/10524

https://www.anquanke.com/post/id/243098

https://hosch3n.github.io/2021/10/08/VMware-vCenter%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90%EF%BC%88%E4%BA%8C%EF%BC%89/

身份验证绕过：https://www.ctfiot.com/27905.html

https://xz.aliyun.com/t/9698

fiddler----https://www.telerik.com/download/fiddler/fiddler4



vsphere-client-serenity.jar 和 vsphere-client-virgo.jar：这些 jar 包通常包含 vCenter Server 的 Web 客户端和 API 相关的代码。你可以在这些包中找到 REST API 的相关实现和用户权限的处理逻辑。

vsphere-sdk.jar：这个 jar 包包含 vSphere SDK，这是一个用于与 vCenter Server 进行通信的库。如果你的应用使用了这个 SDK 来与 vCenter Server 进行通信，你可能会在这个 jar 包中找到 REST API 调用的相关代码。

vSphere-client-lib.jar 和 vmware-base.jar：这些 jar 包包含了 vCenter Server 的一些基础类和函数，可能包含处理用户权限的逻辑。
