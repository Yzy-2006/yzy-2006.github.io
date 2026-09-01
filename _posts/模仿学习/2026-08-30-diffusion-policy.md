---
title: 模仿学习—扩散策略(Diffusion Policy)
description: 扩散策略学习笔记
author: 阎梓瑜
date: 2026-08-30 12:00:00 +0800
categories: [模仿学习, Diffusion Policy]
tags: [模仿学习，扩散策略]
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

>实学习的是当前这个 noisy action $A_k$，在 observation $o$ 下，应该往哪个方向去噪，才能更接近真实动作数据的高概率区域。
{: .prompt-info}

## 七、Score Function

### Score Function的概念

假设我们有一个概率模型：

$$
p_\theta(x)
$$

其中：

- $x$：观测数据
- $\theta$：模型参数
- $p_\theta(x)$：参数为 $\theta$ 时，观察到 $x$ 的概率密度/概率

统计学中的 **score function** 定义为：

$$
s(\theta; x) = \nabla_\theta \log p_\theta(x)
$$

也就是说：

> **score function 是 log-likelihood 对模型参数 $\theta$ 的梯度。**

一维参数时就是：

$$
s(\theta; x)
=
\frac{\partial}{\partial \theta}
\log p_\theta(x)
$$

### 高斯分布的Score Function

假设：

$$
X \sim \mathcal{N}(\mu, \sigma^2)
$$

先假设 $\sigma^2$ 已知，只需要估计 $\mu$。

概率密度：

$$
p_\mu(x)
=
\frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(
-\frac{(x-\mu)^2}{2\sigma^2}
\right)
$$

取 log：

$$
\log p_\mu(x)
=
-\frac{1}{2}\log(2\pi\sigma^2)
-
\frac{(x-\mu)^2}{2\sigma^2}
$$

对 $\mu$ 求导：

$$
s(\mu;x)
=
\frac{\partial}{\partial \mu}
\log p_\mu(x)
$$

得到：

$$
\boxed{
s(\mu;x)
=
\frac{x-\mu}{\sigma^2}
}
$$

### 与MLE的关系

可以将MLE理解为：

>找到一个参数，使得所有样本给出的“参数移动建议”加起来正好为零

### 重要性质:期望为0

这是统计学里一个特别重要的公式：

$$
\mathbb{E}_{X\sim p_\theta}
\left[
\nabla_\theta \log p_\theta(X)
\right]
=0
$$

为什么？

因为：

$$
\nabla_\theta \log p_\theta(x)
=
\frac{\nabla_\theta p_\theta(x)}
{p_\theta(x)}
$$

所以：

$$
\begin{aligned}
\mathbb{E}[s(\theta;X)]
&=
\int p_\theta(x)
\nabla_\theta \log p_\theta(x)\,dx
\\
&=
\int \nabla_\theta p_\theta(x)\,dx
\\
&=
\nabla_\theta
\int p_\theta(x)\,dx
\end{aligned}
$$

但概率密度积分等于 1：

$$
\int p_\theta(x)\,dx = 1
$$

所以：

$$
\nabla_\theta 1 = 0
$$

因此：

$$
\boxed{
\mathbb{E}[s] = 0
}
$$

### 机器学习中的 Score Function

到了 score matching / diffusion model 中，经常会看到：

$$
s(x) = \nabla_x \log p(x)
$$

注意！

这里不是：

$$
\nabla_\theta \log p_\theta(x)
$$

而是：

$$
\nabla_x \log p(x)
$$

也就是说：

> 对 **数据 $x$** 求梯度，而不是对模型参数求梯度。

这是 diffusion model 中通常所说的 score function。

这两个一定要区分：

| 场景 | Score |
|---|---|
| 经典统计学 | $\nabla_\theta \log p_\theta(x)$ |
| Score matching / diffusion | $\nabla_x \log p(x)$ |

数学结构一样：

$$
\nabla \log p
$$

但梯度对象不同

### Score和Energy的关系

Energy-based model 通常写成：

$$
p(x)=\frac{1}{Z}e^{-E(x)}
$$

取 log：

$$
\log p(x)=-E(x)-\log Z
$$

因此：

$$
\nabla_x \log p(x)=-\nabla_x E(x)
$$

所以：

$$
s(x)=-\nabla_x E(x)
$$

也就是说 score 相当于：

> energy landscape 中指向下降最快方向的“力”。

如果把 energy 想成山地高度：

- 高 energy = 低概率；
- 低 energy = 高概率。

那么：

$$
-\nabla E(x)
$$

会把粒子推向 energy 更低的区域，也就是：

$$
p(x)
$$

更高的区域。

>这里对$p(x)$取对数再求导就可以消掉$Z$,就不需要对Energy进行全局积分再进行归一化
{: .prompt-tip}

###  Score 为什么能用来生成数据

这是 diffusion model 的关键思想。

假设我们已经知道：

$$
s(x)=\nabla_x \log p(x)
$$

那么就知道在整个空间中：

> “哪里是数据密集区？”

比如真实图片分布集中在某个复杂的 manifold 附近。

随机噪声一开始可能在任意地方。

如果我们知道 score：

$$
\nabla_x \log p(x)
$$

就可以不断按照这个方向移动：

$$
x_{k+1}
=
x_k
+
\epsilon \nabla_x \log p(x_k)
+
\text{noise}
$$

这就是 Langevin dynamics 的核心形式：

$$
x_{k+1}
=
x_k
+
\frac{\epsilon}{2}s(x_k)
+
\sqrt{\epsilon}z_k
$$

>可以类比一个粒子受到一个确定力的作用的同时在做无规则的热运动
{: .prompt-info}

其中：

$$
z_k \sim \mathcal{N}(0,I)
$$

score 把样本推向高概率区域，而随机噪声提供扩散；在合适条件下，两者共同使目标分布 $p(x)$ 成为 Langevin dynamics 的平稳分布。
