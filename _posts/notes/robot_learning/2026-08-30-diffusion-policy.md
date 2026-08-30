---
title: 模仿学习—扩散策略(Diffusion Policy)
description: 扩散策略学习笔记
author: 阎梓瑜
date: 2026-08-30 12:00:00 +0800
categories: [笔记,机器人学习]
tags: [模仿学习，ACT]
pin: false
math: true
mermaid: true
---

## 一、核心思想

先随机生成一个动作序列，然后经过反复去噪，得到合理的动作序列

## 二、Forward Diffusion：正向扩散

通常先定义一个噪声强度：

$$
\beta_k
$$

然后定义：

$$
\alpha_k = 1 - \beta_k
$$

再定义累计乘积：

$$
\bar{\alpha}_k = \prod_{i=1}^{k} \alpha_i
$$
  
数学上可以写成：

$$
A_k = \sqrt{\bar{\alpha}_k} A_0 + \sqrt{1-\bar{\alpha}_k}\epsilon
$$

其中：

$$
\epsilon \sim \mathcal{N}(0, I)
$$

这里几个量分别是：

- $A_0$：专家真实 Action Sequence
- $A_k$：加噪到第 $k$ 个 diffusion step 后的动作
- $\epsilon$：随机 Gaussian noise
- $k$：扩散时间步
- $\beta_k$：这一 diffusion step 加多少噪声
- $\alpha_k$：这一步保留多少信号
- $\bar{\alpha}_k$：控制还保留多少原始信号

之后，我们将被污染过的动作序列作为输入来对网络进行训练

## 三、网络的结构

网络可以写成：

$$
\epsilon_\theta(A_k, k, o)
$$

输入三个主要东西：

- $A_k$：第 $k$ 个扩散时间步的**带噪动作序列**。它的形状通常为“预测时域长度 $\times$ 动作维度”，例如未来若干步机械臂的位姿、夹爪开合等动作；训练时由专家动作 $A_0$ 加噪得到。
- $k$：当前的**扩散时间步**。网络会先将它编码为时间嵌入（time embedding），以便知道当前动作序列中还含有多少噪声、应采用多强的去噪方式。
- $o$：策略的**条件观测**，即机器人当前所看到和感知到的信息，例如相机图像、关节角/末端位姿、夹爪状态，以及最近几帧观测。它用于让生成的动作与当前任务状态相匹配。

输出：

- $\hat{\epsilon}$：网络预测的**噪声序列**，形状与 $A_k$ 相同。训练时将它与实际加入的噪声 $\epsilon$ 比较并最小化误差；推理时利用该预测从 $A_k$ 去噪得到 $A_{k-1}$，重复直到得到最终动作序列 $A_0$。

损失函数:

$$
\mathcal{L} = \left\| \epsilon - \epsilon_\theta(O_t, A_t^k, k) \right\|^2
$$

## 四、三个很重要的 horizon

**Observation Horizon:** 模型看多少历史 observation

**Prediction Horizon：** 一次生成多少未来 action

**Execution Horizon：** 真正执行多少 action 后重新规划

## 五、反向扩散

反向扩散的目标是从当前 noisy action $A_k$ 逐步恢复更干净的 $A_{k-1}$。

理论上，如果已知原始动作 $A_0$，则：

$$
q(A_{k-1}\mid A_k,A_0)
=
\mathcal{N}(\tilde{\mu}_k,\tilde{\beta}_k I)
$$

其中均值：

$$
\tilde{\mu}_k
=
\frac{\sqrt{\bar{\alpha}_{k-1}}\beta_k}{1-\bar{\alpha}_k}A_0
+
\frac{\sqrt{\alpha_k}(1-\bar{\alpha}_{k-1})}{1-\bar{\alpha}_k}A_k
$$

说明 $A_{k-1}$ 同时由当前 noisy action $A_k$ 和原始 clean action $A_0$ 决定。

但实际推理时 $A_0$ 未知，因此利用网络预测噪声：

$$
\hat{\epsilon}
=
\epsilon_\theta(A_k,k,o)
$$

根据正向扩散公式：

$$
A_k
=
\sqrt{\bar{\alpha}_k}A_0
+
\sqrt{1-\bar{\alpha}_k}\epsilon
$$

可估计：

$$
\hat{A}_0
=
\frac{
A_k-\sqrt{1-\bar{\alpha}_k}\hat{\epsilon}
}{
\sqrt{\bar{\alpha}_k}
}
$$

因此整个反向过程可以理解为：

$$
\boxed{
A_k
\rightarrow
\text{预测噪声}
\rightarrow
\text{估计 }A_0
\rightarrow
A_{k-1}
}
$$

重复这一过程：

$$
A_K
\rightarrow
A_{K-1}
\rightarrow
\cdots
\rightarrow
A_0
$$

最终从随机噪声中生成干净的动作序列。

## 六、为什么学到的是分布

Diffusion Policy 建模的是条件动作分布：

$$
p_\theta(A_0\mid o)
$$

其反向生成过程为：

$$
A_K \rightarrow A_{K-1} \rightarrow \cdots \rightarrow A_0
$$

其中初始噪声：

$$
A_K \sim \mathcal N(0,I)
$$

每一步去噪对应一个条件分布：

$$
p_\theta(A_{k-1}\mid A_k,o)
$$

因此最终动作分布可以写成：

$$
p_\theta(A_0\mid o)
=
\int
p(A_K)
\prod_{k=1}^{K}
p_\theta(A_{k-1}\mid A_k,o)
\,dA_{1:K}
$$

其中：

- $p(A_K)$：初始 Gaussian noise 分布
- $p_\theta(A_{k-1}\mid A_k,o)$：第 $k$ 步反向去噪分布
- $\prod$：整条反向去噪链
- $\int dA_{1:K}$：将所有中间变量边缘化

直观上：

$$
\boxed{
\text{同一个 }o
+
\text{不同随机噪声}
\rightarrow
\text{不同但合理的动作序列}
}
$$

因此 Diffusion Policy 学习的是：

$$
\boxed{
p(A\mid o)
}
$$

而不是普通回归中的单一动作：

$$
\boxed{
o\rightarrow A
}
$$

>实际学习的是当前这个 noisy action $A_k$，在 observation $o$ 下，应该往哪个方向去噪，才能更接近真实动作数据的高概率区域。
{: .prompt-info}