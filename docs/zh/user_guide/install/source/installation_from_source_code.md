# 源码编译安装

在某些情况下，您可能需要从源代码安装 MindIE SD，以便尝试最新功能，或者根据您的特定需求自定义库。您可以按照以下步骤从源代码安装 MindIE SD

## 1. 克隆仓库&进入项目

   ```bash
   git clone https://gitcode.com/Ascend/MindIE-SD && cd MindIE-SD
   ```

## 2. [可选] 安装依赖

   ```bash
   pip install -r requirements.txt
   ```

## 3. 编译

   - 方式一：

   ```bash
   python -m build --wheel --no-isolation
   ```

   - 方式二：

   ```bash
   python setup.py bdist_wheel
   ```

## 4. 安装

   - 方式一：常规安装（使用默认版本号）

     ```bash
     cd dist
     pip install mindiesd-*.whl
     ```

   - 方式二：开发者可编辑模式安装（可通过环境变量**MINDIE_SD_VERSION_OVERRIDE**修改版本号）

     ```bash
     pip install -e .
     ```
