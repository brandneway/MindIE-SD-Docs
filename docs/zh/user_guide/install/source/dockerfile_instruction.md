# MindIE SD Dockerfile 使用指导

## 说明

本Dockerfile仅适用于Atlas 800I A2 推理服务器（AArch64）。

[docker/Dockerfile_910b_aarch64.ubuntu](https://gitcode.com/Ascend/MindIE-SD/blob/dev/docker/Dockerfile_910b_aarch64.ubuntu) 基于 CI 镜像定义 `MindIE-CI/env/version/Dockerfile.py311.arm._2.9.0` 构建。在此基础上，保留了主 CI 构建链：

- `ubuntu:24.04`
- Python `3.11.4`
- CANN `8.5.1`
- `torch 2.9.0`
- 对应的 `torch_npu`

与 MindIE-SD 相关的特定修改仅限于：

- 将 `MindIE-SD` 源码树复制到镜像中
- 安装工作空间的 `requirements.txt`
- 运行 `python3.11 -m build --wheel --no-isolation`
- 将 `/workspace/MindIE-SD` 设为工作目录

## 构建镜像示例

```bash
git clone https://gitcode.com/Ascend/MindIE-SD && cd MindIE-SD
docker build --network=host -f docker/Dockerfile_910b_aarch64.ubuntu -t mindiesd:910b-aarch64-head .
```

## 构建容器示例

```bash
docker run -itd \
  --name mindiesd-910b-test \
  --privileged \
  --ipc=host \
  --net=host \
  -v /usr/local/Ascend/driver:/usr/local/Ascend/driver:ro \
  -v /usr/local/sbin:/usr/local/sbin:ro \
  mindiesd:910b-aarch64-head
```

## 容器内运行MindIE SD全量测试用例

```bash
docker exec -it mindiesd-910b-test bash -lc 'python3 -m pip install coverage && cd /workspace/MindIE-SD && bash tests/run_test.sh --all'
```
