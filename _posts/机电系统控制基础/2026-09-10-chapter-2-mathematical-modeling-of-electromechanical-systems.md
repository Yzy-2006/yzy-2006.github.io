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

## 三、拉氏变换

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

#### 积分性质(零初始状态下)

$$
\mathcal{L}\left[\int_{0}^{t} x(t)\,dt\right]
= \frac{1}{s}X(s)
$$

#### 时域延时定理

$$
\mathcal{L}\left[x(t-\tau)\cdot 1(t-\tau)\right]
= e^{-\tau s}X(s)
$$

#### 复域延时定理

$$
\mathcal{L}^{-1}F(s+a)=e^{-at}f(t)
$$

#### 终值定理

$$
\lim_{t\to\infty}x(t)
=
\lim_{s\to 0}sX(s)
$$

### 4.拉氏反变换

**思路：** 采用部分分式展开法求拉氏反变换

$$
X(s)=
\frac{
b_0s^m+b_1s^{m-1}+\cdots+b_{m-1}s+b_m
}{
s^n+a_1s^{n-1}+\cdots+a_{n-1}s+a_n
}
\qquad (m\le n)
$$

将其进行部分分式展开：

$$
X(s)=X_1(s)+X_2(s)+\cdots+X_n(s)
$$

因此，其拉氏反变换为：

$$
x(t)
=
L^{-1}\left[X_1(s)\right]
+
L^{-1}\left[X_2(s)\right]
+\cdots+
L^{-1}\left[X_n(s)\right]
$$

---

#### 只含不同单极点的

$$
X(s)
=
\frac{
b_0s^m+b_1s^{m-1}+\cdots+b_{m-1}s+b_m
}{
(s+p_1)(s+p_2)\cdots(s+p_n)
}
$$

将其进行部分分式展开：

$$
X(s)
=
\frac{A_1}{s+p_1}
+
\frac{A_2}{s+p_2}
+
\cdots
+
\frac{A_k}{s+p_k}
+
\cdots
+
\frac{A_n}{s+p_n}
$$

用留数公式求待定系数

$$
A_k
=
\left.
\lim_{s\to -p_k}
\left[
X(s)(s+p_k)
\right]
\right.
$$

用该公式取反变换

$$
\mathcal{L}^{-1}
\left[
\frac{A_i}{s+p_i}
\right]
=
A_i e^{-p_i t}
$$

---

#### 含共轭复数极点的情况

$$
X(s)
=
\frac{K_1s+K_2}{s^2+bs+c}
+
\frac{K_3}{s+p_2}
+\cdots+
\frac{K_n}{s+p_n}
$$

其中，第一项包含一对共轭复数极点：

$$
s_{1,2}=-\sigma\pm j\beta
$$

用留数公式求待定系数 $K_1$ 和 $K_2$

$$
K_1s+K_2
=
\left.
X(s)\left(s^2+bs+c\right)
\right|_{s=-\sigma+j\beta}
$$


将二次项整理为标准形式：

$$
\mathcal{L}^{-1}
\left[
\frac{K_1s+K_2}{s^2+bs+c}
\right]
=
\mathcal{L}^{-1}
\left[
\frac{a_1(s+\sigma)}
{(s+\sigma)^2+\beta^2}
+
\frac{a_2\beta}
{(s+\sigma)^2+\beta^2}
\right]
$$

因此：

$$
\mathcal{L}^{-1}
\left[
\frac{K_1s+K_2}{s^2+bs+c}
\right]
=
a_1e^{-\sigma t}\cos\beta t
+
a_2e^{-\sigma t}\sin\beta t
$$

---

#### 含重极点的情况

若 $s=-p_1$ 为 $r$ 重极点，则应展开为 $r$ 个分式：

$$
X(s)
=
\frac{K_{11}}{(s+p_1)^r}
+
\frac{K_{12}}{(s+p_1)^{r-1}}
+\cdots+
\frac{K_{1r}}{s+p_1}
+
\frac{K_2}{s+p_2}
+\cdots+
\frac{K_n}{s+p_n}
$$

求待定系数

$$
K_{11}
=
\lim_{s\to -p_1}
X(s)(s+p_1)^r
$$

$$
K_{12}
=
\frac{1}{1!}
\lim_{s\to -p_1}
\frac{d}{ds}
\left[
X(s)(s+p_1)^r
\right]
$$

$$
K_{13}
=
\frac{1}{2!}
\lim_{s\to -p_1}
\frac{d^2}{ds^2}
\left[
X(s)(s+p_1)^r
\right]
$$

一般地：

