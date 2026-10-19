---
title: 机电系统控制基础第3章 系统的时域分析法
description: 机电系统控制基础第3章笔记
author: 阎梓瑜
date: 2026-09-28 10:30:00 +0800
categories: [机电系统控制基础]
tags: [机电系统控制基础]
pin: false
math: true
mermaid: true
---

## 一、时域响应及典型输入信号

### 1.时域响应

- **瞬态响应**：在系统受到外加作用激励后，从初始状态到最终状态的响应过程。在工程上只讨论输入作用加入一段时间里的瞬态过程。

- **稳态响应**：时间趋于无穷大时，系统的输出状态成为稳态响应。理论上，只有时间趋于无穷大时，系统才进入稳态过程。

### 2.典型输入信号


选取输入信号应当考虑以下几个方面：
  - 输入信号应当具有典型性，能够反映系统工作的大部分实际情况。
  - 输入信号的形式应当尽可能简单，便于分析处理。
  - 输入信号应能使系统在最恶劣的情况下工作。

---

#### 阶跃函数

其表达式为

$$
r(t)=
\begin{cases}
a, & t\ge 0 \\
0, & t<0
\end{cases}
$$

当 $a=1$ 时，称为**单位阶跃函数**，记作 $1(t)$，则有

$$
1(t)=
\begin{cases}
1, & t\ge 0 \\
0, & t<0
\end{cases}
$$

单位阶跃函数的拉氏变换为

$$
R(s)=\mathcal{L}[1(t)]=\frac{1}{s}
$$


#### 速度函数（斜坡函数）

其表达式为

$$
r(t)=
\begin{cases}
at, & t\ge 0 \\
0, & t<0
\end{cases}
$$

其中 $a$ 为常量。

当 $a=1$ 时，

$$
r(t)=t
$$

称为**单位速度函数**，其拉氏变换为

$$
R(s)=\mathcal{L}[t\cdot 1(t)]=\frac{1}{s^2}
$$


#### 加速度函数（抛物线函数）

其表达式为

$$
r(t)=
\begin{cases}
at^2, & t\ge 0 \\
0, & t<0
\end{cases}
$$

其中 $a$ 为常量。

当

$$
a=\frac{1}{2}
$$

时，称为**单位加速度函数**，其拉氏变换为

$$
R(s)
=
\mathcal{L}
\left[
\frac{1}{2}t^2\cdot 1(t)
\right]
=
\frac{1}{s^3}
$$


#### 脉冲函数

宽度为 $\Delta$ 的矩形脉冲可表示为

$$
r(t)=
\begin{cases}
\dfrac{1}{\Delta}, & 0<t<\Delta \\
0, & t<0,\ t>\Delta
\end{cases}
$$

当

$$
\Delta\to 0
$$

时，得到单位脉冲函数 $\delta(t)$。

其数学描述为

$$
\delta(t)=
\begin{cases}
\infty, & t=0 \\
0, & t\ne 0
\end{cases}
$$

并满足

$$
\int_{-\infty}^{+\infty}\delta(t)\,dt=1
$$

单位脉冲函数的拉氏变换为

$$
R(s)=\mathcal{L}[\delta(t)]=1
$$


#### 正弦函数

其表达式为

$$
r(t)=
\begin{cases}
a\sin\omega t, & t\ge 0 \\
0, & t<0
\end{cases}
$$

其拉氏变换为

$$
R(s)
=
\mathcal{L}
\left[
a\sin\omega t\cdot 1(t)
\right]
=
\frac{a\omega}{s^2+\omega^2}
$$

## 二、一阶系统的瞬态响应

**一阶系统:** 可用一阶微分方程描述的系统

$$
G(s)=\frac{X_o(s)}{X_i(s)}=\frac{K}{Ts+1}
$$

>为了便于分析，我们在下边分析是取$K=1$,称为单位增益的一阶系统
{: .prompt-info}

### 1.一阶系统的单位阶跃响应

输入为单位阶跃信号：

$$
x_i(t)=1(t)
$$

其拉氏变换为

