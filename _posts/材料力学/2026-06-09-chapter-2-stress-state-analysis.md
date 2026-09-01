---
title: 材料力学 第2章 应力状态分析
description: 材料力学第2章笔记
author: 阎梓瑜
date: 2026-06-09 21:30:00 +0800
categories: [材料力学]
tags: [材料力学]
pin: false
math: true
mermaid: true
---

## 2-1 应力状态

### 2.1.1 一点的应力状态

$$
\boldsymbol{\sigma}
=
\begin{bmatrix}
\sigma_x & \tau_{xy} & \tau_{xz} \\
\tau_{xy} & \sigma_y & \tau_{yz} \\
\tau_{xz} & \tau_{yz} & \sigma_z
\end{bmatrix}
$$

>$\tau_{ij}$的第一个下标为截面法线方向，第二个下标为应力分量方向
{: .prompt-info}

### 2.1.2 切应力互等定律

$$
\tau_{ij}=\tau_{ji}
$$

### 2.1.3 任意截面的应力公式

$$
\begin{cases}
\sigma_{x'}
=
\dfrac{\sigma_x+\sigma_y}{2}
+
\dfrac{\sigma_x-\sigma_y}{2}\cos 2\alpha
+
\tau_{xy}\sin 2\alpha, \\[8pt]
\tau_{x'y'}
=
-\dfrac{\sigma_x-\sigma_y}{2}\sin 2\alpha
+
\tau_{xy}\cos 2\alpha.
\end{cases}
$$

#### 推导过程

$$
\boldsymbol{\sigma}'
=
\boldsymbol{Q}\boldsymbol{\sigma}\boldsymbol{Q}^{\mathrm T}
$$

$$
\boldsymbol{Q}
=
\begin{bmatrix}
\cos\alpha & \sin\alpha \\
-\sin\alpha & \cos\alpha
\end{bmatrix}
$$

$$
\begin{bmatrix}
\sigma_{x'} & \tau_{x'y'} \\
\tau_{x'y'} & \sigma_{y'}
\end{bmatrix}
=
\begin{bmatrix}
\cos\alpha & \sin\alpha \\
-\sin\alpha & \cos\alpha
\end{bmatrix}
\begin{bmatrix}
\sigma_x & \tau_{xy} \\
\tau_{xy} & \sigma_y
\end{bmatrix}
\begin{bmatrix}
\cos\alpha & -\sin\alpha \\
\sin\alpha & \cos\alpha
\end{bmatrix}
$$

### 2.1.4 主应力和主平面

$$
\frac{\mathrm{d}\sigma_{x'}}{\mathrm{d}\alpha}
=
2\left(
-\frac{\sigma_x-\sigma_y}{2}\sin 2\alpha
+
\tau_{xy}\cos 2\alpha
\right)
=0
$$

可得**正应力取得极值时切应力为0**

切应力为零的平面是**主平面**，主平面的外法线方向为**主方向**，主方向上的正应力称为**主应力**

$$
\left.
\begin{array}{c}
\sigma_{\max} \\[6pt]
\sigma_{\min}
\end{array}
\right\}
=
\frac{\sigma_x+\sigma_y}{2}
\pm
\sqrt{
\left(
\frac{\sigma_x-\sigma_y}{2}
\right)^2
+
\tau_{xy}^{\,2}
}
$$

$$
\tan 2\alpha_{\sigma}
=
\frac{2\tau_{xy}}{\sigma_x-\sigma_y}
\quad\Longrightarrow\quad
\left\{
\begin{array}{c}
\alpha_{\sigma} \\[6pt]
\alpha_{\sigma}+90^\circ
\end{array}
\right.
$$

### 2.1.5 主切应力和主切平面

$$
\left.
\begin{array}{c}
\tau' \\[6pt]
\tau''
\end{array}
\right\}
=
\pm
\sqrt{
\left(
\frac{\sigma_x-\sigma_y}{2}
\right)^2
+
\tau_{xy}^{\,2}
}
$$

$$
\sigma'
=
\frac{\sigma_x+\sigma_y}{2}
$$

$$
\tan 2\alpha_{\tau}
=
-\frac{\sigma_x-\sigma_y}{2\tau_{xy}}
\quad\Longrightarrow\quad
\left\{
\begin{array}{c}
\alpha_{\tau} \\[6pt]
\alpha_{\tau}+90^\circ
\end{array}
\right.
$$

## 2-2 扩展知识

### 2.2.1 主应力和正应力关系

$$
\sigma_{\max}+\sigma_{\min}
=
\sigma_x+\sigma_y
$$

### 2.2.2 主应力和主切应力关系

$$
\left.
\begin{array}{c}
\tau' \\[6pt]
\tau''
\end{array}
\right\}
=
\pm\frac{1}{2}
\left(
\sigma_{\max}-\sigma_{\min}
\right)
$$

### 2.2.3 y方向上的正应力

$$
\sigma_{y'}
=
\frac{\sigma_x+\sigma_y}{2}
-
\frac{\sigma_x-\sigma_y}{2}\cos 2\alpha
-
\tau_{xy}\sin 2\alpha
$$

>其实我觉得直接代入$\alpha+\frac{\pi}{2}$即可
{: .prompt-tip}

### 2.2.4 主应力方位角的判断方法

$$
\sigma_x>\sigma_y,
\qquad
\alpha\text{ 即为主方位角 }\alpha_{\sigma}
$$
