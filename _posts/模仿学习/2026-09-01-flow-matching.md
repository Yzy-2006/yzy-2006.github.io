---
title: 模仿学习—流匹配(Flow Matching)
description: 流匹配学习笔记
author: 阎梓瑜
date: 2026-09-01 12:00:00 +0800
categories: [模仿学习, 流匹配]
tags: [模仿学习，流匹配]
pin: false
math: true
mermaid: true
---

## 一、核心思想

不是让策略网络直接回答“现在应该做什么动作”，而是让它学习一个速度场（vector field），把一个简单的随机噪声分布逐渐“流动”成专家示范中的动作分布。

生成过程就变成一个 ODE(常微分方程)：

$$
\frac{dx_t}{dt} = v_\theta(x_t,t)
$$

初始化：

$$
x_0 \sim \mathcal{N}(0,I),
$$

然后从 $t=0$ 积分到 $t=1$：

$$
x_1 = x_0 + \int_0^1 v_\theta(x_t,t)\,dt.
$$

最后 $x_1$ 就应该服从数据分布

## 二、Conditional Flow Matching（CFM，条件流匹配）

我们有一个真实数据：

$$
x_1 \sim p_{\text{data}}.
$$

然后采一个噪声：

$$
x_0 \sim \mathcal{N}(0,I).
$$

现在人为规定它们之间怎么移动。

最简单的：

$$
x_t = (1-t)x_0 + tx_1
$$

它就是一条直线。

当 $t=0$：

$$
x_t=x_0.
$$

当 $t=1$：

$$
x_t=x_1.
$$

那么求导：

$$
\frac{dx_t}{dt}=x_1-x_0.
$$

所以这个 pair 对应的 target velocity 非常简单：

$$
u_t=x_1-x_0
$$

于是训练就变成：

$$
L_{\mathrm{CFM}}
=
\mathbb{E}
\left[
\left\|
v_\theta(x_t,t)-(x_1-x_0)
\right\|^2
\right].
$$

## 三、更一般的Flow Matching

实际上不一定要：

$$
x_t=(1-t)x_0+tx_1.
$$

更一般地可以写：

$$
x_t=\alpha(t)x_1+\sigma(t)x_0
$$

于是速度就是：

$$
\dot{x}_t
=
\dot{\alpha}(t)x_1+\dot{\sigma}(t)x_0
$$

所以 target：

$$
u_t
=
\dot{\alpha}(t)x_1+\dot{\sigma}(t)x_0.
$$

因此训练：

$$
L
=
\mathbb{E}
\left[
\left\|
v_\theta(x_t,t)
-
\left(
\dot{\alpha}(t)x_1+\dot{\sigma}(t)x_0
\right)
\right\|^2
\right].
$$

## 四、和Diffusion Policy的区别

### Diffusion Policy的训练过程

对于一个 demo：

$$
(O,A)
$$

先随机选 diffusion timestep $k$。

给 action sequence 加噪：

$$
A^k
=
\sqrt{\bar{\alpha}_k}A
+
\sqrt{1-\bar{\alpha}_k}\epsilon.
$$

网络输入：

$$
(O,A^k,k).
$$

输出：

$$
\epsilon_\theta(O,A^k,k).
$$

训练：

$$
L
=
\left\|
\epsilon
-
\epsilon_\theta(O,A^k,k)
\right\|^2.
$$

### Diffusion Policy的推理过程

首先生成随机 action chunk：

$$
A^K\sim\mathcal{N}(0,I).
$$

然后：

$$
A^K
\rightarrow
A^{K-1}
\rightarrow
\cdots
\rightarrow
A^0.
$$

每一步都调用一次网络：

$$
\epsilon_\theta(O,A^k,k).
$$

最终：

$$
A^0
=
[a_t,a_{t+1},\ldots,a_{t+H}].
$$

### Flow Matching Policy的训练过程

目标仍然是：

$$
p(A\mid O).
$$

拿一条 expert action chunk：

$$
A_1
\sim
p_{\mathrm{demo}}(A\mid O)
$$

和一份 Gaussian noise：

$$
A_0
\sim
\mathcal{N}(0,I).
$$

随机：

$$
t\sim U(0,1).
$$

