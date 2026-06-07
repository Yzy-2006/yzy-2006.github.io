---
title: 机械原理 第3章 平面机构的运动分析
description: 机械原理第3章笔记
author: 阎梓瑜
date: 2026-05-15 21:00:00 +0800
categories: [笔记,机械原理]
tags: [机械原理]
pin: false
math: true
mermaid: true
---

## 3-2 用速度瞬心法对平面机构进行速度分析

### 一、速度瞬心和机构中速度瞬心的数目

**速度瞬心：** 相对作平面运动的两构件上瞬时相对速度等于零的点
含有$m$个构件 **(包含机架)** 的机构，其速度瞬心的数目$K$为
$$
K=\frac{m(m-1)}{2}
$$

### 二、机构中速度瞬心位置的确定

#### 1.直接构成运动副两构件的速度瞬心位置

1. **转动副：**转动副的中心即为两构件的速度瞬心
2. **移动副：**速度瞬心在垂直于导路方向的无穷远处
3. **平面高副：**纯滚动时接触点即为速度瞬心；既作相对滚动又作相对滑动时速度瞬心在接触点处的公法线上

>移动副可进一步扩展为相对运动为纯平移的两构件速度瞬心都在无穷远处
{: .prompt-info}

#### 2.不直接构成运动副两构件的速度瞬心位置

**三心定理：**三个作平面运动的构件的三个速度瞬心必在同一条直线上                              

### 三、速度瞬心法在平面机构速度分析中的应用

#### 1.铰链四杆机构

可以确定主动件和从动件的角速度之比

![铰链四杆机构](assets/img/posts/notes/theory_of_machines_and_machanism/chapter3/four-bar_linkage.png)

$$
\begin{aligned}
\because\quad v_{13} &= v_{13} \\
\therefore\quad \omega_1 \overline{P_{14} P_{13}} &= \omega_3 \overline{P_{34} P_{13}} \\
化简得\quad \frac{\omega_1}{\omega_3} &= \frac{\overline{P_{34} P_{13}} }{\overline{P_{14} P_{13}} }
\end{aligned}
$$

>个人感觉分析还是要从**绝对瞬心**入手，**相对瞬心**相对于不同的**绝对瞬心**的速度相同，速度瞬心同时处在两个构件上，分别求速度
{: .prompt-tip }

#### 2.曲柄滑块机构

可以求滑块的移动速度

![曲柄滑块机构](assets/img/posts/notes/theory_of_machines_and_machanism/chapter3/slider_crank.png)

$$
P_{24}是绝对瞬心
$$

>只要下标里面包含机架的应该就是绝对瞬心
{: .prompt-tip }

$$
v_3=v_{P_{13}}=\omega_1\ \overline{P_{12} P_{13}} 
$$

>瞬心的含义是：在该瞬间，两个构件上经过这个点的速度大小和方向相同。对于平动的构件来说，经过任何点的速度都是平动的速度
{: .prompt-tip }


#### 3.凸轮机构

![凸轮机构](assets/img/posts/notes/theory_of_machines_and_machanism/chapter3/cam.png)

$$
v_2=v_{P_{12}}=\omega_1\ \overline{P_{13} P_{12}} 
$$

>移动副的瞬心不是任意无穷远点，而是在垂直于相对移动速度方向的无穷远处。$P_{23}$位于水平方向的无穷远处。也就是说，任何经过$P_{23}$的有限直线，都应当是一条水平直线
{: .prompt-tip }

#### 4.齿轮-连杆机构

![齿轮连杆机构](assets/img/posts/notes/theory_of_machines_and_machanism/chapter3/gear_linkage.png)

**瞬心多边形法**

1. 计算出瞬心的数目。
2. 按构件数目画凸 m 边形的 m 个顶点，每个顶点代表一个构件，并按顺序标注顶点号 1，2，…，m，两个顶点间的连线代表一个以该两顶点号为下标的两构件的瞬心。
3. 三个顶点连线构成的三角形的三条边表示三瞬心共线。
4. 利用两个三角形的公共边可求未知瞬心，即未知瞬心位于能与该瞬心组成三角形的其他两已知瞬心的连线上。
![瞬心多边形](assets/img/posts/notes/theory_of_machines_and_machanism/chapter3/instant_center_polygon.png)
