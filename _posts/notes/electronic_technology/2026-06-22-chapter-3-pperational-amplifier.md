---
title: 电子技术第3章笔记 集成运算放大器
description: 电子技术第3章笔记
author: 阎梓瑜
date: 2026-06-22 17:30:00 +0800
categories: [笔记,电子技术]
tags: [电子技术]
pin: false
math: true
mermaid: true
---

## 1.集成运算放大器概述

### 1-1 集成运算放大器的特点

- 元器件参数的一致性和对称性好；
- 电阻的阻值受到限制，大电阻常用三极管恒流源代替，电位器需外接；
- 电容的容量受到限制，电感不能集成，故大电容、电感和变压器均需外接；
- 二极管多用三极管的发射结代替。

### 1-2 集成运算放大器的电路组成

**输入级：**输入电阻高，能减小零点漂移和抑制干扰信号，都采用带恒流源的差分放大器。

**中间级：**要求电压放大倍数高。常采用带恒流源的共发射极放大电路构成。

**输出级：**与负载相接，要求输出电阻低，带负载能力强，一般由互补对称电路或射极输出器构成。

**偏置电路：**由镜像恒流源等电路组成。

### 1-3 集成运算放大器的电压传输特性

![电压传输特性](assets/img/posts/notes/electronic_technology/chapter3/3-1.png){: .w-50}

### 1-4 理想运算放大器及其分析依据

![理想输出特性](assets/img/posts/notes/electronic_technology/chapter3/3-2.png){: .w-50}

#### 理想化的主要条件

1. 开环电压放大倍数

$$
A_{uo} \to \infty
$$

2. 开环输入电阻

$$
r_{id} \to \infty
$$

3. 开环输出电阻

$$
r_o \to 0
$$

4. 共模抑制比

$$
K_{\mathrm{CMRR}} \to \infty
$$

必须加**负反馈**才能使其工作在线性区

#### 理想运算放大器工作在线性区

差模输入电压约等于0,称为**虚短**

$$
u_+ = u_-
$$

输入电流约等于0,称为**虚断**

$$
i_+ \approx 0,\quad i_- \approx 0
$$

#### 理想运算放大器工作在饱和区

当 $u_+ > u_-$ 时，

$$
u_o = +U_{o(\mathrm{sat})}
$$

当 $u_+ < u_-$ 时，

$$
u_o = -U_{o(\mathrm{sat})}
$$

不存在“**虚短**”现象,仍存在“**虚断**”现象。

## 2.放大电路中的负反馈

### 2-1 反馈的基本概念

净输入信号：

$$
\dot{X}_d = \dot{X}_i - \dot{X}_f
$$

若反馈信号削弱了净输入信号，即：

$$
\dot{X}_d < \dot{X}_i
$$

则该反馈称为**负反馈**。

若反馈信号增强了净输入信号，即：

$$
\dot{X}_d > \dot{X}_i
$$

则该反馈称为**正反馈**。

引入**直流负反馈**的目的：稳定静态工作点

引入**交流负反馈**的目的：改善放大电路的性能

### 2-2 放大电路中的负反馈类型

![放大电路的负反馈类型](assets/img/posts/notes/electronic_technology/chapter3/3-3.png){:.w-75}

![电压串联负反馈](assets/img/posts/notes/electronic_technology/chapter3/3-4.png){:.w-50}

![电压并联负反馈](assets/img/posts/notes/electronic_technology/chapter3/3-5.png){:.w-50}

![电流串联负反馈](assets/img/posts/notes/electronic_technology/chapter3/3-6.png){:.w-50}

![电流并联负反馈](assets/img/posts/notes/electronic_technology/chapter3/3-7.png){:.w-50}

####  判断电压/电流反馈

如果反馈网络和负载 **并联** 在输出端，取的是**输出电压**，则为**电压反馈**

如果反馈网络和负载 **串联** 在输出回路中，取的是**输出电流**，则为**电流反馈**

#### 判断串联/并联反馈

如果反馈信号以**电压**形式串到输入回路中，输入端比较的是电压，则是**串联反馈**

如果反馈信号以**电流**形式并到输入节点，输入端比较的是电流，则是**并联反馈**

### 2-3 负反馈对放大电路性能的影响

#### 减小放大倍数，但是提高放大倍数

$$
A_f = \frac{A}{1+AF}
$$

#### 减小非线性失真

#### 展宽通频带

#### 影响输入电阻

串联负反馈会增大输入电阻:

$$
r_{if} = (1+AF)r_i
$$

并联负反馈会减小输入电阻:

$$
r_{if} = \frac{r_i}{1+AF}
$$

>$r_i=\frac{u_i}{i_i}$,串联反馈$u_i = u_d + u_f$,并联反馈$i_i = i_d + i_f$
{:.prompt-info}

