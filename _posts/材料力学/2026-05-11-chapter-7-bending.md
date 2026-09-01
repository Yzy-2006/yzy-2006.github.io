---
title: 材料力学 第7章 弯曲
description: 材料力学第7章笔记
author: 阎梓瑜
date: 2026-05-11 15:53:00 +0800
categories: [材料力学]
tags: [材料力学]
pin: false
math: true
mermaid: true
---

## 7-1 梁的内力 剪力与弯矩

### 7-1-1 基本概念

**弯曲变形:** 由直线变成曲线的变形形式
**梁：** 以弯曲为主要变形的杆件
- **简支梁：** 一端是固定铰支约束，一端是可动铰支约束
- **外伸梁：** 有外伸部分的简支梁
- **悬臂梁：** 一端固定，一端自由的梁
  
![梁](/assets/img/posts/notes/machanics_of_materials/chapter7/beam.png){: .w-50 .normal}

> 悬臂梁的固定端对杆件不止有力，还有力偶的作用
{: .prompt-warning }

![平面弯曲构件](/assets/img/posts/notes/machanics_of_materials/chapter7/bending_member.png){: .w-50 .right}

### 7-1-2 平面弯曲构件的特点

**受力特点**

1. 构件存在纵轴线和对称平面
2. 外力和外力偶都作用在对称平面
3. 外力垂直于纵轴线
   
**变形特点**

纵轴线由直线变成曲线，但仍位于对称平面内

### 7-1-3 剪力和弯矩的正负号规定

![剪力和弯矩的方向](/assets/img/posts/notes/machanics_of_materials/chapter7/shear_force_symbol.png){: .w-75 .normal}

> **剪力方向的判断：**使用右手定则，指向纸面外为正(左下角坐标系z轴的正方向)  
> **弯矩方向的判断：**引起“下凸”的弯矩为正
{: .prompt-tip }

## 7-2 剪力图与弯矩图

![剪力图与弯矩图](/assets/img/posts/notes/machanics_of_materials/chapter7/shear_bending_moment_diagram.png){: .w-50 .right}

### 7-2-1 定义

以横坐标x表示梁的截面位置，纵坐标表示剪力和弯矩的数值

### 7-2-2 性质

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

### 7-4-1 纯弯曲和剪力弯曲的概念

**纯弯曲：** 梁的横截面上只有弯矩的弯曲

**剪力弯曲：** 梁的横截面上既有弯矩又有剪力的弯曲

### 7-4-2 静力平衡方程

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

### 7-4-3 几何方程

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

### 7-4-4 物理方程

$$
\sigma_x = E\varepsilon_x = -E\frac{y}{\rho}
$$

### 7-4-5 横截面上正应力公式

#### y轴和z轴的几何位置

$$
\iint_A -E\frac{y}{\rho}\,\mathrm{d}A
= -\frac{E}{\rho}\iint_A y\,\mathrm{d}A = 0
$$

$$
\iint_A y\, dA = 0
$$

由此可知，截面的中性轴$z$为截面的**形心轴**；由于$y$轴本身就是截面的对称轴，所以$y$轴也是**形心轴**

$$
\iint_A
\left(
-z\cdot E\frac{y}{\rho}
\right)dA
=
-\frac{E}{\rho}
\iint_A zy\, dA
=
0
$$

由此可知，$y$轴和$z$轴是**主轴**

综上，$y$轴和$z$轴是**形心主轴**

#### 纯弯曲梁变形公式

$$
\frac{E}{\rho}
\iint_A y^2\, dA
=
M_z
$$

$$
\frac{1}{\rho}
=
\frac{M_z}{EI_z}
$$

式子中$\frac{1}{\rho}$是中性层的曲率，即梁的轴线弯曲后的曲率，$EI_z$称为**抗弯刚度**

#### 横截面上正应力公式

$$
\sigma_x
=
-\frac{M_z}{I_z}y
$$

#### 最大弯曲正应力

$$
|\sigma_x|_{\max}
=
\frac{|M_z|}{I_z}|y|_{\max}
=
\frac{|M_z|}{W_z}
$$

其中$W_z=\frac{I_z}{\lvert y \lvert_{\max}}$称为**抗弯截面系数**

>对于矩形截面，$W_z=\frac{bh^2}{6}$；对于圆截面，$W_z=\frac{\pi D^3}{32}(1-\alpha^4)$
{: .prompt-info}

## 7-6 剪力弯曲切应力

### 7-6-1 矩形截面梁的弯曲切应力

![截面梁的弯曲切应力](assets/img/posts/notes/machanics_of_materials/chapter7/7-21.jpg)

![微段的力分析](assets/img/posts/notes/machanics_of_materials/chapter7/7-22.jpg)

