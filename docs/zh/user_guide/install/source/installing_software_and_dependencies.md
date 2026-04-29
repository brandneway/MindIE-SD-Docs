# 安装软件包和依赖

介绍安装MindIE前，需要安装的相关软件包和依赖。

## 安装CANN

需要安装的CANN软件包包括：Toolkit开发套件包、ops算子包和NNAL神经网络加速库。

### 前提条件

宿主机已经安装过NPU驱动和固件。如未安装，请参见《CANN 软件安装指南》中的“[选择安装场景](https://www.hiascend.com/document/detail/zh/canncommercial/850/softwareinst/instg/instg_0000.html?Mode=PmIns&InstallType=local&OS=openEuler)”章节（商用版）或“[选择安装场景](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/850/softwareinst/instg/instg_0000.html?Mode=PmIns&InstallType=local&OS=openEuler)”章节（社区版），按如下方式选择安装场景，按“**安装NPU驱动和固件**”章节进行安装。

- 安装方式：选择“在物理机上安装”。
- 操作系统：选择使用的操作系统，MindIE支持的操作系统请参考[硬件配套和支持的操作系统](../installation_introduction.md)。
- 安装类型：根据在线或离线的安装方式，选择对应的安装类型。

### 安装

请参见《CANN 软件安装指南》中的“[选择安装场景](https://www.hiascend.com/document/detail/zh/canncommercial/850/softwareinst/instg/instg_0000.html?Mode=PmIns&InstallType=local&OS=openEuler)”章节（商用版）或“[选择安装场景](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/850/softwareinst/instg/instg_0000.html?Mode=PmIns&InstallType=local&OS=openEuler)”章节（社区版），并按如下方式选择安装场景，选择完成后单击“开始阅读”，按“**安装CANN**”章节进行安装。

- 安装方式：选择“在物理机上安装”。
- 操作系统：选择使用的操作系统，MindIE支持的操作系统请参考[硬件配套和支持的操作系统](../installation_introduction.md)。
- 安装类型：根据在线或离线的安装方式，选择对应的安装类型。

## 安装Pytorch和Torch NPU

- 如果操作系统是ubuntu 22.04，请安装torch_npu 2.1.0；如果操作系统是ubuntu 24.04 LTS，请安装torch_npu 2.9.0。
- 请参见《Ascend Extension for PyTorch 软件安装指南》中的“[安装PyTorch](https://www.hiascend.com/document/detail/zh/Pytorch/730/configandinstg/instg/docs/zh/installation_guide/installation_via_binary_package.md)”章节安装PyTorch框架和torch_npu插件。

MindIE中各组件依赖PyTorch框架和torch_npu插件，依赖情况如下表所示，请用户依据实际使用需求安装。

**表 1** MindIE各组件依赖PyTorch框架和torch_npu插件说明表

|组件名称|是否需要安装PyTorch框架|是否需要安装torch_npu插件|
|--|--|--|
|MindIE Motor|**必装**|**必装**|
|MindIE LLM|**必装**|**必装**|
|MindIE SD|**必装**|**必装**|

> **注意**：使用 Python 3.10 环境编译，需配套 torch 2.9.0 版本 + torch_npu 2.9.0 版本,
否则会导致 \_bz2 模块缺失，从而导致编译失败。

## 安装依赖

### 安装前必读

- 请提前安装Python并配置好pip源。
- 建议执行命令`pip3 install --upgrade pip`进行升级（pip版本需大于或等于24.0），避免因pip版本过低导致安装失败。

## 安装步骤

1. 请用户自行准备依赖安装文件requirements.txt，样例如下所示。

    ```text
    diffusers==0.29.0
    transformers==4.44.2
    open_clip_torch==2.26.1
    av==12.0.0
    tqdm==4.66.5
    timm==0.9.12
    tensorboard==2.20.0
    pre-commit==3.8.0
    mmengine==0.10.4
    ftfy==6.1.3
    accelerate==0.26.1
    bs4
    torchvision==0.24.0
    einops
    numpy==1.26.4
    strenum
    zmq
    ```

2. 执行以下命令进行安装。以下命令如果使用非root用户安装，需要在安装命令后加上`--user`，安装命令需在`requirements.txt`所在目录执行。

    ```bash
    pip3 install -r requirements.txt
    ```