#### 影响输出电阻

电压负反馈会减小输出电阻：

$$
r_{of} = \frac{r_o}{1+AF}
$$

电流负反馈会增大输出电阻：

$$
r_{of} = (1+AF)r_o
$$

>电压/电流负反馈的作用是稳定输出电压/电流，使其更像理想电压/电流源
{:.prompt-info}

## 3.集成运算放大器在信号运算方面的应用

运算放大器工作在线性区时，通常要引入深度负反馈，**反馈深度**$1+AF$远大于1,$A_f \approx \frac{1}{F}$，输出电压和输入电压的关系基本决定于电路的结构与参数，与运算放大器本身的参数关系不大

### 3-1 比例运算电路

#### 反相比例运算

![反相比例运算](assets/img/posts/notes/electronic_technology/chapter3/3-8.png){: .w-50}

$$
u_o = -\frac{R_F}{R_1}u_i
$$

$$
A_u = \frac{u_o}{u_i} = -\frac{R_F}{R_1}
$$

为了减小输入偏置电流造成的输出误差，要使两个输入端外接的等效电阻相等

$$
R_2=R_1\parallel R_F
$$

#### 同相比例运算

![同相比例运算](assets/img/posts/notes/electronic_technology/chapter3/3-9.png){:.w-50}

$$
u_o = \left(1+\frac{R_F}{R_1}\right)u_i
$$

$$
A_u = \frac{u_o}{u_i} = 1+\frac{R_F}{R_1}
$$

$$
R_2=R_1\parallel R_F
$$

![电压跟随器](assets/img/posts/notes/electronic_technology/chapter3/3-18.png){:.w-50}

当 $R_1 = \infty$ 或 $R_F = 0$ 时，

$$
u_o = u_i,\quad A_{uf}=1
$$

称**电压跟随器**，输入电阻大，输出电阻小，跟随性能比射极输出器更好

### 3-2 加法运算电路

#### 反相加法运算

![反相加法运算](assets/img/posts/notes/electronic_technology/chapter3/3-10.png){: .w-50}

$$
u_o = -R_F\left(\frac{u_{i1}}{R_{11}}+\frac{u_{i2}}{R_{12}}+\frac{u_{i3}}{R_{13}}\right)
$$

$$
R_2 = R_{11} \parallel R_{12} \parallel R_{13} \parallel R_F
$$

#### 同相加法运算

![同相加法运算](assets/img/posts/notes/electronic_technology/chapter3/3-11.png){: .w-50}

$$
u_o =
\left(1+\frac{R_F}{R_1}\right)
\frac{
\frac{u_{i1}}{R_{11}}+\frac{u_{i2}}{R_{12}}+\frac{u_{i3}}{R_{13}}
}{
\frac{1}{R_{11}}+\frac{1}{R_{12}}+\frac{1}{R_{13}}+\frac{1}{R_2}
}
$$

$$
R_{11} \parallel R_{12} \parallel R_{13} \parallel R_2
=
R_1 \parallel R_F
$$

>反相加法电路输入电阻较低，但共模电压低、各路权重独立，适合精确加权求和；同相加法电路输入电阻高，但共模电压高、各路权重相互影响，调节不如反相加法方便
{: .prompt-info}

### 3-3 差分比例运算电路（减法运算电路）

![减法运算电路](assets/img/posts/notes/electronic_technology/chapter3/3-12.png){: .w-50}

$$
u_o=\left(1+\frac{R_F}{R_1}\right)\frac{R_3}{R_2+R_3}u_{i2}-\frac{R_F}{R_1}u_{i1}
$$

>我感觉就是同相和反相加法电路用一下叠加原理
{: .prompt-info}

### 3-4 积分运算电路

![积分运算电路](assets/img/posts/notes/electronic_technology/chapter3/3-13.png){: .w-50}

$$
u_o=-\frac{1}{RC}\int u_i\,dt
$$

#### 其他积分运算电路

![其他积分运算电路](assets/img/posts/notes/electronic_technology/chapter3/3-19.png)

#### 比例-积分运算电路

![积分运算电路](assets/img/posts/notes/electronic_technology/chapter3/3-20.png)

这种运算器又称 PI 调节器，常用于控制系统中，以保证自控系统的稳定性和控制精度。改变 (R_F) 和 (C_F)，可调整比例系数和积分时间常数，以满足控制系统的要求。

### 3-5 微分运算电路

![微分运算电路](assets/img/posts/notes/electronic_technology/chapter3/3-14.png){: .w-50}

$$
u_o = -RC\frac{du_i}{dt}
$$

#### PID调节器

![PID调节器](assets/img/posts/notes/electronic_technology/chapter3/3-21.png){:.w-50}

