---
title: 材料力学 第6章 扭转
description: 材料力学第6章笔记
author: 阎梓瑜
date: 2026-05-21 21:00:00 +0800
categories: [笔记,材料力学]
tags: [材料力学]
pin: false
math: true
mermaid: true
---

## 6-1 扭转杆件的内力

**扭转：**在一对大小相等、转向相反的外力偶矩作用下，杆的各横截面发生相对转动的变形形式

![扭转](assets/img/posts/notes/machanics_of_materials/chapter6/6-1.png){: .w-75 .normal}

**外扭矩（$M_x$）:** 使杆产生扭转变形的外力偶矩

**扭转角（$\theta$）** 两个横截面的相对转角

**切应变（$\gamma$）** 直角的改变量

![扭矩方向](assets/img/posts/notes/machanics_of_materials/chapter6/6-2.png){: .w-50 .normal}

**扭矩的正负号规定**

正的扭矩背离截面；负的扭矩指向截面

>画图的时候$T$要用双箭头
{: .prompt-info}

**扭矩图：** 表示扭矩和截面位置之间关系的图线

## 6-2 圆柱扭转横截面上的切应力

### 静力平衡方程

![静力平衡方程](assets/img/posts/notes/machanics_of_materials/chapter6/6-4.png){: .w-50 .normal}

$$
\sum M_x = 0,\qquad \iint_A \rho \tau_{x\phi}\,\mathrm{d}A - T = 0
$$

### 几何方程

**平面假设：** 圆轴扭转变形后，横截面仍保持为平面，但其形状、大小以及两横截面间距离均不改变

![扭转的几何变形](assets/img/posts/notes/machanics_of_materials/chapter6/6-6a.png)

$$
\gamma_{x\phi} \approx \tan \gamma_{x\phi}
= \frac{\overset{\frown}{ff'}}{\mathrm{d}x}
= \rho \frac{\mathrm{d}\phi}{\mathrm{d}x}
$$

### 物理方程

![受力状态](assets/img/posts/notes/machanics_of_materials/chapter6/6-6c.png){: .w-50 .normal}

$$
\tau_{x\phi} = G\gamma_{x\phi} = G\rho\frac{\mathrm{d}\phi}{\mathrm{d}x}
$$

式中,$\frac{\mathrm{d}\phi}{\mathrm{d}x}$是相距为单位长度的两横截面相对扭过的角度，称为**单位长度扭转角**

### 横截面上的切应力公式

![横截面切应力](assets/img/posts/notes/machanics_of_materials/chapter6/6-6d.png){: .w-50 .normal}

联立以上三个方程得

$$
\frac{\mathrm{d}\phi}{\mathrm{d}x} = \frac{T}{G I_p}
$$

其中，$I_p = \iint_A \rho^2 \,\mathrm{d}A$为截面的**极惯性矩**，$G I_p$为**抗扭刚度**

再将其代回可得圆轴扭转横截面切应力公式

$$
\tau_{x\phi} = \frac{T}{I_p}\rho
$$

所以最大切应力在横截面外圆周的各个点上

$$
\tau_{x\phi,\max}
= \frac{T}{I_p}\rho_{\max}
= \frac{T}{I_p}R
= \frac{T}{W_t}
$$

其中，$W_t = \frac{I_p}{R}$称为**抗扭截面系数**

>对于圆截面，$W_t = \frac{\pi}{16}D^3\left(1-\alpha^4\right)$，其中，$\alpha = \frac{d}{D}$
{: .prompt-info}

## 6-3 圆柱扭转破坏模式的分析

![破坏模式](assets/img/posts/notes/machanics_of_materials/chapter6/6-7.png){: .w-50 .normal}

若材料抗拉压能力差，构件沿$45^\circ$斜截面发生破坏 **（脆性材料）**

若材料抗剪切能力差，构件沿横截面发生破坏 **（塑形材料）**

## 6-4 圆柱扭转变形与变形能

### 圆柱扭转变形公式

$$
\mathrm{d}\phi = \frac{T}{G I_p}\,\mathrm{d}x
$$

$$
\phi = \int_0^l \mathrm{d}\phi
= \int_0^l \frac{T}{G I_p}\,\mathrm{d}x
$$

如果圆轴为材料均匀的等直圆杆，并且各个截面扭矩相等

$$
\phi = \frac{Tl}{G I_p}
$$

### 圆柱扭转的变形能

$$
e = \frac{1}{2}\tau_{x\phi}\gamma_{x\phi}
= \frac{1}{2}\cdot \frac{\tau_{x\phi}^{2}}{G}
$$

$$
\mathrm{d}E_\gamma
= \left( \iint_A e\,\mathrm{d}A \right)\mathrm{d}x
= \left( \iint_A \frac{\tau_{x\phi}^{2}}{2G}\,\mathrm{d}A \right)\mathrm{d}x
$$

代入切应力公式得

$$
\mathrm{d}E_\gamma = \frac{T^2}{2G I_p}\,\mathrm{d}x
$$

整个圆轴的变形能为

$$
E_\gamma
= \int_0^l \mathrm{d}E_\gamma
= \int_0^l \frac{T^2}{2G I_p}\,\mathrm{d}x
$$

若圆轴材料及各个截面尺寸与扭矩均相等

$$
E_\gamma = \frac{T^2 l}{2G I_p}
$$