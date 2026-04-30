# 开发工具与文档

本文档说明 MindIE SD 本地开发中常用的文档生成、开发镜像构建与提交前检查命令。

## 本地文档服务构建

MkDocs 是一个快速、简单且极其精美的静态网站生成器，旨在构建项目文档。文档源文件以 Markdown 编写，并通过单个 YAML 配置文件  mkdocs.yaml 进行配置。

环境依赖位于 `requirements/requirements-mkdocs.txt`。安装：

```bash
python -m pip install -r requirements/requirements-mkdocs.txt
```

本地生成实时预览HTML文档可使用以下命令：

```bash
# 仅构建中文
mkdocs serve -f mkdocs.yml
# 仅构建英文
mkdocs serve -f mkdocs-en.yml
```

本地预览方法：

http://127.0.0.1:8000/zh-cn/latest/ → 自动跳转中文版
http://127.0.0.1:8000/en/latest/ → 自动跳转英文版

## 开发镜像构建

仓库提供了基于Atlas 800I A2 推理服务器的AArch64环境的开发镜像定义文件 `docker/Dockerfile_910b_aarch64.ubuntu`。本地构建镜像可使用：

```bash
docker build --network=host -f docker/Dockerfile_910b_aarch64.ubuntu -t mindiesd:910b-aarch64-head .
```

## Lint 与提交前检查

Lint 相关依赖位于 `requirements/requirements-lint.txt`。首次在本地开发前，建议先安装并启用 `pre-commit`：

```bash
python -m pip install -r requirements/requirements-lint.txt
pre-commit install
pre-commit run --all-files
```

`pre-commit install` 会将仓库 hook 写入 `.git/hooks/pre-commit`。完成一次安装后，后续 `git commit` 会自动执行当前仓库默认启用的检查。

如果需要显式执行 Markdown 文档检查，请额外运行：

```bash
pre-commit run markdownlint --all-files --hook-stage manual
```

只有在明确需要绕过检查时，才使用 `git commit --no-verify`。
