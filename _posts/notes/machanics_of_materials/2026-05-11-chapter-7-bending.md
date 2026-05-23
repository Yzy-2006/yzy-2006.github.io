---
title: 材料力学 第7章 弯曲
description: 材料力学第7章笔记
author: 阎梓瑜
date: 2026-05-11 15:53:00 +0800
categories: [笔记,材料力学]
tags: [材料力学]
pin: false
math: true
mermaid: true
---

## 7-1 梁的内力 剪力与弯矩

### 基本概念

**弯曲变形:** 由直线变成曲线的变形形式

**梁：** 以弯曲为主要变形的杆件

- **简支梁：** 一端是固定铰支约束，一端是可动铰支约束
- **外伸梁：** 有外伸部分的简支梁
- **悬臂梁：** 一端固定，一端自由的梁
  
![梁](/assets/img/posts/notes/machanics_of_materials/chapter7/beam.png){: .w-50 .normal}

> 悬臂梁的固定端对杆件不止有力，还有力偶的作用
{: .prompt-warning }

![平面弯曲构件](/assets/img/posts/notes/machanics_of_materials/chapter7/bending_member.png){: .w-50 .right}

### 平面弯曲构件的特点

**受力特点**

1. 构件存在纵轴线和对称平面
2. 外力和外力偶都作用在对称平面
3. 外力垂直于纵轴线
   
**变形特点**

纵轴线由直线变成曲线，但仍位于对称平面内

### 剪力和弯矩的正负号规定

![剪力和弯矩的方向](/assets/img/posts/notes/machanics_of_materials/chapter7/shear_force_symbol.png){: .w-75 .normal}

> **剪力方向的判断：**使用右手定则，指向纸面外为正(左下角坐标系z轴的正方向)  
> **弯矩方向的判断：**引起“下凸”的弯矩为正
{: .prompt-tip }

## 7-2 剪力图与弯矩图

![剪力图与弯矩图](/assets/img/posts/notes/machanics_of_materials/chapter7/shear_bending_moment_diagram.png){: .w-50 .right}

### 定义

以横坐标x表示梁的截面位置，纵坐标表示剪力和弯矩的数值

### 性质

1. **集中力作用处：**剪力发生突变，突变量为集中力的数值；弯矩连续，但出现折点(斜率不连续)
2. **集中力偶作用处：**弯矩不连续，发生突变，但剪力不受影响。

>突变量的方向和集中力（力偶）的方向相反
{: .prompt-tip}

## 7-3 载荷、剪力及弯矩间的关系

$$
\frac{dF_s(x)}{dx} = -q(x)
$$

$$
\frac{dM(x)}{dx} = -F_s(x)
$$

$$
\frac{d^2M(x)}{dx^2} = q(x)
$$

![表格](/assets/img/posts/notes/machanics_of_materials/chapter7/sheet.png)

## 7-4 纯弯曲梁的正应力

### 纯弯曲和剪力弯曲的概念

**纯弯曲：** 梁的横截面上只有弯矩的弯曲

**剪力弯曲：** 梁的横截面上既有弯矩又有剪力的弯曲

### 静力平衡方程

![静力平衡](assets/img/posts/notes/machanics_of_materials/chapter7/7-13a.png){: .w-50 .normal}

$$
\sum F_x = 0
\qquad
\iint_A -\sigma_x \,\mathrm{d}A = 0
$$

$$
\sum M_y = 0
\qquad
\iint_A -z\sigma_x \,\mathrm{d}A = 0
$$

$$
\sum M_z = 0
\qquad
\iint_A y\sigma_x \,\mathrm{d}A - M_z = 0
$$

### 几何方程

**平面假设：** 假设梁弯曲变形后，横截面仍保持为平面，并发生相对转动，与变形后的轴线依然正交

**中性层：** 纵向线段不伸长也不缩短

**中性线：** 中性层与任一横截面的交线   

![几何变形](assets/img/posts/notes/machanics_of_materials/chapter7/7-14.png)

$$
\varepsilon_x
= \frac{(\rho-y)\mathrm{d}\theta-\mathrm{d}x}{\mathrm{d}x}
= \frac{(\rho-y)\mathrm{d}\theta-\rho\,\mathrm{d}\theta}{\rho\,\mathrm{d}\theta}
= -\frac{y}{\rho}
$$

### 物理方程

$$
\sigma_x = E\varepsilon_x = -E\frac{y}{\rho}
$$

### 横截面上正应力公式

$$
\iint_A -E\frac{y}{\rho}\,\mathrm{d}A
= -\frac{E}{\rho}\iint_A y\,\mathrm{d}A = 0
$$

$$
\iint_A -E\frac{y}{\rho}\,\mathrm{d}A
= -\frac{E}{\rho}\iint_A y\,\mathrm{d}A = 0
$$

由此可知，截面的中性轴$z$为截面的**形心轴**