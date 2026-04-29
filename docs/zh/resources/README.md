# 技术资源

本章节收录 MindIE-SD 相关的技术论文与研究报告。

## 技术论文

### RainFusion

- **RainFusion2.0** — [PDF](./tech_report/RainFusion2.0.pdf)

  RainFusion 是一种面向视频扩散模型的稀疏注意力方法，基于视频本身具有的时空相似性，对 Attention 进行自适应判断和稀疏计算，有效减少计算开销并提高推理速度。该方法将 Attention head 分为 Spatial、Temporal、Textural 三种稀疏类型，并引入轻量化在线判别模块（ARM）实时判定每个 head 的稀疏类型，从而在保持生成质量的同时大幅提升推理效率。