$$
\mathcal{L}[1(t)]=\frac{1}{s}
$$

因此

$$
X_o(s)
=
\frac{1}{Ts+1}\cdot\frac{1}{s}
$$

对其进行拉氏反变换，可得输出响应

$$
x_o(t)
=
\mathcal{L}^{-1}[X_o(s)]
=
1-e^{-\frac{t}{T}},
\qquad t\geq0
$$

$T$ 称为时间常数，它影响到响应的快慢，因而是一阶系统的重要参数。

#### 时间常数 $T$ 的确定方法

1. 在响应曲线上，找到稳态值的 $63.2\%$ 对应的 $A$ 点，并向时间轴 $t$ 作垂线，与时间轴的交点值即为时间常数 $T$。

2. 由 $t=0$ 那一点 $O$（即原点）作响应曲线的切线，与稳态值交于 $A$ 点。由 $A$ 点向时间轴 $t$ 作垂线，与时间轴的交点值即为时间常数 $T$。

### 2.一阶系统的单位脉冲响应



当输入为单位脉冲信号时，

$$
X_i(s)=1
$$

因此

$$
X_o(s)=G(s)
$$

对于一阶系统

$$
G(s)=\frac{1}{Ts+1}
=
\frac{\frac{1}{T}}{s+\frac{1}{T}}
$$

对其进行拉氏反变换，得到输出响应

$$
x_o(t)
=
\mathcal{L}^{-1}[G(s)]
=
\mathcal{L}^{-1}
\left[
\frac{\frac{1}{T}}{s+\frac{1}{T}}
\right]
=
\frac{1}{T}e^{-\frac{t}{T}},
\qquad t\geq0
$$

> 响应有瞬态无稳态，主要原因是引起此响应的输入是**瞬态作用**。
{: .prompt-info}

### 3.单位斜坡响应

输入信号为

$$
x(t)=t
$$

其拉氏变换为

$$
X(s)=\frac{1}{s^2}
$$

对于一阶系统，

$$
Y(s)
=
\frac{1}{Ts+1}\cdot\frac{1}{s^2}
$$

对其进行部分分式展开：

$$
Y(s)
=
\frac{1}{s^2}
-
\frac{T}{s}
+
\frac{T^2}{Ts+1}
$$

进行拉氏反变换，得到系统的单位斜坡响应：

$$
y(t)
=
t-T+Te^{-\frac{t}{T}}
$$

偏差量为

$$
e(t)
=
x(t)-y(t)
=
T\left(1-e^{-\frac{t}{T}}\right)
$$

当

$$
t\rightarrow\infty
$$

时，

$$
e(\infty)=T
$$

即一阶系统在单位斜坡输入作用下存在稳态偏差，其稳态偏差等于时间常数 $T$

### 4.单位抛物线响应

输入信号为

$$
x(t)=\frac{1}{2}t^2
$$

其拉氏变换为

$$
X(s)=\frac{1}{s^3}
$$

对于一阶系统，

$$
Y(s)
=
\frac{1}{Ts+1}\cdot\frac{1}{s^3}
$$

进行部分分式展开：

$$
Y(s)
=
\frac{a_1}{s^3}
+
\frac{a_2}{s^2}
+
\frac{a_3}{s}
+
\frac{a_4}{Ts+1}
$$

其中

$$
a_1
=
\left.
\frac{1}{Ts+1}\cdot\frac{1}{s^3}\cdot s^3
\right|_{s=0}
=1
$$

$$
a_2
=
\left.
\frac{d}{ds}
\left(
\frac{1}{Ts+1}
\right)
\right|_{s=0}
=
\left.
\frac{-T}{(Ts+1)^2}
\right|_{s=0}
=-T
$$

$$
a_3
=
\left.
\frac{1}{2!}
\frac{d^2}{ds^2}
\left(
\frac{1}{Ts+1}
\right)
\right|_{s=0}
=
\left.
\frac{1}{2}
\frac{2T^2}{(Ts+1)^3}
\right|_{s=0}
=T^2
$$

