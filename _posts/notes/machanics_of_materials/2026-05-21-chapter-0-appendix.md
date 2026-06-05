---
title: 材料力学 附录 截面的几何性质
description: 材料力学第0章笔记
author: 阎梓瑜
date: 2026-05-21 19:30:00 +0800
categories: [笔记,材料力学]
tags: [材料力学]
pin: false
math: true
mermaid: true
---

# 一、静矩 形心
## 1.静矩
$$
\left\{
\begin{aligned}
S_y = \int_A z \operatorname{d}\! A \\
S_z = \int_A y \operatorname{d}\! A
\end{aligned}
\right.
$$
## 2.形心
$$
\left\{
\begin{aligned}
\overline{y}=\frac{S_z}{A} \\
\overline{z}=\frac{S_y}{A}
\end{aligned}
\right.
$$

## 3.形心轴
若截面对某一坐标轴的静矩为零，则该坐标轴必通过截面的形心，即为**形心轴**

## 4.组合图形的形心计算
$$
\left\{
\begin{aligned}
y_c
=
\frac{\sum A_i y_{ci}}{A}
\\[1em]
z_c
=
\frac{\sum A_i z_{ci}}{A}
\end{aligned}
\right.
$$

# 二、惯性矩 极惯性矩 惯性积 惯性半径
## 1. 惯性矩
$$
\left\{
\begin{aligned}
I_y=\int_A z^2 \operatorname{d} \! A
\\
I_z=\int_A y^2 \operatorname{d} \! A
\end{aligned}
\right.
$$

## 2. 极惯性矩
$$
I_p = \int_A \rho^2 \operatorname{d} \! A = \int_A (y^2 + z^2) \operatorname{d} \! A = I_z + I_y
$$

>对于空心圆截面，$I_y=I_z=\frac{I_p}{2}=\frac{\pi D^4}{64} (1-\alpha^4)$
{: .prompt-tip}

## 3. 惯性积
$$
I_{yz} = \int_A  yz \operatorname{d} \! A
$$

## 4.惯性半径
$$
\left\{
\begin{aligned}
i_y=\sqrt{\frac{I_y}{A}}
\\
i_z=\sqrt{\frac{I_z}{A}}
\end{aligned}
\right.
$$

## 三、平行移轴公式
$$
\left\{
\begin{aligned}
I_y&=I_{y_C}+\overline{z}^2 A
\\
I_z&=I_{z_C}+\overline{y}^2 A
\\
I_{yz}&=I_{y_C z_C}+\overline{yz} A
\end{aligned}
\right.
$$

## 四、转轴公式
$$
\left\{
\begin{aligned}
I_{z1}
&=
\frac{I_z+I_y}{2}
+
\frac{I_z-I_y}{2}\cos 2\alpha
-
I_{zy}\sin 2\alpha
\\[1em]
I_{y1}
&=
\frac{I_z+I_y}{2}
-
\frac{I_z-I_y}{2}\cos 2\alpha
+
I_{zy}\sin 2\alpha
\\[1em]
I_{z1y1}
&=
\frac{I_z-I_y}{2}\sin 2\alpha
+
I_{zy}\cos 2\alpha
\end{aligned}
\right.
$$

## 五、主轴 主惯性矩 形心主轴 形心主惯性矩
**主轴：** 惯性矩有极值、惯性积为零的轴

**主惯性矩：** 对主轴的惯性矩

**形心主轴** 通过形心的主轴

**形心主惯性矩：** 对形心主轴的惯性矩