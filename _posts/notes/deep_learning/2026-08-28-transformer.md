---
title: Transformer
description: 伟大的Transformer
author: 阎梓瑜
date: 2026-08-28 16:00:00 +0800
categories: [笔记,深度学习]
tags: [Ubuntu,Linux]
pin: false
math: true
mermaid: true
---

**核心思想：** 序列中的每个元素都能直接关注序列中的其他元素，从而建立全局依赖关系

### 一、自注意力机制(Self-Attention)

每个token先被表示为一个向量，然后对每一个词，计算它应该关注其他词多少

### 二、Q、K、V的概念

**Query：** 我想找什么信息？

**Key：** 我这里有什么信息？

**Value：** 真正要取走的信息是什么？

$$
Q = XW_Q
$$

$$
K = XW_K
$$

$$
V = XW_V
$$

### 三、Attention的公式

$$
\operatorname{Attention}(Q,K,V)
=
\operatorname{softmax}
\left(
\frac{QK^{T}}{\sqrt{d_k}}
\right)V
$$

先计算$Q$和$K$的相似度，再进行一下数值稳定性的处理，最够对$V$进行一下加权平均

### 四、多头注意力(Multi-Head Attention)

```
             输入
              │
     ┌────────┼────────┐
     ▼        ▼        ▼
   Head1    Head2    Head3 ... Head8
     │        │        │
     └────────┼────────┘
              ▼
            拼接
              ▼
          Linear
```

使用不同的head可以学习不同的关系

### 五、FFN

一个全连接神经网络，用于处理每个token自己的信息

### 六、残差连接

```
x
↓
Attention
↓
F(x)
```

然后会输出

$$
x+F(x)
$$

这样做可以保留一部分旧信息，让深层网络更加容易训练

### 七、Transformer的完整结构

```
              Input Tokens
                   │
                   ↓
          Multi-Head Attention
                   │
              + Residual
                   │
              LayerNorm
                   │
                   ↓
           Feed Forward
                   │
              + Residual
                   │
              LayerNorm
                   │
                   ↓
             Output Tokens
```