$$
a_4
=
\left.
\frac{1}{Ts+1}
\cdot
\frac{1}{s^3}
\cdot
(Ts+1)
\right|_{s=-\frac{1}{T}}
=-T^3
$$

因此

$$
Y(s)
=
\frac{1}{s^3}
-
\frac{T}{s^2}
+
\frac{T^2}{s}
-
\frac{T^3}{Ts+1}
$$

进行拉氏反变换，得到单位抛物线响应：

$$
y(t)
=
\frac{1}{2}t^2
-
Tt
+
T^2
-
T^2e^{-\frac{t}{T}}
$$

即

$$
y(t)
=
\frac{1}{2}t^2
-
Tt
+
T^2
\left(
1-e^{-\frac{t}{T}}
\right)
$$

### 5.输入及时间响应的关系

输入信号的关系为：

$$
x(t)=\delta(t),\qquad
x(t)=1(t),\qquad
x(t)=t,\qquad
x(t)=\frac{1}{2}t^2
$$

它们之间满足

$$
x_{i\text{脉冲}}(t)
=
\frac{d x_{i\text{阶跃}}(t)}{dt}
=
\frac{d^2 x_{i\text{斜坡}}(t)}{dt^2}
=
\frac{d^3 x_{i\text{抛物线}}(t)}{dt^3}
$$

而时间响应间的关系为：

$$
y_{\text{脉冲}}(t)
=
\frac{d y_{\text{阶跃}}(t)}{dt}
=
\frac{d^2 y_{\text{斜坡}}(t)}{dt^2}
=
\frac{d^3 y_{\text{抛物线}}(t)}{dt^3}
$$

## 三、二阶系统的瞬态响应

微分方程为：

$$
\frac{d^2x_o(t)}{dt^2}
+
2\xi\omega_n\frac{dx_o(t)}{dt}
+
\omega_n^2x_o(t)
=
\omega_n^2x_i(t)
$$

传递函数为：

$$
G(s)
=
\frac{X_o(s)}{X_i(s)}
=
\frac{\omega_n^2}
{s^2+2\xi\omega_ns+\omega_n^2}
$$

其中：

- $\omega_n$ 称为**无阻尼自然频率**。
- $\xi$ 称为**阻尼比**。
- $\omega_n$ 和 $\xi$ 是二阶系统本身固有的、与外界无关的特征参数。

### 1.二阶系统特征根的讨论

令传递函数的特征多项式为 0，得

$$
s^2+2\xi\omega_n s+\omega_n^2=0
$$

解特征方程，可得特征根

$$
s_{1,2}
=
-\xi\omega_n
\pm
\omega_n\sqrt{\xi^2-1}
$$

二阶系统的特征根随阻尼比 $\xi$ 的不同而不同，可分为以下四种情况。

- 当 $0<\xi<1$ 时，为**欠阻尼系统**：

$$
s_{1,2}
=
-\xi\omega_n
\pm
j\omega_n\sqrt{1-\xi^2}
$$

此时特征根为一对共轭复数，系统传递函数的极点位于复平面左半平面。

- 当 $\xi=0$ 时，为**无阻尼系统**：

$$
s_{1,2}=\pm j\omega_n
$$

此时特征根为一对共轭纯虚根，系统传递函数的极点位于复平面的虚轴上。

- 当 $\xi=1$ 时，为**临界阻尼系统**：

$$
s_{1,2}=-\omega_n
$$

此时特征根为两个相等的负实根，系统传递函数的两个极点重合于复平面左半平面的负实轴上。

- 当 $\xi>1$ 时，为**过阻尼系统**：

$$
s_{1,2}
=
-\xi\omega_n
\pm
\omega_n\sqrt{\xi^2-1}
$$

此时特征根为两个不相等的负实根，系统传递函数的极点位于复平面的负实轴上。

### 2.二阶系统的单位脉冲响应

**定义：** 以单位脉冲函数 $\delta(t)$ 为输入的二阶系统输出。

系统输出的拉氏变换为

$$
X_o(s)=G(s)X_i(s)
$$

由于单位脉冲输入满足

