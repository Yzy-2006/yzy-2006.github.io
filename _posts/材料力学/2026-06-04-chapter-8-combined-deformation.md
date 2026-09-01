---
title: 材料力学 第8章 组合变形
description: 材料力学第8章笔记
author: 阎梓瑜
date: 2026-06-04 21:30:00 +0800
categories: [材料力学]
tags: [材料力学]
pin: false
math: true
mermaid: true
---

## 8-1 斜弯曲

### 8.1.1 横截面内力与斜弯曲变形

**斜弯曲:** 当外力作用面不通过主惯性平面时，梁的轴线不再位于外力的作用面内
>主惯性平面是指：通过杆件轴线，并且包含截面某一条主惯性轴的纵向平面
{: .peompt-info}

![斜弯曲受力](assets/img/posts/notes/machanics_of_materials/chapter8/8-1.jpg)

$$
M_z(x)=F_y(l-x)=F\sin\beta\,(l-x)
$$

$$
M_y(x)=F_z(l-x)=F\cos\beta\,(l-x)
$$

利用叠加原理可知合位移$\delta$与主轴$z$的夹角$\varphi$满足

$$
\tan \varphi = \frac{I_y}{I_z}\tan\beta
$$

$\varphi \neq \beta$时，绕曲线与载荷不共面

### 8.1.2 横截面上应力计算

$$
\sigma_x
=\sigma_x'+\sigma_x''
=-\frac{M_z}{I_z}y
-\frac{M_y}{I_y}z
$$

正应力为零的位置即为中性轴所在位置，所以中性轴方程为

$$
\frac{M_z}{I_z}y+\frac{M_y}{I_y}z=0
$$

中性轴与主轴的夹角$\alpha$满足

$$
\tan\alpha
=\frac{y}{z}
=-\frac{M_y}{M_z}\cdot\frac{I_z}{I_y}
=-\frac{I_z}{I_y}\cot\beta
$$

进而可得

$$
\tan\alpha\cdot\tan\varphi=-1
$$

所以**中性轴和挠曲方向正交**

### 8.1.3 横截面上最大正应力

最大应力依然出现在距离中性轴最远的位置

$$
\sigma_{xe}
=\sigma_{x_{tmax}}
=\frac{M_y}{W_y}+\frac{M_z}{W_z}
$$

$$
\sigma_{xf}
=\sigma_{x_{cmax}}
=-\frac{M_y}{W_y}-\frac{M_z}{W_z}
$$

>这里的$W$和纯弯曲时候的是一样的
{: .prompt-info}

## 8-2 偏心拉伸与压缩

### 8.2.1 横截面上的内力

内力分量为

$$
\left\{
\begin{aligned}
F_N &= F' = F,\\
M_y &= m_y = F z_F,\\
M_z &= m_z = F y_F.
\end{aligned}
\right.
$$

由此可见，偏心拉压实际上是**拉压与弯曲的组合变形**

### 8.2.2 横截面上的应力

$$
\sigma_x
=\sigma_x'+\sigma_x''+\sigma_x'''
=\frac{F}{A}
\left(
1+\frac{y_F}{i_z^2}y
+\frac{z_F}{i_y^2}z
\right)
$$ 

所以中性轴方程为

$$
1+\frac{y_F}{i_z^2}y
+\frac{z_F}{i_y^2}z=0
$$

### 8.2.3 横截面上的最大应力

$$
\sigma_{x_e}
=\sigma_{x,\mathrm{t},\max}
=\frac{F}{A}
+\frac{M_y}{W_y}
+\frac{M_z}{W_z}
$$

$$
\sigma_{x_f}
=\sigma_{x,\mathrm{c},\max}
=\frac{F}{A}
-\frac{M_y}{W_y}
-\frac{M_z}{W_z}
$$

### 8.2.4 截面核心

控制偏心外力作用点的位置来实现中性轴不在截面之内

## 8-3 弯曲和扭转

危险点为上下两点

**扭转切应力**

$$
\tau_{xz}=\frac{T}{W_t}
$$

**弯曲正应力**

$$
\sigma_x=\frac{M_z}{W_z}
$$

危险点的主应力为

$$
\left\{
\begin{aligned}
\sigma_1
&=\sigma'
=\frac{\sigma_x}{2}
+\sqrt{
\left(
\frac{\sigma_x}{2}
\right)^2
+\tau_{xz}^2
},\\
\sigma_2&=0,\\
\sigma_3
&=\sigma''
=\frac{\sigma_x}{2}
-\sqrt{
\left(
\frac{\sigma_x}{2}
\right)^2
+\tau_{xz}^2
}.
\end{aligned}
\right.
$$