$$
F_{x2}^{*}
=
\iint_{A^{*}} \sigma_{x2}\, dA
=
\iint_{A^{*}}
\frac{M_z+dM_z}{I_z}
y^{*}\, dA
=
\frac{M_z+dM_z}{I_z}
\iint_{A^{*}} y^{*}\, dA
=
\frac{M_z+dM_z}{I_z}S_z^{*}
$$

同理可得

$$
F_{x1}^*
=
\frac{M_z}{I_z}S_z^*
$$

由受力平衡可知

$$
F_{x1}^*-F_{x2}^*-dF_x'=0
$$

因为$dF_x'=\tau_{yx}b\mathrm{d}x$

$$
\tau_{yx}
=
-\frac{dM_z}{dx}
\frac{S_z^*}{bI_z}
=
\frac{F_{sy}S_z^*}{bI_z}
$$

由于$\frac{\mathrm{d} M_z}{\mathrm{d} x}=-F_{S_y}$，可得切应力的计算公式

$$
\tau_{xy}
=
\tau_{yx}
=
\frac{F_{sy}S_z^*}{bI_z}
$$

部分面积对中性轴的静矩为

$$
S_z^*
=
\int_{A^*} y\,dA
=
\int_y^{h/2} y' b\,dy'
=
\frac{b}{2}
\left(
\frac{h^2}{4}-y^2
\right)
$$

代入切应力计算公式

$$
\tau_{xy}
=
\frac{F_{sy}}{2I_z}
\left(
\frac{h^2}{4}-y^2
\right)
$$

切应力的最大值为

$$
\tau_{xy\max}
=
\frac{F_{sy}h^2}{8I_z}
=
\frac{3}{2}
\frac{F_{sy}}{bh}
$$

切应变为

$$
\gamma_{xy}
=
\frac{\tau_{xy}}{G}
=
\frac{F_{sy}}{2GI_z}
\left(
\frac{h^2}{4}-y^2
\right)
$$

### 7-6-2 工字形截面梁的弯曲切应力

![工字形截面梁](assets/img/posts/notes/machanics_of_materials/chapter7/7-25.jpg)

对于腹板，计算与矩形截面梁相同

$$
\tau_{xy}
=
\frac{F_{sy}S_z^*}{dI_z}
$$

对于翼缘，$y$方向上的切应力分量非常小，可以忽略不计

$$
\tau_{xz}
=
\frac{F_{sy}S_z^*}{\delta I_z}
$$

但是，$z$方向上的切应力分量与腹板上的比较也是次要的

>工字梁的腹板承担绝大部分的**剪力**，翼缘承担绝大部分的**弯矩**
{: .prompt-info}

### 7-6-3 圆形截面梁的弯曲切应力

![圆形截面梁](assets/img/posts/notes/machanics_of_materials/chapter7/7-26.jpg)

$$
\tau_{xy}
=
\frac{F_sS_z^*}{bI_z}
$$

最大切应力为平均切应力的$\frac{4}{3}$倍

$$
\tau_{xy\max}
=
\frac{4}{3}
\frac{F_s}{\pi R^2}
$$

### 7-6-4 环形截面梁的切应力

![环形截面梁](assets/img/posts/notes/machanics_of_materials/chapter7/7-27.jpg)

对于壁厚远小于平面半径的环形截面梁，可以认为切应力沿厚度均匀分布且与圆周相切

$$
\tau
=
\frac{F_sS_z^*}{2\delta I_z}
$$

$$
\tau_{xy\max}
=
\frac{F_{sy}}{\pi R\delta}
$$

>对于细长的实心截面梁或非薄壁截面梁，正应力是强度问题的主要考虑因素
{: .prompt-info}

## 7-8 梁的弹性弯曲变形

### 7-8-1 基本概念

**挠曲线：** 梁变形后的轴线，应该是一条光滑连续的平面曲线

**挠度：** 横截面形心沿垂直于轴线方向的位移，用$v$表示，**向上为正**

**转角：** 横截面绕中性轴转过的角度，用$\theta$表示，**逆时针为正**

$$
\tan\theta = \frac{dv}{dx}  = v'
$$

$$
\theta \approx \tan\theta = v'
$$

### 7-8-2 挠曲线与弯矩的关系

$$
\frac{1}{\rho(x)} = \frac{M(x)}{EI_z}
$$

$$
\frac{1}{\rho(x)}
=
\pm \frac{v''}{\left[1+(v')^2\right]^{\frac{3}{2}}}
=
\pm v''
$$

$$
EI v'' = \pm M(x)
$$

> 该公式适用于弹性范围内工作的细长梁
{: .prompt-info}

### 7-8-3 求挠曲线时的边界条件和连续条件

**固定端支座处：** 挠度和转角均为零

**固定铰支座处：** 挠度为零

**弯矩方程分段处：** 左右两截面的挠度和转角相等

### 7-8-4 叠加原理和叠加法求变形

**叠加原理：** 各载荷同时作用时的挠度和转角等于各载荷分别作用饰挠度和转角的代数和