$$
X_i(s)=\mathcal{L}[\delta(t)]=1
$$

因此

$$
X_o(s)=G(s)
$$

二阶系统的单位脉冲响应为

$$
x_o(t)
=
\mathcal{L}^{-1}
\left[
\frac{\omega_n^2}
{s^2+2\xi\omega_ns+\omega_n^2}
\right]
$$

将分母配方可得

$$
x_o(t)
=
\mathcal{L}^{-1}
\left[
\frac{\omega_n^2}
{(s+\xi\omega_n)^2+
\left(\omega_n\sqrt{1-\xi^2}\right)^2}
\right]
$$

- 输入为瞬态作用。
- 响应形式根据阻尼比 $\xi$ 的不同进行划分。

#### 欠阻尼系统：$0<\xi<1$

定义

$$
\omega_d=\omega_n\sqrt{1-\xi^2}
$$

其中 $\omega_d$ 称为二阶系统的**阻尼自然频率**。

则

$$
x_o(t)
=
\mathcal{L}^{-1}
\left[
\frac{\omega_n}{\sqrt{1-\xi^2}}
\cdot
\frac{\omega_n\sqrt{1-\xi^2}}
{(s+\xi\omega_n)^2+
\left(\omega_n\sqrt{1-\xi^2}\right)^2}
\right]
$$

因此

$$
x_o(t)
=
\frac{\omega_n}{\sqrt{1-\xi^2}}
e^{-\xi\omega_n t}
\sin\omega_d t,
\qquad t\geq0
$$

#### 无阻尼系统：$\xi=0$

此时

$$
x_o(t)
=
\mathcal{L}^{-1}
\left[
\omega_n
\cdot
\frac{\omega_n}{s^2+\omega_n^2}
\right]
$$

因此

$$
x_o(t)=\omega_n\sin\omega_n t
$$

#### 临界阻尼系统：$\xi=1$

此时

$$
x_o(t)
=
\mathcal{L}^{-1}
\left[
\frac{\omega_n^2}{(s+\omega_n)^2}
\right]
$$

因此

$$
x_o(t)
=
\omega_n^2t e^{-\omega_n t},
\qquad t\geq0
$$

#### 过阻尼系统：$\xi>1$

此时

$$
x_o(t)
=
\frac{\omega_n}{2\sqrt{\xi^2-1}}
\left\{
\mathcal{L}^{-1}
\left[
\frac{1}
{s+\left(\xi-\sqrt{\xi^2-1}\right)\omega_n}
\right]
-
\mathcal{L}^{-1}
\left[
\frac{1}
{s+\left(\xi+\sqrt{\xi^2-1}\right)\omega_n}
\right]
\right\}
$$

因此

$$
x_o(t)
=
\frac{\omega_n}{2\sqrt{\xi^2-1}}
\left[
e^{-\left(\xi-\sqrt{\xi^2-1}\right)\omega_n t}
-
e^{-\left(\xi+\sqrt{\xi^2-1}\right)\omega_n t}
\right]
$$

令

$$
s_1
=
-\omega_n\xi
-
\omega_n\sqrt{\xi^2-1}
$$

$$
s_2
=
-\omega_n\xi
+
\omega_n\sqrt{\xi^2-1}
$$

则

$$
s_1<s_2<0
$$

所以也可以写成

$$
x_o(t)
=
\frac{\omega_n}{2\sqrt{\xi^2-1}}
\left(
e^{s_2t}-e^{s_1t}
\right)
$$

### 3.二阶系统的单位阶跃响应

**定义：** 以单位阶跃函数 $1(t)$ 为输入的二阶系统输出。

输入信号为

$$
x_i(t)=1(t)
$$

其拉氏变换为

$$
X_i(s)=\mathcal{L}[1(t)]=\frac{1}{s}
$$

因此系统输出为

$$
X_o(s)
=
G(s)\frac{1}{s}
=
\frac{\omega_n^2}
{s^2+2\xi\omega_ns+\omega_n^2}
\cdot
\frac{1}{s}
$$

根据阻尼比 $\xi$ 的不同，二阶系统的单位阶跃响应可以分为以下几种情况。

