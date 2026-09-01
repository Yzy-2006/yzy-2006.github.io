---
title: 材料力学 第3章 应变状态分析
description: 材料力学第3章笔记
author: 阎梓瑜
date: 2026-06-12 13:00:00 +0800
categories: [材料力学]
tags: [材料力学]
pin: false
math: true
mermaid: true
---

## 3-1 应变的概念

![应变的概念](assets/img/posts/notes/machanics_of_materials/chapter3/3-1.png)

**线应变：**某一方向上单位长度的相对伸长或缩短 **（伸长为正，缩短为负）**

$$
\varepsilon_x
=\lim_{\Delta x\to 0}\frac{\Delta u}{\Delta x}
=\frac{\partial u}{\partial x}
$$

**切应变：**互相垂直的两条线段之间直角的改变量 **（使直角减小的切应变为正）**

$$
\gamma_{xy}
=
\lim_{\Delta x\to 0,\ \Delta y\to 0}
(\alpha+\beta)
=
\frac{\partial u}{\partial y}
+
\frac{\partial v}{\partial x}
$$

**体积应变：** 单位体积的体积改变

$$
\theta
=
\frac{V'-V}{V}
=
\varepsilon_1+\varepsilon_2+\varepsilon_3
=
\frac{\partial u}{\partial x}
+
\frac{\partial v}{\partial y}
+
\frac{\partial w}{\partial z}
$$

>$u$和$v$是单元体的位置，是和位置有关的函数
{: .prompt-info}

## 3-2 平面应变状态分析

### 3.2.1 斜方向应变

$$
\varepsilon_{x'}
=
\frac{\varepsilon_x+\varepsilon_y}{2}
+
\frac{\varepsilon_x-\varepsilon_y}{2}\cos 2\alpha
+
\frac{\gamma_{xy}}{2}\sin 2\alpha
$$

$$
\frac{\gamma_{x'y'}}{2}
=
-\frac{\varepsilon_x-\varepsilon_y}{2}\sin 2\alpha
+
\frac{\gamma_{xy}}{2}\cos 2\alpha
$$


### 3.2.2 主应变和主切应变

$$
\left.
\begin{aligned}
\varepsilon_{\max}\\
\varepsilon_{\min}
\end{aligned}
\right\}
=
\frac{\varepsilon_x+\varepsilon_y}{2}
\pm
\sqrt{
\left(
\frac{\varepsilon_x-\varepsilon_y}{2}
\right)^2
+
\left(
\frac{\gamma_{xy}}{2}
\right)^2
}
\quad
\qquad
\tan 2\alpha_{\varepsilon}
=
\frac{\gamma_{xy}}
{\varepsilon_x-\varepsilon_y}
$$

$$
\left.
\begin{aligned}
\frac{\gamma_{\max}}{2}\\
\frac{\gamma_{\min}}{2}
\end{aligned}
\right\}
=
\pm
\sqrt{
\left(
\frac{\varepsilon_x-\varepsilon_y}{2}
\right)^2
+
\left(
\frac{\gamma_{xy}}{2}
\right)^2
}
\quad
\qquad
\tan 2\alpha_{\gamma}
=
-\frac{\varepsilon_x-\varepsilon_y}
{\gamma_{xy}}
$$


>**为什么切应变要除2而切应力不用？**
>
>材料力学中使用的$\gamma_{xy}$是“工程切应变”，而应变张量中的实际切应变分量为$\frac{\gamma_{xy}}{2}$
{: .prompt-tip}

### 3.2.3 直角应变花公式

$$
\varepsilon_{x'}=\varepsilon_0
$$

$$
\varepsilon_{y'}=\varepsilon_{90}
$$

$$
\gamma_{x'y'}=2\varepsilon_{45}-\left(\varepsilon_0+\varepsilon_{90}\right)
$$
