---
title: 机械原理 第10章 机械的运转及其速度波动的调节
description: 机械原理第10章笔记
author: 阎梓瑜
date: 2026-05-21 14:00:00 +0800
categories: [笔记,机械原理]
tags: [机械原理]
pin: false
math: true
mermaid: true
---

## 10-1 概述

**机械运转过程的三个阶段：** 启动阶段、稳定运转阶段和停车阶段

## 10-2 机械系统的等效动力学模型

### 一、等效动力学模型

1. 具有等效质量，其上作用有等效力的等效移动构件
2. 具有等效转动惯量，其上作用有等效力矩的转动构件

![等效动力学模型](assets/img/posts/notes/theory_of_machines_and_machanism/chapter10/10-3.png)

### 二、等效参数的确定

#### 1.等效质量和等效转动惯量

等效构件所具有的动能等于原整个机械系统的总动能

#### 2.等效力和等效力矩

等效力和等效力矩产生的瞬时功率等于原机械系统所有力和力矩的瞬时功率之和

## 10-3 在已知力作用下机械系统的运动规律

### 一、机械动力学方程式的建立

#### 1.能量形式的动力学方程式

$$
\operatorname{d}W = \operatorname{d}E
$$

#### 2. 力矩形式的动力学方程式

$$
J\frac{\mathrm{d}\omega}{\mathrm{d}t}
+
\frac{\omega^2}{2}
\frac{\mathrm{d}J}{\mathrm{d}\varphi}
=
M_d - M_r
$$

$$
m\frac{\mathrm{d}v}{\mathrm{d}t}
+
\frac{v^2}{2}
\frac{\mathrm{d}m}{\mathrm{d}s}
=
F_d - F_r
$$

当等效质量和等效转动惯量为常数时，有

$$
M_d - M_r
=
J\frac{\mathrm{d}\omega}{\mathrm{d}t}
$$

$$
F_d - F_r
=
m\frac{\mathrm{d}v}{\mathrm{d}t}
$$

## 10-4 机械速度波动及其调节方法

### 一、周期性速度波动及其调节

![周期性速度波动](assets/img/posts/notes/theory_of_machines_and_machanism/chapter10/10-5.png)

#### 1. 周期性速度波动的原因

$$
\int_{\varphi_a}^{\varphi_a+\varphi_T}
\left(M_d - M_r\right)\,\mathrm{d}\varphi
=
0
$$

>机械系统的公共周期为各参数周期的最小公倍数
{: .prompt-info}

#### 2. 平均加速度和速度不均匀系数

平均角速度指一个运动周期内角速度的平均值

$$
\omega_m
=
\frac{
\displaystyle \int_{0}^{\varphi_T} \omega \,\mathrm{d}\varphi
}{
\varphi_T
}
$$

在工程上，常用算术平均值来近似

$$
\omega_m
\approx
\frac{\omega_{\min}+\omega_{\max}}{2}
$$

用速度不均匀系数表示机械系统速度波动的程度

$$
\delta
=
\frac{\omega_{\max}-\omega_{\min}}{\omega_m}
$$

$$
\omega_{\max}^{2}
-
\omega_{\min}^{2}
=
2\omega_m^{2}\delta
$$

#### 3.周期性速度波动的调节方法——飞轮调速原理

一个周期内，系统对外界做的最大盈功（或亏功）成为最大盈亏功

$$
\Delta W_{\max}
=
E_{\max}-E_{\min}
=
\frac{1}{2}J\omega_{\max}^{2}
-
\frac{1}{2}J\omega_{\min}^{2}
$$

$$
\delta
=
\frac{\Delta W_{\max}}{(J+J_F)\omega_m^{2}}
$$

加装一个具有等效转动惯量$J_F$的飞轮之后

$$
\delta
=
\frac{\Delta W_{\max}}{(J+J_F)\omega_m^{2}}
$$

$$
J_F
\geq
\frac{\Delta W_{\max}}{\omega_m^{2}[\delta]}
-
J
$$

为了简化计算

$$
J_F
=
\frac{\Delta W_{\max}}{\omega_m^{2}[\delta]}
$$

>这里求得是飞轮的等效转动惯量，实际转动惯量$J_F'=J_F\left(\frac{\omega_m}{\omega_A}\right)^2$
{: .prompt-warning}