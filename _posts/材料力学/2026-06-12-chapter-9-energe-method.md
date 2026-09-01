---
title: 材料力学 第9章 能量原理
description: 材料力学第9章笔记
author: 阎梓瑜
date: 2026-06-12 16:00:00 +0800
categories: [材料力学]
tags: [材料力学]
pin: false
math: true
mermaid: true
---

## 9-1 莫尔积分

### 9.1.1 莫尔积分的公式

$$
1\cdot\Delta
=
\int_{0}^{l}
\left(
\frac{\overline{F}_{N}F_{N}}{EA}
+
\frac{k\overline{F}_{s}F_{s}}{GA}
+
\frac{\overline{T}T}{GI_{p}}
+
\frac{\overline{M}_{z}M_{z}}{EI}
\right)
\,\mathrm{d}x
$$

### 9.1.2 莫尔积分的图乘法

#### 推导过程

以弯矩为例，单位载荷的弯矩方程为直线或分段直线

$$
\overline{M}_z(x)=kx+b
$$

$$
\int_0^l M_z\overline{M}_z(x)\,\mathrm{d}x
=
\int_0^l M_z(kx+b)\,\mathrm{d}x
=
k\int_0^l xM_z\,\mathrm{d}x
+
b\int_0^l M_z\,\mathrm{d}x
=
kx_c\Omega_M+b\Omega_M
=
\Omega_M\overline{M_c}
$$

其中$\Omega_M$为图形的面积，$x_c$为图形形心的横坐标,$\overline{M_c}$为$x_c$处单位载荷作用下的弯矩值

#### 图乘法公式

莫尔积分的图乘法公式为

$$
\Delta
=
\frac{\Omega_M \overline{M}_c}{EI}
+
\frac{\Omega_{F_N}\overline{F}_{Nc}}{EA}
+
\frac{\Omega_T\overline{T}_c}{GI_p}
+
\frac{k\Omega_{F_s}\overline{F}_{Sc}}{GA}
$$

**注意事项**

1. 多个载荷共同作用时，要分别画图进行计算
2. 单位载荷内力图为折线时分段进行计算
3. 弯矩值位于基线同侧时结果为正，反之为负（弯矩画在受压一侧）
   
#### 常见图形的面积和形心

**三角形**

![三角形](assets/img/posts/notes/machanics_of_materials/chapter9/9-1.png){: .w-75 ,normal}

**二次抛物线**

![二次抛物线](assets/img/posts/notes/machanics_of_materials/chapter9/9-2.png){: .w-75 ,normal}

**三次抛物线**

![三次抛物线](assets/img/posts/notes/machanics_of_materials/chapter9/9-3.png){: .w-50 ,normal}


## 9-2 冲击

### 自由落体冲击

$$
k_d
=
\frac{\Delta_d}{\Delta_{\mathrm{st}}}
=
1+\sqrt{1+\frac{2h}{\Delta_{\mathrm{st}}}}
$$

$$
F_d=k_dQ
$$

$$
\sigma_d=k_d\sigma_{\mathrm{st}}
$$

### 水平冲击

$$
k_d=V\sqrt{\frac{1}{g\Delta_{\mathrm{st}}}}
$$

$$
\Delta_d=k_d\Delta_{\mathrm{st}}
$$

$$
F_d=k_dmg
$$

$$
\sigma_d=k_d\sigma_{\mathrm{st}}
$$
