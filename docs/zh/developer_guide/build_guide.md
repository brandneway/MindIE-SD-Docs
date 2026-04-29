# 开发镜像构建
MindIE-SD 提供了基于Atlas 800I A2 推理服务器的AArch64环境的开发镜像定义文件 `docker/Dockerfile_910b_aarch64.ubuntu`。快速构建开发镜像可使用：

```bash
docker build --network=host -f docker/Dockerfile_910b_aarch64.ubuntu -t mindiesd:910b-aarch64-head .
```
详情请参见[使用 Dockerfile 构建开发镜像](../user_guide/install/source/dockerfile_instruction.md)。

# 本地Docker容器构建
MindIE-SD 提供了基于Vs Code Dev Container构建标准化容器的配置。详情请参见[使用 Dev Container 构建开发容器](../user_guide/install/source/devcontainer_instruction.md)。

# MindIE-SD 源码编译安装指导
详情请参见[源码编译安装](../user_guide/install/source/installation_from_source_code.md)。

如有更多开发环境构建方面的需求，请参阅[安装指南](../user_guide/install/README.md)。