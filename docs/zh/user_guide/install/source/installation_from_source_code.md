# 源码安装

## 安装依赖

* OS: Linux
* Python: >=3.10
* Pytorch：2.6, 2.7, 2.8, 2.9
* torch-npu: 2.6, 2.7, 2.8, 2.9
* CANN: 8.5.1

### 注意事项

1. MindIE SD主要依赖torch-npu的版本，会尽力满足其要求的CANN以及Python版本要求。
2. CANN版本安装后，安装路径下提供进程级环境变量设置脚本“set_env.sh“，以自动完成环境变量设置，该脚本包含如[表1 环境变量](#table_environment0001)所示中的LD_LIBRARY_PATH和ASCEND_CUSTOM_OPP_PATH，用户进程结束后自动失效。

**表 1**  环境变量<a id="table_environment0001"></a>

|环境变量|说明|
|--|--|
|LD_LIBRARY_PATH|动态库的查找路径。|
|ASCEND_CUSTOM_OPP_PATH|推理引擎自定义算子包安装路径。|
|ASCEND_RT_VISIBLE_DEVICES|指定当前进程所用的昇腾AI处理器的逻辑ID，如有需要请自行配置。<br>配置示例："0,1,2"或"0-2"；昇腾AI处理器的逻辑ID间使用“,”表示分割，使用“-”表示连续。|

## 源码安装步骤

在某些情况下，您可能需要从源代码安装 MindIE SD，以便尝试最新功能，或者根据您的特定需求自定义库。

您可以按照以下步骤从源代码安装 MindIE SD

### 1. 克隆仓库&进入项目：

   ```bash
   git clone https://gitcode.com/Ascend/MindIE-SD && cd MindIE-SD
   ```
### 2. [可选] 安装依赖：

   ```bash
   pip install -r requirements/requirements.txt
   ```
### 3. 编译：
   - 方式一：
   ```bash
   python -m build --wheel --no-isolation
   ```
   - 方式二：
   ```bash
   python setup.py bdist_wheel
   ```

### 4. 安装：

   - 方式一：常规安装（使用默认版本号）

     ```bash
     cd dist
     pip install mindiesd-*.whl
     ```

   - 方式二：开发者可编辑模式安装（可通过环境变量MINDIE_SD_VERSION_OVERRIDE修改版本号）

     ```bash
     pip install -e .
     ```