#### 欠阻尼系统：$0<\xi<1$

定义阻尼自然频率

$$
\omega_d=\omega_n\sqrt{1-\xi^2}
$$

系统响应为

$$
x_o(t)
=
1
-
e^{-\xi\omega_nt}
\left(
\cos\omega_dt
+
\frac{\xi}{\sqrt{1-\xi^2}}
\sin\omega_dt
\right),
\qquad t\geq0
$$

利用三角函数公式，可进一步写成

$$
x_o(t)
=
1
-
e^{-\xi\omega_nt}
\frac{1}{\sqrt{1-\xi^2}}
\sin
\left(
\omega_dt
+
\arctan
\frac{\sqrt{1-\xi^2}}{\xi}
\right),
\qquad t\geq0
$$

式中第二项为**瞬态项**，是减幅正弦振荡函数，其振幅随时间增加而逐渐减小。

#### 无阻尼系统：$\xi=0$

此时系统响应为

$$
x_o(t)=1-\cos\omega_nt,
\qquad t\geq0
$$

系统输出为等幅振荡，不会随着时间增加而衰减。

#### 临界阻尼系统：$\xi=1$

系统响应为

$$
x_o(t)
=
1-(1+\omega_nt)e^{-\omega_nt},
\qquad t\geq0
$$

由于

$$
\dot{x}_o(t)
=
\omega_n^2t e^{-\omega_nt}>0
$$

因此 $x_o(t)$ **单调上升**，不存在振荡。

#### 过阻尼系统：$\xi>1$

令

$$
s_1
=
-\left(\xi+\sqrt{\xi^2-1}\right)\omega_n
$$

$$
s_2
=
-\left(\xi-\sqrt{\xi^2-1}\right)\omega_n
$$

则系统响应为

$$
x_o(t)
=
1
+
\frac{1}
{2\sqrt{\xi^2-1}
\left(\xi+\sqrt{\xi^2-1}\right)}
e^{-\left(\xi+\sqrt{\xi^2-1}\right)\omega_nt}
-
\frac{1}
{2\sqrt{\xi^2-1}
\left(\xi-\sqrt{\xi^2-1}\right)}
e^{-\left(\xi-\sqrt{\xi^2-1}\right)\omega_nt}
$$

也可以写成

$$
x_o(t)
=
1+
\frac{\omega_n}{2\sqrt{\xi^2-1}}
\left[
\frac{e^{s_1t}}{-s_1}
-
\frac{e^{s_2t}}{-s_2}
\right],
\qquad t\geq0
$$

当 $\xi>1.5$ 时，两个衰减指数项中，$e^{s_1t}$ 的衰减速度比 $e^{s_2t}$ 快得多，因此过渡过程主要由 $e^{s_2t}$ 项决定。

#### 二阶系统单位阶跃响应分析

- 当 $\xi<1$ 时，过渡过程为**衰减振荡**。随着阻尼比 $\xi$ 减小，振荡越强烈；当 $\xi=0$ 时，系统达到等幅振荡。

- 当 $\xi\geq1$ 时，过渡过程为**单调上升**；其中 $\xi=1$ 时过渡过程较快。

- 当

$$
\xi=0.4\sim0.8
$$

时，系统振荡适度，过渡过程较短，是控制系统设计中常采用的阻尼比范围。

- 决定过渡过程特性的主要是响应中的**瞬态响应部分**；合适的 $\omega_n$ 和 $\xi$ 可以得到较合适的过渡过程。

## 四、二阶系统响应的性能指标

### 相关约定

系统性能指标通常根据系统对**单位阶跃输入**的响应来界定，主要原因如下：

- 阶跃输入容易产生，且基于阶跃响应可以求得系统对其他输入的响应。
- 实际输入与阶跃输入具有一定相似性，而且阶跃输入可看作实际情况中较不利的输入情况。

对于欠阻尼二阶系统，常用的响应性能指标包括：

- 上升时间 $t_r$
- 峰值时间 $t_p$
- 最大超调量 $\sigma_p$
- 调整时间 $t_s$
- 振荡次数 $N$