最简单的 interpolant：

$$
A_t
=
(1-t)A_0+tA_1
$$

target velocity：

$$
u
=
A_1-A_0.
$$

网络：

$$
v_\theta(A_t,t,O).
$$

loss：

$$
L_{\mathrm{FM}}
=
\left\|
v_\theta(A_t,t,O)
-
(A_1-A_0)
\right\|^2.
$$

### Flow Matching Policy 推理

首先：

$$
A(0)
\sim
\mathcal{N}(0,I).
$$

然后解：

$$
\frac{dA(t)}{dt}
=
v_\theta(A(t),t,O)
$$

从：

$$
t=0
$$

积分到：

$$
t=1.
$$

最简单的 Euler：

$$
A_{i+1}
=
A_i
+
\Delta t\,
v_\theta(A_i,t_i,O).
$$

例如 4 步：

$$
A_0
\rightarrow
A_{0.25}
\rightarrow
A_{0.5}
\rightarrow
A_{0.75}
\rightarrow
A_1.
$$

|                     | Diffusion Policy                   | Flow Matching Policy                 |
| ------------------- | ---------------------------------- | ------------------------------------ |
| 最终目标                | $p(A\mid O)$                     | $p(A\mid O)$                       |
| 初始状态                | Gaussian noise                     | Gaussian noise                       |
| 网络学习                | noise / score                      | velocity                             |
| 典型输出                | $\epsilon_\theta(A_t,t,O)$       | $v_\theta(A_t,t,O)$                |
| Training target     | 加进去的噪声 $\epsilon$                | trajectory velocity $\dot A_t$     |
| 生成观点                | denoise                            | transport / flow                     |
| 连续时间观点              | reverse SDE / probability-flow ODE | ODE                                  |
| 随机性                 | 初始噪声；DDPM sampling 还可有过程噪声         | 通常主要来自初始噪声                           |
| 推理                  | iterative denoising                | numerical ODE integration            |
| trajectory path     | diffusion/noise schedule 决定        | probability path 可自由选择               |
| multimodality       | 可以                                 | 可以                                   |
| action chunking     | 可以                                 | 可以                                   |
| receding horizon    | 可以                                 | 可以                                   |
| visual conditioning | 可以                                 | 可以                                   |
| 典型优势                | 成熟、鲁棒、训练稳定                         | vector target 简单、路径设计灵活，并经常有潜力减少 NFE |

### Score 和 Velocity 的区别

Diffusion 中的 score：

$$
s_t(x)=\nabla_x\log p_t(x)
$$

> 对状态变量 $x$ 求梯度，描述固定时刻 $t$ 下概率密度的空间几何结构，即概率密度增长最快的方向。

Flow Matching 中的 velocity field：

$$
v_t(x_t)=\frac{dx_t}{dt}
$$

> 描述样本随着生成时间 $t$ 增大时，在状态空间中应该如何运动。

二者不是同一个量：

$$
s_t(x)\neq v_t(x).
$$

它们通过概率分布的动力学联系起来。对于 velocity field $v_t$，其诱导的概率分布满足连续性方程：

$$
\frac{\partial p_t(x)}{\partial t}
+
\nabla\cdot\left(p_t(x)v_t(x)\right)
=
0.
$$

其中：

$$
\underbrace{
\frac{\partial p_t}{\partial t}
}_{\text{本地概率密度变化}}
+
\underbrace{
\nabla\cdot(p_t v_t)
}_{\text{概率的净流出}}
=
0.
$$

对于一个已知的 forward diffusion SDE：

$$
dx=f(x,t)\,dt+g(t)\,dW_t,
$$

如果知道 score：

$$
s_t(x)=\nabla_x\log p_t(x),
$$

则可以构造对应的 probability-flow ODE velocity：

$$
v_t(x)
=
f(x,t)
-
\frac{1}{2}g(t)^2s_t(x).
$$

因此，score 本身不是 velocity。

更准确地说：

> Diffusion 学习 noise/score，并结合已知的 diffusion dynamics 得到反向生成动力学；在 probability-flow ODE 视角下，这个动力学可以等价表示为一个 velocity field。

Flow Matching 则直接学习这个 velocity field。