$$
K_{1r}
=
\frac{1}{(r-1)!}
\lim_{s\to -p_1}
\frac{d^{r-1}}{ds^{r-1}}
\left[
X(s)(s+p_1)^r
\right]
$$

## 四、系统的传递函数

### 1.传递函数的定义及特点

**传递函数**：线性定常系统在**零初始条件**下，输出量的 Laplace 变换与输入量的 Laplace 变换之比。

**零初始条件:** 当 $t<0$ 时，输入量及其各阶导数均为 $0$。


系统的微分方程为：

$$
a_n\frac{d^n}{dt^n}x_o(t)
+a_{n-1}\frac{d^{n-1}}{dt^{n-1}}x_o(t)
+\cdots
+a_1\frac{d}{dt}x_o(t)
+a_0x_o(t)

=
b_m\frac{d^m}{dt^m}x_i(t)
+b_{m-1}\frac{d^{m-1}}{dt^{m-1}}x_i(t)
+\cdots
+b_1\frac{d}{dt}x_i(t)
+b_0x_i(t),
\qquad (n\ge m)
$$

对微分方程进行 Laplace 变换，则有

$$
\left(
a_ns^n+a_{n-1}s^{n-1}+\cdots+a_1s+a_0
\right)X_o(s)

=
\left(
b_ms^m+b_{m-1}s^{m-1}+\cdots+b_1s+b_0
\right)X_i(s)
$$

根据传递函数定义，则有 $G(s)$ 如下

$$
G(s)
=
\frac{X_o(s)}{X_i(s)}
=
\frac{
b_ms^m+b_{m-1}s^{m-1}+\cdots+b_1s+b_0
}{
a_ns^n+a_{n-1}s^{n-1}+\cdots+a_1s+a_0
}
$$

#### 传递函数的特点

- 传递函数是**复数域**中的系统数学模型，其参数仅取决于**系统本身的结构及参数**，与系统的输入形式无关；

- 传递函数的**分母**反映了系统本身与外界无关的**固有特性**，分子反映了系统本身与外界之间的关系；

- 传递函数表征了系统内在的**固有动态特性**；

- 传递函数分母中 $s$ 的阶次 $n$ **不小于**分子中 $s$ 的阶次 $m$；

- 传递函数可以有量纲，也可以无量纲；

- 不同的物理系统可以具有相同的传递函数；

- 同一系统选取不同物理量作为输入、输出，传递函数可不同；

- 传递函数的概念，只适用**初始状态为零的线性定常系统**。

### 2.传递函数的特征方程、零点、极点和放大系数

$$
G(s)
=
\frac{X_o(s)}{X_i(s)}
=
\frac{
b_m s^m+b_{m-1}s^{m-1}+\cdots+b_1s+b_0
}{
a_n s^n+a_{n-1}s^{n-1}+\cdots+a_1s+a_0
}
=
\frac{M(s)}{N(s)}
$$

式中：

$$
M(s)
=
b_m s^m+b_{m-1}s^{m-1}+\cdots+b_1s+b_0
$$

$$
N(s)
=
a_n s^n+a_{n-1}s^{n-1}+\cdots+a_1s+a_0
$$

其中：

$$
N(s)=0
$$

称为系统的**特征方程**，其根称为系统的**特征根**。

$$
G(s)
=
\frac{X_o(s)}{X_i(s)}
=
\frac{M(s)}{N(s)}
=
\frac{
K(s-z_1)(s-z_2)\cdots(s-z_m)
}{
(s-p_1)(s-p_2)\cdots(s-p_n)
}
\qquad (K\text{ 为常数})
$$

式中，

$$
M(s)
=
K(s-z_1)(s-z_2)\cdots(s-z_m)
$$

方程

$$
M(s)=0
$$

的根

$$
s=z_i,\qquad i=1,2,\ldots,m
$$

称为传递函数的**零点**。

> 零点影响瞬态响应曲线的形状，不影响系统稳定性。
{: .prompt-info}

---

$$
N(s)
=
(s-p_1)(s-p_2)\cdots(s-p_n)
$$

方程

$$
N(s)=0
$$

的根

$$
s=p_j,\qquad j=1,2,\ldots,n
$$

称为传递函数的**极点**。

**极点就是系统的特征根。**

> 极点决定系统瞬态响应曲线的收敛性，即系统的稳定性。
{: .prompt-info}

### 3.关于传递函数的几点说明

- 通常只**适用于线性定常系统**；

- 传递函数是 $s$ 的复变函数，**完全取决于系统结构与参数**；

- 传递函数是在**零初始条件下定义**的；

- 传递函数只能表示系统**单输入与单输出的关系**，无法描述系统内部中间变量的变化情况。