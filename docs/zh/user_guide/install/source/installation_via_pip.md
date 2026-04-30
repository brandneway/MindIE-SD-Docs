# 开源whl文件安装

## 快速安装

```bash
pip install --trusted-host ascend.devcloud.huaweicloud.com -i https://ascend.devcloud.huaweicloud.com/pypi/simple/ mindiesd
```

>[!NOTE]说明
>
>- MindIE-SD 的开源whl文件中默认包含自定义算子相关的动态库，该动态库依赖Pytorch/torch_npu，安装时的Pytorch/torch_npu需与开源whl文件编译时的版本一致，否则可能会在使用MindIE-SD运行时触发**undefined symbol**报错。然而当前发布的开源whl文件没有明确对应的Pytorch/torch_npu版本，因此优先推荐使用源码编译安装方式，该方式可自动编译动态库，并自动依赖Pytorch/torch_npu。
>- 软件包名字叫**mindiesd**，与仓库名有些不一样
>- 当前whl文件仅可通过huaweicloud.com渠道获取，未通过其他源发布
