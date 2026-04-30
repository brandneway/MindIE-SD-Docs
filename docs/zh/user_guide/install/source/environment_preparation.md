# 环境准备

介绍安装**MindIE-SD**之前的相关环境准备。

## NPU驱动和固件

物理机需安装NPU驱动和固件。安装CANN前请确认已安装NPU驱动和固件，执行命令查询，若返回驱动相关信息且无异常，则可继续安装CANN；若未安装，请参考[安装NPU驱动和固件](https://www.hiascend.com/document/detail/zh/canncommercial/850/softwareinst/instg/instg_0005.html?Mode=PmIns&InstallType=local&OS=openEuler)进行安装。

   ```bash
   npu-smi info
   ```

## 安装Python并配置好pip源

若未安装，请参考[编译安装Python](https://www.hiascend.com/document/detail/zh/mindie/230/envdeployment/instg/mindie_instg_0087.html)章节在物理机或Docker容器内安装Python并配置好pip源。

>[!NOTE]说明
>
>- 当前CANN支持Python3.7.x至3.13.x版本，推荐安装Python3.10.x或者Python3.11.x。

## 安装CANN

物理机需安装CANN（如使用Docker容器开发，需在Docker容器内安装CANN）。若未安装，请按照《CANN 软件安装指南》中[安装CANN”](https://www.hiascend.com/document/detail/zh/canncommercial/850/softwareinst/instg/instg_0008.html?Mode=PmIns&InstallType=local&OS=openEuler)进行安装。

>[!NOTE]说明
>
>- 推荐安装最新版本CANN。
>- 当前 MindIE-SD 不依赖NNAL神经网络加速库，可以跳过安装NNAL。 

## 安装PyTorch和Torch NPU

若未安装，请参考《Ascend Extension for PyTorch 软件安装指南》中的[安装PyTorch](https://www.hiascend.com/document/detail/zh/Pytorch/730/configandinstg/instg/docs/zh/installation_guide/installation_via_binary_package.md)章节在物理机或Docker容器内安装PyTorch框架和torch_npu插件。

>[!NOTE]说明
>
>- PyTorch和torch_npu的版本需一一对应。
>- 当前 MindIE-SD 适配的PyTorch/torch_npu版本为2.1、2.6、2.7、2.8、2.9。 
>- 推荐安装2.9版本。

## 安装gcc、g++（可选）

如需源码编译安装MindIE-SD，请参考[编译安装gcc](https://www.hiascend.com/document/detail/zh/canncommercial/850/softwareinst/instg/instg_0062.html?Mode=PmIns&InstallType=netyum&OS=openEuler)、[g++安装](https://www.hiascend.com/document/detail/zh/canncommercial/850/softwareinst/instg/instg_0094.html?Mode=PmIns&InstallType=local&OS=openEuler)安装gcc、g++。

>[!NOTE]说明
>
>- 请确保安装gcc/g++版本大于或等于11.4.0。
