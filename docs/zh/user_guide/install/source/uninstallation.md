# 升级

卸载**MindIE-SD**需执行以下命令   

## 查看当前已安装的MindIE-SD安装路径

```bash
pip show mindiesd | grep Location
```

以Python3.11.1为例，默认安装路径为：/usr/local/lib/python3.11/site-packages/mindiesd

## 卸载MindIE-SD

```bash
pip uninstall mindiesd
```

## 确认是否卸载成功

查看默认安装路径下是否删除了mindiesd，若没有请手动删除。

>[!NOTE]说明
>
>- 此举是为了兼容旧版本。旧版本的MindIE-SD中的自定义算子是独立安装的，pip uninstall mindiesd无法卸载算子包，需手动删除。
