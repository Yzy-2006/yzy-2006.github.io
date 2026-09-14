---
title: 第2章 机电系统的数学模型
description: 机电系统控制基础第2章笔记
author: 阎梓瑜
date: 2026-09-10 18:30:00 +0800
categories: [机电系统控制基础]
tags: [机电系统控制基础]
pin: false
math: true
mermaid: true
---

## 一、控制系统数学模型的概念

### 1. 数学模型的定义

**数学模型:** 描述系统输入、输出量以及内部各变量之间关系的数学表达式，对于同一系统，可以建立多种形式的数学模型。如微分方程、传递函数、频率特性及状态空间模型等。

- 数学模型
  - 微分方程
    - 时域
  - 传递函数
    - 复数域
  - 频率特性
    - Nyquist 图
    - Bode 图
    - 频域

### 2. 如何建立数学模型(建模方法)

- **解析法 / 分析法**：根据系统和元件所遵循的有关定律来推导出数学表达式。
  - 例如：牛顿运动定律、欧姆定律、基尔霍夫定律、虎克定律、流体力学等。

- **实验法 / 系统辨识法**：人为地对系统施加某种测试信号，记录其输出响应，通过数据整理，拟合出比较接近实际系统的数学表达式。

## 二、系统的微分方程

### 1. 线性系统的微分方程

**微分方程：** 在时域中描述系统（或元件）动态特性的数学模型

- 系统
  - 线性系统
    - 线性定常系统
    - 线性时变系统
  - 非线性系统
  
对线性定常系统，其微分方程的一般形式如下：

$$
a_n \frac{d^n}{dt^n}c(t)
+a_{n-1}\frac{d^{n-1}}{dt^{n-1}}c(t)
+\cdots
+a_1\frac{d}{dt}c(t)
+a_0c(t)
$$

$$
=
b_m\frac{d^m}{dt^m}r(t)
+b_{m-1}\frac{d^{m-1}}{dt^{m-1}}r(t)
+\cdots
+b_1\frac{d}{dt}r(t)
+b_0r(t)
$$

式中：

- $c(t)$ 为系统输出量；
- $r(t)$ 为系统输入量；
- $a_0,a_1,\ldots,a_n$ 及 $b_0,b_1,\ldots,b_m$ 均为由系统结构与参数所决定的实常数。

### 2. 机械系统的微分方程

#### 平动机械系统的微分方程

$$
M\frac{d^2y(t)}{dt^2}
=
f(t)
-
B\frac{dy(t)}{dt}
-
Ky(t)
$$

$$
M\frac{d^2y(t)}{dt^2}
+
B\frac{dy(t)}{dt}
+
Ky(t)
=
f(t)
$$

>这里重力一般包含在外力里
{: .prompt-info}

#### 转动机械系统的微分方程

$$
T
=
J\frac{d^2\theta}{dt^2}
+
B\frac{d\theta}{dt}
+
K\theta
$$

#### 机械系统中基本物理量的折算

- 丝杠螺母传动机构

  $$
  J
  =
  m\left(\frac{L}{2\pi}\right)^2
  $$

- 齿轮齿条 / 同步带传动机构

  $$
  J
  =
  mr^2
  $$

- 多级齿轮传动
  - 传动比

    $$
    i
    =
    \frac{n_1}{n_2}
    =
    \frac{\theta_1}{\theta_2}
    =
    \frac{\omega_1}{\omega_2}
    =
    \frac{r_2}{r_1}
    =
    \frac{z_2}{z_1}
    =
    \frac{T_2}{T_1}
    $$

  - 等效转动惯量

  $$
  J
  =
  J_1
  +
  \frac{J_2}{i_1^2}
  +
  \frac{J_3}{i_1^2 i_2^2}
  +
  \cdots
  $$

  - 等效阻尼系数

    $$
    B
    =
    B_1
    +
    \frac{B_2}{i_1^2}
    +
    \frac{B_3}{i_1^2 i_2^2}
    +
    \cdots
    $$

  - 等效扭转刚度

    $$
    \frac{1}{K}
    =
    \frac{1}{K_1}
    +
    \frac{i_1^2}{K_2}
    +
    \frac{i_1^2 i_2^2}{K_3}
    +
    \cdots
    $$

>其实就是在用能量守恒进行推导
{: .prompt-info}

### 3. 电气系统的微分方程

#### 电阻

$$
u(t)=R\,i(t)
$$

#### 电容

$$
u(t)=\frac{1}{C}\int i(t)\,dt
$$

电容：电压 = 电流的积分，电容值的倒数是常系数。

#### 电感

$$
u(t)=L\frac{di(t)}{dt}
$$

## 三、系统的传递函数

### 1. 拉氏变换的定义

对于函数 $x(t)$，如果满足下列条件：

1. 当 $t<0$ 时，

   $$
   x(t)=0
   $$

   当 $t>0$ 时，$x(t)$ 有有限个间断点；

2. 积分

   $$
   \int_{0}^{\infty} x(t)e^{-st}\,dt
   $$

   存在，其中

   $$
   s=\sigma+j\omega
   $$

   为复变量。

则如下积分变换称为 **Laplace 变换（拉氏变换）**：

$$
\boxed{
X(s)=\mathcal{L}[x(t)]
=\int_{0}^{\infty}x(t)e^{-st}\,dt
}
$$

其中：

- $x(t)$：原函数
- $X(s)$：象函数
- $s=\sigma+j\omega$：复变量

### 2. 典型拉氏变换

| 原函数 $x(t)$          | Laplace 变换 $X(s)$                             |
| ---------------------- | ----------------------------------------------- |
| $\delta(t)$            | $1$                                             |
| $u(t)$                 | $\displaystyle \frac{1}{s}$                     |
| $t^n$                  | $\displaystyle \frac{n!}{s^{n+1}}$              |
| $e^{-at}$              | $\displaystyle \frac{1}{s+a}$                   |
| $\sin \omega t$        | $\displaystyle \frac{\omega}{s^2+\omega^2}$     |
| $\cos \omega t$        | $\displaystyle \frac{s}{s^2+\omega^2}$          |
| $t^n e^{-at}$          | $\displaystyle \frac{n!}{(s+a)^{n+1}}$          |
| $e^{-at}\sin \omega t$ | $\displaystyle \frac{\omega}{(s+a)^2+\omega^2}$ |
| $e^{-at}\cos \omega t$ | $\displaystyle \frac{s+a}{(s+a)^2+\omega^2}$    |

> 原函数乘以$e^{-at}$，象函数的$s$替换为$s+a$
{: .prompt-info}

### 3. 拉氏变换的基本性质和定理

#### 线性性质

$$
\mathcal{L}\left[a x_1(t) \pm b x_2(t)\right]= aX_1(s)\pm bX_2(s)
$$

#### 微分性质

若系统处于**零初始条件**下，则有：`

$$
\boxed{
\mathcal{L}\left[\frac{d^n x(t)}{dt^n}\right]
= s^nX(s)
}
$$