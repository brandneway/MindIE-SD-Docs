# Layer级核心加速接口

本文档描述 `mindiesd` 包 `layers` 模块中的接口，是针对layer层级优化的核心加速接口。所有接口均可通过 `from mindiesd import <接口名>` 直接导入使用。

## def rotary_position_embedding

**函数功能**

旋转位置编码技术可以提升DiT模型在处理序列数据时的性能和效率，其具体使用方法请参见[RoPE](../features/core_layers.md#rotary_position_embedding)。

**函数原型**

```python
def rotary_position_embedding(x: torch.Tensor,
                              cos: torch.Tensor,
                              sin: torch.Tensor,
                              rotated_mode: str = "rotated_half",
                              head_first: bool = False,
                              fused: bool = True) -> torch.Tensor:
```

**参数说明**

|参数名|输入/输出|类型|说明|
|--|--|--|--|
|x|输入|torch.Tensor|应用旋转嵌入的q或k张量，shape要求输入为4维，一般为[B, N, S, D]或[B, S, N, D]或[S, B, N, D]。x可表示为 [x_0, x_1,..., x_d/2-1, x_d/2, x_d/2+1,..., x_d-1]。|
|cos|输入|torch.Tensor|预计算的复指数cos频率张量。shape要求输入为2维或4维，一般为[S,D]或[1, 1, S, D]或[1, S, 1, D]或[S, 1, 1, D]。|
|sin|输入|torch.Tensor|预计算的复指数sin频率张量。shape要求输入为2维或4维，一般为[S,D]或[1, 1, S, D]或[1, S, 1, D]或[S, 1, 1, D]。|
|rotated_mode|输入|str|旋转模式：支持rotated_half和rotated_interleaved两种模式。<ul><li>rotated_half：对半旋转，将x旋转为[-x_d/2, -x_d/2+1,..., -x_d-1, x_0, x_1,..., x_d/2-1]。</li><li>rotated_interleaved：相邻旋转，将x旋转为[-x_1, x_0, -x_3, x_2,..., -x_d-1, x_d-2]。</li></ul>|
|head_first|输入|bool|当x的layout中，head_dim在seqlen前面时，设置为True，否则设置为False。|
|fused|输入|bool|是否开启融合操作。<ul><li>True：选择高性能的RoPE融合算子。</li><li>False：使用原始计算公式。</li></ul>|

<br>

**返回值说明**

返回经旋转嵌入修改后的q张量和k张量。

## def attention_forward

**函数功能**

注意力计算模块，集成多种计算模式，包含原始计算模式、多种近似优化，用于搜索最优的计算公式，其具体使用方法请参见[attention_forward](../features/core_layers.md#attention_forward)。

**函数原型**

```python
def attention_forward(query, key, value, attn_mask=None, scale=None, fused=True, **kwargs):
```

**参数说明**

|参数名|输入/输出|类型|说明|
|--|--|--|--|
|query|输入|torch.Tensor|注意力计算公式的q输入，输入格式必须为(batch, seq_len, num_heads, head_dim)。|
|key|输入|torch.Tensor|注意力计算公式的k输入，输入格式必须为(batch, seq_len, num_heads, head_dim)。|
|value|输入|torch.Tensor|注意力计算公式的v输入，输入格式必须为(batch, seq_len, num_heads, head_dim)。|
|attn_mask|输入|torch.Tensor|注意力掩码。|
|scale|输入|float|输入缩放。|
|fused|输入|bool|是否开启融合操作。<ul><li>True：可选择融合算子。</li><li>False：使用原始计算公式，即缩放点积注意力（scaled dot-product attention）。</li></ul>|
|kwargs|输入|-|其他参数，包含以下三个可选项：<ul><li>opt_mode：str类型，支持runtime、static和manual三种模式，默认为runtime。<br>- runtime：在运行时动态搜索最佳融合算子，仅第一次搜索会消耗时间。<br>- static：通过静态表获取最佳融合算子。<br>- manual：手动设置融合算子类型。</li><li>op_type：str类型，表示融合算子类型，支持prompt_flash_attn、fused_attn_score和ascend_laser_attention。</li><li>layout：str类型，表示注意力机制布局方式，仅当opt_mode参数设置为manual时生效，支持BNSD、BSND和BSH。</li></ul>|

<br>

**返回值说明**

返回搜索后的最优注意力计算公式。

>[!NOTE]说明
>
>- 接口的输入shape为(batch, seq_len, num_heads, head_dim)，输出shape为(batch, seq_len, num_heads, head_dim)。
>- manual模式下设置算子的layout只会影响内部算子执行的layout，接口的输入shape和输出shape依然为(batch, seq_len, num_heads, head_dim)。

## def attention_forward_varlen

**函数功能**

不等长场景的注意力计算模块，其具体使用方法请参见[attention_forward_varlen](../features/core_layers.md#attention_forward_varlen)。

**函数原型**

```python
def attention_forward_varlen(
        q: torch.Tensor,
        k: torch.Tensor,
        v: torch.Tensor,
        cu_seqlens_q: list[torch.Tensor],
        cu_seqlens_k: list[torch.Tensor],
        max_seqlen_q: Optional[int] = None,
        max_seqlen_k: Optional[int] = None,
        dropout_p: float = 0.0,
        softmax_scale: Optional[float] = None,
        causal: bool = False,
        window_size: Optional[int] = None,
        softcap: Optional[float] = None,
        alibi_slopes: Optional[torch.Tensor] = None,
        deterministic: Optional[bool] = None,
        return_attn_probs: Optional[bool] = None,
        block_table: Optional[torch.Tensor] = None,
):
```

**参数说明**

|参数名|输入/输出|类型|说明|
|--|--|--|--|
|q|输入|torch.Tensor|查询(Query)张量。输入格式必须为(total_q, num_heads, head_dim)。total_q 是 batch 中所有query序列长度的总和（即“packed”格式，无填充）。num_heads 是注意力头数，head_dim 是每个头的维度。|
|k|输入|torch.Tensor|键(Key)张量。输入格式必须为(total_k, num_heads, head_dim)。total_k 是 batch 中所有key序列长度的总和（即“packed”格式，无填充）。num_heads 是注意力头数，head_dim 是每个头的维度。|
|v|输入|torch.Tensor|值(Value)张量。输入格式必须为(total_v, num_heads, head_dim)。total_v 是 batch 中所有value序列长度的总和（即“packed”格式，无填充）。num_heads 是注意力头数，head_dim 是每个头的维度。|
|cu_seqlens_q|输入|list[torch.Tensor]|查询序列的累积长度，用于将 packed 的 q 张量分割成独立序列。|
|cu_seqlens_k|输入|list[torch.Tensor]|键/值序列的累积长度。用于索引 k 和 v。|
|max_seqlen_q|输入|-|该参数仅支持与flash_attn_varlen_func保持一致，npu无需配置该参数，也不支持该参数。|
|max_seqlen_k|输入|-|该参数仅支持与flash_attn_varlen_func保持一致，npu无需配置该参数，也不支持该参数。|
|dropout_p|输入|float|表示数据需要忽略的概率，默认值为0.0，推理阶段建议保持默认值即可。|
|softmax_scale|输入|float|表示对QKT的缩放系数，若为None，则会根据head_dim ** -0.5进行缩放|
|causal|输入|bool|<ul><li>causal=true时，算子会传入下三角形式的atten mask；</li><li>causal=false时，算子不会传入atten mask。</li></ul>|
|window_size|输入|-|仅接口参数与flash_attn_varlen_func保持一致，npu无需配置该参数，也不支持该参数。|
|softcap|输入|-|该参数仅支持与flash_attn_varlen_func保持一致，npu无需配置该参数，也不支持该参数。|
|alibi_slopes|输入|-|该参数仅支持与flash_attn_varlen_func保持一致，npu无需配置该参数，也不支持该参数。|
|deterministic|输入|-|该参数仅支持与flash_attn_varlen_func保持一致，npu无需配置该参数，也不支持该参数。|
|return_attn_probs|输入|-|该参数仅支持与flash_attn_varlen_func保持一致，npu无需配置该参数，也不支持该参数。|
|block_table|输入|-|该参数仅支持与flash_attn_varlen_func保持一致，npu无需配置该参数，也不支持该参数。|

**返回值说明**

返回不等长场景的注意力机制的输出张量。

## def sparse_attention

**函数功能**

稀疏注意力前向计算接口，支持RainFusion（rf_v2）和自适应块稀疏（ada_bsa）两种稀疏策略，其具体使用方法请参见[sparse_attention](../features/core_layers.md#sparse_attention)。

**函数原型**

```python
def sparse_attention(
    q: torch.Tensor,
    k: torch.Tensor,
    v: torch.Tensor,
    attn_mask: Optional[torch.Tensor] = None,
    scale: Optional[float] = None,
    is_causal: Optional[bool] = False,
    head_num: int = 1,
    input_layout: str = "BNSD",
    inner_precise: int = 0,
    sparse_type: Optional[str] = None,
    txt_len: int = 0,
    block_size: int = 128,
    latent_shape_q: Optional[list] = None,
    latent_shape_k: Optional[list] = None,
    keep_sink: Optional[bool] = True,
    keep_recent: Optional[bool] = True,
    cdf_threshold: float = 1.0,
    sparsity: float = 0.0,
    **kwargs
):
```

**参数说明**

|参数名|输入/输出|类型|说明|
|--|--|--|--|
|q|输入|torch.Tensor|查询张量。若input_layout为'BNSD'，shape为[batch, head, qseqlen, headdim]；若input_layout为'BSND'，shape为[batch, qseqlen, head, headdim]。|
|k|输入|torch.Tensor|键张量。若input_layout为'BNSD'，shape为[batch, head, kseqlen, headdim]；若input_layout为'BSND'，shape为[batch, kseqlen, head, headdim]。|
|v|输入|torch.Tensor|值张量。若input_layout为'BNSD'，shape为[batch, head, vseqlen, headdim]；若input_layout为'BSND'，shape为[batch, vseqlen, head, headdim]。|
|attn_mask|输入|torch.Tensor|注意力掩码，预留参数。|
|scale|输入|float|注意力计算公式的输入缩放，若为None，则自动设置为headdim ** -0.5。|
|is_causal|输入|bool|是否对注意力矩阵应用因果掩码。|
|head_num|输入|int|注意力头数量，默认值为1。|
|input_layout|输入|str|张量布局，支持'BNSD'或'BSND'，默认值为'BNSD'。|
|inner_precise|输入|int|计算精度模式，0表示高精度，1表示高性能，默认值为0。|
|sparse_type|输入|str|稀疏类型，支持None、'rf_v2'、'ada_bsa'，默认值为None。|
|txt_len|输入|int|文本序列长度，仅在sparse_type为'rf_v2'时生效，默认值为0。|
|block_size|输入|int|块大小，当前仅支持128，默认值为128。|
|latent_shape_q|输入|list|查询的潜空间形状[t, h, w]，t*h*w = qseqlen，仅在sparse_type为'rf_v2'时生效。|
|latent_shape_k|输入|list|键的潜空间形状[t, h, w]，t*h*w = kseqlen，仅在sparse_type为'rf_v2'时生效。|
|keep_sink|输入|bool|是否保留sink token，仅在sparse_type为'ada_bsa'时生效，默认值为True。|
|keep_recent|输入|bool|是否保留recent token，仅在sparse_type为'ada_bsa'时生效，默认值为True。|
|cdf_threshold|输入|float|CDF阈值，仅在sparse_type为'ada_bsa'时生效，默认值为1.0。|
|sparsity|输入|float|稀疏率，取值范围[0, 1]，0表示不使用稀疏算法，默认值为0.0。|

**返回值说明**

返回稀疏注意力计算结果，布局与输入一致。

## class RMSNorm

### 类说明

RMSNorm（Root Mean Square Normalization，均方根归一化）是一种归一化方法，与LayerNorm类似，但它不计算输入张量的均值，而是直接基于输入张量的平方均值（Root Mean Square，RMS）进行归一化操作。这种方法在某些深度学习模型中（如：T5）被广泛使用，因为它可以减少计算复杂度并提升性能。该模块的主要功能是对输入张量hidden\_states进行归一化，并通过可学习的权重参数weight对归一化后的结果进行缩放，其具体使用方法请参见[RMSNorm](../features/core_layers.md#rmsnorm)。

**成员**

|成员名称|描述|
|--|--|
|__init__|类初始化函数。|
|weight|类成员变量，可学习的权重参数，形状为(hidden_size,)，初始值为全1的张量。用于对归一化后的结果进行缩放。|
|variance_epsilon|类成员变量，归一化过程中使用的平滑因子，防止数值不稳定。|
|forward|根据设备类型（是否支持NPU）选择不同的实现方式，对输入张量hidden_states进行RMS归一化操作。|

### def \_\_init__

**函数功能**

类初始化函数。

**函数原型**

```python
def __init__(self, hidden_size, eps=1e-6):
```

**参数说明**

|参数名|输入/输出|类型|说明|
|--|--|--|--|
|hidden_size|输入|torch.Tensor|输入张量的最后一维大小（即隐藏层的维度）。用于初始化归一化权重参数weight的形状。|
|eps|输入|float|一个小的常数，用于防止除零错误。默认值为1e-6。|

**返回值说明**

无

### def forward

**函数功能**

根据参数if_fused选择不同的实现方式，对输入张量hidden_states进行RMS归一化操作。

**函数原型**

```python
def forward(self, hidden_states, if_fused=True):
```

**参数说明**

|参数名|输入/输出|类型|说明|
|--|--|--|--|
|hidden_states|输入|torch.Tensor|输入张量，形状通常为(batch_size, sequence_length, hidden_size)或类似的多维张量。最后一维的大小必须等于hidden_size。|
|if_fused|输入|bool|是否使用融合算子，默认为True。|

**返回值说明**

归一化后的张量，形状与输入张量hidden_states相同。

## def fast_layernorm

**函数功能**

高性能LayerNorm融合算子，支持多种计算精度模式，其具体使用方法请参见[fast_layernorm](../features/core_layers.md#fast_layernorm)。

**函数原型**

```python
def fast_layernorm(norm: torch.nn.LayerNorm,
                   x: torch.Tensor,
                   impl_mode: int = 0,
                   fused: bool = True) -> torch.Tensor:
```

**参数说明**

|参数名|输入/输出|类型|说明|
|--|--|--|--|
|norm|输入|torch.nn.LayerNorm|PyTorch LayerNorm实例。|
|x|输入|torch.Tensor|输入张量，必须为3维，支持的布局为[B,S,H]。|
|impl_mode|输入|int|指定kernel的计算模式，取值必须在[0, 1, 2]中，默认值为0。0表示高精度模式，1表示高性能模式，2表示float16模式。float16模式仅当所有输入均为float16时可用。|
|fused|输入|bool|是否使用融合算子。<ul><li>True：可通过指定impl_mode启用不同的layernorm模式。</li><li>False：回退到标准torch.nn.LayerNorm计算。</li></ul>|

**返回值说明**

返回LayerNorm计算结果，形状与输入x一致。

## def layernorm_scale_shift

**函数功能**

自适应LayerNorm（AdaLayerNorm）融合算子，在LayerNorm基础上添加自适应缩放和偏移。计算公式：out = layernorm(x) * (1 + scale) + shift，其具体使用方法请参见[layernorm_scale_shift](../features/core_layers.md#layernorm_scale_shift)。

**函数原型**

```python
def layernorm_scale_shift(layernorm: torch.nn.LayerNorm,
                          x: torch.Tensor,
                          scale: torch.Tensor,
                          shift: torch.Tensor,
                          fused: bool = True) -> torch.Tensor:
```

**参数说明**

|参数名|输入/输出|类型|说明|
|--|--|--|--|
|layernorm|输入|torch.nn.LayerNorm|PyTorch LayerNorm实例。|
|x|输入|torch.Tensor|输入张量，必须为3维，支持的布局为[B,S,H]。|
|scale|输入|torch.Tensor|自适应缩放参数，必须为2维或3维，支持的布局为[B,H]或[B,1,H]。|
|shift|输入|torch.Tensor|自适应偏移参数，必须为2维或3维，支持的布局为[B,H]或[B,1,H]。|
|fused|输入|bool|是否使用融合算子。<ul><li>True：使用高性能AdaLayerNorm算子。</li><li>False：使用原始计算公式。</li></ul>|

**返回值说明**

返回AdaLayerNorm计算结果，形状与输入x一致。

>[!NOTE]说明
>
>- x的最后一维必须与scale、shift的最后一维相等。
>- 若scale或shift为3D张量，则第二维必须为1。

## def get_activation_layer

**函数功能**

从字符串中获取激活函数的辅助函数，其具体方法请参见[activation](../features/core_layers.md#get_activation_layer)。

**函数原型**

```python
def get_activation_layer(act_type: str) -> nn.Module:
```

**参数说明**

|参数名|输入/输出|类型|说明|
|--|--|--|--|
|act_type|输入|str|激活函数的名称。|

**返回值说明**

返回激活函数。