$$
u_o = -\left[\left(\frac{R_2}{R_1}+\frac{C_1}{C_2}\right)u_i
+ C_1R_2\frac{du_i}{dt}
+ \frac{1}{R_1C_2}\int u_i\,dt\right]
$$

PID 调节器兼具比例调节的快速性、积分调节消除余差、微分调节超前控制能力。

### 3-6 指对运算电路

#### 对数运算电路

![对数运算电路](assets/img/posts/notes/electronic_technology/chapter3/3-15.png){: .w-50}

$$
i_D = I_S e^{\frac{u_D}{U_T}}
$$

$$
u_o = -U_T \ln \frac{u_I}{RI_S}
$$

#### 指数运算电路

![指数运算电路](assets/img/posts/notes/electronic_technology/chapter3/3-16.png){: .w-50}

$$
u_o = -RI_S e^{\frac{u_I}{U_T}}
$$

### 3-7 乘法运算电路

#### 乘法运算电路

![乘法运算电路](assets/img/posts/notes/electronic_technology/chapter3/3-17.png){: .w-50}

![乘法运算](assets/img/posts/notes/electronic_technology/chapter3/3-22.png){: .w-50}

$$
u_o \approx -I_S R e^{\frac{u_{o3}}{V_T}}
= -\frac{1}{I_S R}u_{i1}u_{i2}
$$

#### 乘法运算符号

![乘法器](assets/img/posts/notes/electronic_technology/chapter3/3-23.png){: .w-75}

#### 除法运算电路

![除法运算电路](assets/img/posts/notes/electronic_technology/chapter3/3-24.png){: .w-50}

$$
u_o = -\frac{R_2}{kR_1}\frac{u_{i1}}{u_{i2}}0
$$

## 4.集成运放在信号处理方面的应用

### 4-1 有源滤波器

**无源滤波器：**由电阻、电容和电感组成的滤波器。

>缺点：低频时体积大，很难做到小型化。

**有源滤波器：**含有运算放大器的滤波器。

>优点：体积小、效率高、频率特性好。

按频率范围的不同，滤波器可分为低通、高通、带通和带阻等。

#### 有源低通滤波器
iqoa bi ji iao
![有源低通滤波器](assets/img/posts/notes/electronic_technology/chapter3/3-25.png){:.w-50}

$$
\dot{U}_o=\left(1+\frac{R_F}{R_1}\right)\dot{U}_+
$$

$$
\dot{U}_+=\dot{U}_C=
\frac{-\mathrm{j}\dfrac{1}{\omega C}}
{R-\mathrm{j}\dfrac{1}{\omega C}}
\dot{U}_i
$$

$$
\frac{\dot{U}_o}{\dot{U}_i}
=
\frac{1+\dfrac{R_F}{R_1}}{1+\mathrm{j}\omega RC}
=
\frac{1+\dfrac{R_F}{R_1}}{1+\mathrm{j}\dfrac{\omega}{\omega_0}}
$$

其中，$\omega_0=\frac{1}{RC}$称为**特征频率**


显然，电路能使低于 $\omega_0$ 的信号顺利通过，衰减很小，而使高于 $\omega_0$ 的信号不易通过，衰减很大，称一阶有源低通滤波器。

为了改善滤波效果，使 $\omega > \omega_0$ 时信号衰减得更快些，常将两节 $RC$ 滤波环节串接起来，组成二阶有源低通滤波器。

![二阶有源低通滤波器](assets/img/posts/notes/electronic_technology/chapter3/3-26.png){:.w-50}

### 4-2 电压比较器

#### 基本电压比较器

![基本电压比较器](assets/img/posts/notes/electronic_technology/chapter3/3-27.png){:.w-50}

#### 滞回比较器

![滞回比较器](assets/img/posts/notes/electronic_technology/chapter3/3-28.png){:.w-50}

电路中引入了正反馈

1. 提高了比较器的响应速度
2. 门限电压受到输出电压的控制

$$
U_{T+}=+\frac{R_2}{R_2+R_F}U_Z
$$

$$
U_{T-}=-\frac{R_2}{R_2+R_F}U_Z
$$

$$
\Delta U_T = 2\frac{R_2}{R_2+R_F}U_Z
$$

与过零比较器相比具有以下优点：

1. 改善了输出波形在跃变时的陡度。
2. 回差提高了电路的抗干扰能力，$\Delta U$ 越大，抗干扰能力越强。

## 5.集成运放在波形发生方面的应用

### 滞回比较器的应用——矩形波发生器

![矩形波发生器](assets/img/posts/notes/electronic_technology/chapter3/3-29.png){:.w-50}

![工作波形](assets/img/posts/notes/electronic_technology/chapter3/3-30.png){:.w-50}

$$
T = T_1 + T_2 = 2R_FC\ln\left(1+\frac{2R_2}{R_1}\right)
$$

再用积分运算电路可以将方波转换为三角波