欠阻尼二阶系统的单位阶跃响应为

$$
x_o(t)
=
1-
\frac{e^{-\xi\omega_n t}}{\sqrt{1-\xi^2}}
\sin
\left(
\omega_d t+
\arctan\frac{\sqrt{1-\xi^2}}{\xi}
\right),
\qquad t\geq 0
$$

其中阻尼自然频率为

$$
\omega_d=\omega_n\sqrt{1-\xi^2}
$$

令

$$
\beta
=
\arctan\frac{\sqrt{1-\xi^2}}{\xi}
$$

---

### 1. 上升时间 $t_r$

响应曲线**第一次达到稳态值所需要的时间**定义为上升时间。

当

$$
t=t_r
$$

时，有

$$
x_o(t_r)=1
$$

代入单位阶跃响应表达式：

$$
1
=
1-
\frac{e^{-\xi\omega_n t_r}}{\sqrt{1-\xi^2}}
\sin
\left(
\omega_d t_r+
\arctan\frac{\sqrt{1-\xi^2}}{\xi}
\right)
$$

因此

$$
\sin
\left(
\omega_d t_r+\beta
\right)=0
$$

即

$$
\omega_d t_r
=
\pi-\beta,\;
2\pi-\beta,\;
3\pi-\beta,\;\cdots
$$

由于上升时间取第一次到达稳态值的时间，因此

$$
\omega_d t_r=\pi-\beta
$$

所以

$$
t_r
=
\frac{\pi-\beta}{\omega_d}
$$

即

$$
t_r
=
\frac{1}{\omega_n\sqrt{1-\xi^2}}
\left(
\pi-
\arctan\frac{\sqrt{1-\xi^2}}{\xi}
\right)
$$

---

### 2. 峰值时间 $t_p$

响应曲线达到**第一个峰值所需要的时间**定义为峰值时间。

峰值处满足

$$
\frac{dx_o(t)}{dt}=0
$$

由单位阶跃响应求导，可得

$$
\frac{\xi\omega_n e^{-\xi\omega_n t}}
{\sqrt{1-\xi^2}}
\sin(\omega_d t+\beta)
-
\frac{\omega_d e^{-\xi\omega_n t}}
{\sqrt{1-\xi^2}}
\cos(\omega_d t+\beta)
=0
$$

整理得

$$
\tan(\omega_d t_p+\beta)
=
\frac{\sqrt{1-\xi^2}}{\xi}
$$

而

$$
\tan\beta
=
\frac{\sqrt{1-\xi^2}}{\xi}
$$

因此

$$
\omega_d t_p
=
0,\;\pi,\;2\pi,\;\cdots
$$

根据定义，$t_p$ 为第一次出现超调峰值的时间，因此取

$$
\omega_d t_p=\pi
$$

所以

$$
t_p=\frac{\pi}{\omega_d}
$$

即

$$
t_p
=
\frac{\pi}
{\omega_n\sqrt{1-\xi^2}}
$$

---

### 3. 最大超调量 $\sigma_p$

最大超调量定义为

$$
\sigma_p
=
\frac{x_o(t_p)-x_o(\infty)}
{x_o(\infty)}
\times100\%
$$

对于单位阶跃输入，

$$
x_o(\infty)=1
$$

且

$$
t_p=\frac{\pi}{\omega_d}
$$

代入单位阶跃响应表达式，可得

$$
\sigma_p
=
e^{-\frac{\pi\xi}{\sqrt{1-\xi^2}}}
\times100\%
$$

因此

$$
\boxed{
\sigma_p
=
e^{-\frac{\pi\xi}{\sqrt{1-\xi^2}}}
\times100\%
}
$$

可见，最大超调量 $\sigma_p$ **只与阻尼比 $\xi$ 有关**。

当

$$
\xi=0.4\sim0.8
$$

时，相应的最大超调量约为

$$
\sigma_p=25\%\sim1.5\%
$$

---

### 4. 调整时间 $t_s$

