---
title: 机械原理 第6章 凸轮机构及其设计
description: 机械原理第6章笔记
author: 阎梓瑜
date: 2026-05-17 20:30:00 +0800
categories: [机械原理]
tags: [机械原理]
pin: false
math: true
mermaid: true
---

## 6-1 凸轮机构的分类 

### 一、按两活动构件之间的相对运动特性

1. 平面凸轮机构
   1. 盘形凸轮
   2. 移动凸轮
2. 空间凸轮机构

### 二、按从动件运动副元素形状分类

1. 尖顶从动件
2. 滚子从动件
3. 平底从动件

### 三、按凸轮高副的锁合方式

1. 力锁合
2. 形锁合

## 6-2 从动件的运动规律及其选择

### 一、凸轮机构的运动循环及基本名词术语

1. **凸轮基圆：** 以凸轮轴心$O$为圆心，一起轮廓最小向径$r_O$为半径所作的圆称为基圆，基圆半径用$r_O$表示
2. **偏距：** 从动件导路中心线相对凸轮轴心$O$偏置的距离称为偏距$e$,以$O$为圆心，$e$为半径的圆称为偏距圆
3. **从动件行程：** 从动件的最大位移
4. **从动件推程：** 在凸轮推动下使从动件远离凸轮轴心的过程，此过程中凸轮转过的角度称为推程运动角$\varPhi_O$
5. **从动件回程：** 在弹簧力或其他外力作用下使从动件移近凸轮轴心的过程，此过程中凸轮转过的角度称为推程运动角$\varPhi'_O$
6. **从动件远（近）休程：** 从动件在距凸轮轴心最远（最近）位置处休止的过程，此过程凸轮转过的角度称为远（近）休止角，用$\varPhi_s、\varPhi'_s$表示

### 二、从动件运动规律

![凸轮运动规律表](assets/img/posts/notes/theory_of_machines_and_machanism/chapter6/sheet.png)

![选择凸轮运动规律](assets/img/posts/notes/theory_of_machines_and_machanism/chapter6/sheet2.png)

## 6-3 按预定运动规律设计盘形凸轮轮廓

### 一、凸轮轮廓设计的基本原理

**反转法：** 让凸轮静止不动，让从动件相对于凸轮轴心作反转运动

### 二、理论轮廓和实际轮廓

**理论轮廓：** 把滚子中心视为尖顶从动件的尖顶得到的尖顶从动件轮廓
**实际轮廓：** 以理论轮廓上各点为圆心，滚子半径为半径的包络线

## 6-4 盘形凸轮机构基本尺寸的确定

### 一、凸轮机构的压力角$\alpha$及其许用值

![求凸轮机构的压力角](assets/img/posts/notes/theory_of_machines_and_machanism/chapter6/alpha.png)

图中凸轮机构的瞬时效率计算公式为

$$
\eta =
\frac{
\cos(\alpha+\varphi_1)
-
\left(1+\frac{2b}{l}\right)
\sin(\alpha+\varphi_1)\tan\varphi_2
}{
\cos\alpha
}
$$

效率降为零时，机构发生自锁，压力角为临界压力角

$$
\alpha_c
=
\arctan
\left\{
\frac{1}{
\left[
\left(1+\frac{2b}{l}\right)\tan\varphi_2
\right]
}
\right\}
-\varphi_1
$$

通常规定最大压力角$\alpha_{max}$小于等于许用压力角$[\alpha]$

>**推程（工作行程）：**直动从动件取 $[\alpha]=30^\circ \sim 40^\circ$；摆动从动件取 $[\alpha]=35^\circ \sim 45^\circ$。  
>**回程（空回行程）：**考虑到此时从动件靠其他外力（如弹簧力等）推动返回，故不会自锁，许用压力角的取值可以适当放宽。直动和摆动从动件推荐取 $[\alpha]'=70^\circ \sim 80^\circ$。

### 二、按许用压力角确定凸轮轮廓的基本尺寸

$$
\omega_1 \overline{OP_{12}} = v_2
$$

$$
\overline{OP}_{12}
=
\frac{v_2}{\omega_1}
=
\frac{ds}{d\varphi}
$$

$$
\tan \alpha
=
\frac{\left|\overline{OP}_{12}-e\right|}{s_0+s}
=
\frac{\left|\dfrac{ds}{d\varphi}-e\right|}{s_0+s}
$$

其中，$s_0=\sqrt{r_0^2-e^2}$

**如何确定凸轮轴心许用位置以及$r_0$和$e$？**

![确定凸轮轴心位置](assets/img/posts/notes/theory_of_machines_and_machanism/chapter6/center.png)

这里的详细推到过程可以看课本的$P_{162}-P_{163}$

>$\dfrac{ds}{d\varphi}$在坐标轴的定义按从动件速度方向绕凸轮转动方向转$90^\circ$。例如，凸轮顺时针转动的时候推程在右。
{: .prompt-info }

**如何确定凸轮偏置的方位**

![凸轮偏置](assets/img/posts/notes/theory_of_machines_and_machanism/chapter6/e.png)

为了减小压力角，通常要让偏置和推程的速度瞬心在轴心的同侧

>基圆下半圆的转动方向指向哪导路就偏向哪
{: .prompt-info }

### 三、按凸轮轮廓全部外凸条件确定基圆半径(针对直动平底从动件)

$$
r_0 \geq (\rho_{\min}-s-s'')_{\max}  \
 (0 \leq \varphi \leq 2\pi)
$$

### 四、滚子半径的选择

$$
r_r < \rho_{\min} - \Delta 
$$

式中，$\rho_{\min}$ 为凸轮理论轮廓外凸部分的最小曲率半径；$\Delta = 3 \sim 5\ \text{mm}$。
