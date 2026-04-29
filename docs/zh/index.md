---
hide:
  - navigation
---

# 欢迎使用 MindIE-SD

<div style="text-align: center; margin: 0.5rem 0 0.3rem 0; font-family: 'Avenir Next', 'Avenir', 'Century Gothic', 'Segoe UI', sans-serif;">
  <span style="font-size: 4.5rem; font-weight: 300; letter-spacing: 0.02em;">MindIE-SD</span>
</div>

MindIE SD（Mind Inference Engine Stable Diffusion，Diffusion系列大模型）旨在构建昇腾亲和的多模态加速系列套件，配合业内模型套件（如：diffusers），提升多模态推理在昇腾上的效率。主要专注于提供多模态生成的关键算子和融合算子，配合的昇腾亲和量化/稀疏算法，以存代算，多卡并行等策略，实现对diffusers模型的快速迁移和昇腾加速，未来会进一步扩展到多模态理解，全模态等场景的加速。

MindIE SD各模块间独立解耦设计，可单独使用也可以叠加使用。业内本身存在类似Cache-dit， xDiT等加速手段， 其效果与cache模块和parallelism模块功能相似，存在方案选择的问题。但是MindIE SD中其他组件依旧可以单独与之叠加使用，但各组件都使用了monkey patch。

MindIE SD基于PyTorch框架对外提供昇腾的加速能力，各加速能力支持独立使用，主要包含cache、parallelism、quantization、layer、compilation等模块，相关接口遵从diffusers的接口定义，部分基于MindIE SD实现昇腾加速的diffusers模型详情请参见在[Modelers](https://modelers.cn/models?name=MindIE&page=1&size=16)和[ModelZoo](https://www.hiascend.com/software/modelzoo)。


如何开始使用 MindIE-SD 取决于您的用户类型。如果您希望：

- 安装部署 MindIE-SD，推荐从 [安装指南](user_guide/install/README.md) 开始
- 快速体验运行开源模型，推荐从 [快速开始](user_guide/quick_start.md) 开始
- 了解目前已经支持的模型，推荐从 [支持模型](features/supported_matrix.md)
- 了解MindIE-SD的架构设计和支持的功能特性，推荐从[架构设计](architecture.md) 开始
- 参与构建MindIE-SD，推荐从 [开发者指南](developer_guide/README.md) 开始

有关 MindIE-SD 开发的信息，请参阅

- [路线图](https://gitcode.com/Ascend/MindIE-SD/issues/44)
- [发布](./release_note.md)

## 核心能力

MindIE SD 具备视图生成场景下的高性能推理加速能力：

- 昇腾亲和加速算子：提供高性能FA、MM、MoE、Quant类算子及融合算子
- 量化稀疏能力：针对昇腾数据类型和算力分布，提供亲和的量化与稀疏算法组合
- 以存代算：提供 DiT Block、Attention 等多种粒度的 Cache 加速算法
- 自动亲和加速：基于 torch.compile 的 Inductor 机制，自定义融合 Pass 实现昇腾自动算子替换
- 多卡并行：提供CFG、USP等并行能力，融入加速算子的API中，实现接口替换后的自动使能

MindIE SD 具备灵活易用的特性：

- 各个功能特性独立解耦，可单独使用也可叠加组合
- 接口遵从 diffusers 定义，支持简单插件化改造
- 兼容昇腾生态，支持基于 diffusers 快速迁移
- 完善的参数配置和环境变量体系

## 架构概览

MindIE SD 基于 PyTorch 框架对外提供昇腾加速能力，各模块独立解耦，主要包含：

- **layer 模块**：提供基础对外的加速接口（Attention、MatMul、Rope、Norm 等），是高阶特性的基础
- **ops 模块**：提供多模态生成相关的昇腾高性能算子实现，支持 AscendC 和 Triton 等算子接入
- **plugin 模块**：提供自定义算子的python接口注册，支持用户自定义算子接入
- **compilation 模块**：基于 FX Graph 的能力，开启 compile 后使能融合 Pass，实现昇腾自动亲和加速
- **quantization 模块**：支持量化能力的自动使能
- **cache_agent 模块**：提供以存代算的加速能力实现
- **eplb 模块**：面向DiT-MoE场景，构建了动态专家负载均衡的策略
- **parallelism 模块**：提供多卡并行的分布式加速能力，需要与layer模块和pytorch协同实现。


详情请参见 [架构设计](architecture.md)。

## 相关链接

- [昇腾社区](https://www.hiascend.com/)
- [MindIE 镜像仓库](https://www.hiascend.com/developer/ascendhub/detail/af85b724a7e5469ebd7ea13c3439d48f)