在过渡过程中，当输出响应进入规定的误差带，并且此后始终保持在误差带内时，对应的最短时间称为**调整时间**。

其定义为

$$
|x_o(t)-x_o(\infty)|
\leq
\Delta x_o(\infty),
\qquad t\geq t_s
$$

即

$$
x_o(\infty)-\Delta x_o(\infty)
\leq
x_o(t)
\leq
x_o(\infty)+\Delta x_o(\infty)
$$

对于单位阶跃响应，

$$
x_o(\infty)=1
$$

因此

$$
|x_o(t)-1|\leq\Delta
$$

欠阻尼二阶系统的单位阶跃响应为

$$
x_o(t)
=
1-
\frac{e^{-\xi\omega_n t}}
{\sqrt{1-\xi^2}}
\sin
\left(
\omega_d t+
\arctan\frac{\sqrt{1-\xi^2}}{\xi}
\right)
$$

为了保证响应始终位于误差带内，可利用包络线得到

$$
\frac{e^{-\xi\omega_n t}}
{\sqrt{1-\xi^2}}
\leq
\Delta
$$

因此

$$
t_s
\geq
\frac{1}{\xi\omega_n}
\ln
\frac{1}
{\Delta\sqrt{1-\xi^2}}
$$

#### 当 $\Delta=0.02$ 时

$$
t_s
\geq
\frac{
4+\ln\frac{1}{\sqrt{1-\xi^2}}
}
{\xi\omega_n}
$$

当

$$
0<\xi<0.7
$$

时，可近似为

$$
\boxed{
t_s\approx\frac{4}{\xi\omega_n}
}
$$

#### 当 $\Delta=0.05$ 时

$$
t_s
\geq
\frac{
3+\ln\frac{1}{\sqrt{1-\xi^2}}
}
{\xi\omega_n}
$$

当

$$
0<\xi<0.7
$$

时，可近似为

$$
\boxed{
t_s\approx\frac{3}{\xi\omega_n}
}
$$

---

### 5. 振荡次数 $N$

在过渡过程中，输出 $x_o(t)$**穿越其稳态值次数的一半**称为振荡次数。

欠阻尼系统的振荡周期为

$$
T_d=\frac{2\pi}{\omega_d}
$$

因此

$$
N
=
\frac{t_s}{2\pi/\omega_d}
$$

当

$$
0<\xi<0.7
$$

时，利用调整时间的近似表达式可得：

当

$$
\Delta=0.02
$$

时，

$$
N
=
\frac{2\sqrt{1-\xi^2}}{\pi\xi}
$$

当

$$
\Delta=0.05
$$

时，

$$
N
=
\frac{1.5\sqrt{1-\xi^2}}{\pi\xi}
$$

---

### 二阶系统性能指标总结

上升时间：

$$
t_r
=
\frac{\pi-\beta}{\omega_d}
=
\frac{1}{\omega_n\sqrt{1-\xi^2}}
\left(
\pi-
\arctan\frac{\sqrt{1-\xi^2}}{\xi}
\right)
$$

峰值时间：

$$
t_p=\frac{\pi}{\omega_d}
$$

最大超调量：

$$
\sigma_p
=
e^{-\frac{\pi\xi}{\sqrt{1-\xi^2}}}
\times100\%
$$

调整时间（$\Delta=0.02$）：

$$
t_s\approx\frac{4}{\xi\omega_n}
$$

振荡次数（$\Delta=0.02$）：

$$
N
=
\frac{2\sqrt{1-\xi^2}}{\pi\xi}
$$

其中：

- 增大 $\omega_n$，可以提高二阶系统的响应速度，减小上升时间 $t_r$、峰值时间 $t_p$ 和调整时间 $t_s$。
- 增大 $\xi$，可以减弱系统振荡，降低最大超调量 $\sigma_p$，减少振荡次数 $N$，但会使上升时间 $t_r$ 和峰值时间 $t_p$ 增大。
- 系统的响应速度与振荡性能之间往往存在矛盾，需要合理选择 $\omega_n$ 和 $\xi$，以满足系统的综合性能要求。
