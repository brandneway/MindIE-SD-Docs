# pip源安装

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

## 快速安装

现在最简单的方式是通过pip源安装，我们的软件包名字叫mindiesd，与仓库名有些不一样。

```bash
pip install --trusted-host ascend.devcloud.huaweicloud.com -i https://ascend.devcloud.huaweicloud.com/pypi/simple/ mindiesd
```

## 每日构建安装

每日构建版本可供测试最新功能：

待提供...
