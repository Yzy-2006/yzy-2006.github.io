---
title: 材料力学 第16章 压杆稳定
description: 材料力学16章笔记
author: 阎梓瑜
date: 2026-06-09 19:50:00 +0800
categories: [材料力学]
tags: [材料力学]
pin: false
math: true
mermaid: true
---

## 16-1 细长压杆临界压力的欧拉公式

### 16.1.1 两端铰支细长压杆的临界力

![细长压杆](assets/img/posts/notes/machanics_of_materials/chapter16/16-1.png)

$$
\frac{\mathrm{d}^2v}{\mathrm{d}x^2}
=
\frac{M(x)}{EI}
=
-\frac{F_{\mathrm{cr}}v}{EI}
$$

令$K^2=\frac{F_{\mathrm{cr}}}{EI}$可得

$$
\frac{\mathrm{d}^2v}{\mathrm{d}x^2}+K^2v=0
$$

解得

$$
v=C_1\sin Kx+C_2\cos Kx
$$

代入边界条件（压杆两端挠度为0）

$$
K=\frac{n\pi}{l}
\qquad
(n=0,1,2,\cdots)
$$

从而得到

$$
F_{\mathrm{cr}}=\frac{n^2\pi^2EI}{l^2}
$$

$n=1$时的最小轴压即为**临界压力**

$$
F_{\mathrm{cr}}=\frac{\pi^2EI}{l^2}
$$

### 16.1.2 不同杆端约束细长压杆的临界力

一般情况下，压杆的临界力公式可以统一写成**欧拉公式的一般形式**

$$
F_{\mathrm{cr}}=\frac{\pi^2 EI}{(\mu l)^2}
$$

其中$\mu$为**长度系数**，和约束类型有关。$\mu l$称为压杆的**相当长度**

### 16.1.2 临界应力公式

$$
\sigma_{\mathrm{cr}}
=
\frac{F_{\mathrm{cr}}}{A}
=
\frac{\pi^2 EI}{(\mu l)^2A}
=
\frac{\pi^2 i^2 E}{(\mu l)^2}
=
\frac{\pi^2 E}{\lambda^2}
$$

其中$\lambda=\frac{\mu l}{i}$称为压杆的柔度

### 16.1.3 欧拉公式的适用范围

由于欧拉公式的推导建立在材料服从胡克定律的基础上，所以欧拉公式只有在临界压力不超过比例极限$\sigma_p$时适用

$$
\lambda_p=\pi\sqrt{\frac{E}{\sigma_p}}
$$

$\lambda \geq \lambda_p$ 的压杆定义为**细长杆**

## 16-2 中长杆的直线公式

### 16.2.1 直线公式

对于超过比例极限的非细长压杆

$$
\sigma_{\mathrm{cr}}=a-b\lambda
$$

定义屈服点对应的柔度值为$\lambda_s$

$$
\lambda_s=\frac{a-\sigma_s}{b}
$$

当$\lambda_s\leq\lambda\leq\lambda_p$时，直线公式成立

### 16.2.2 临界应力与柔度之间的关系

![临界应力与柔度的关系](assets/img/posts/notes/machanics_of_materials/chapter16/16-2.png)

## 16-3 压杆稳定性的计算

### 16.3.1 安全系数法

$$
F \leq \frac{F_{\mathrm{cr}}}{n_{\mathrm{st}}} = [F]_{\mathrm{st}}
$$

$$
n_{\mathrm{st}}=\frac{F_{\mathrm{cr}}}{F}\geq [n_{\mathrm{st}}]
$$

$$
\sigma \leq \frac{\sigma_{\mathrm{cr}}}{n_{\mathrm{st}}} = [\sigma]_{\mathrm{st}}
$$

### 16.3.2 折减系数法

$$
[\sigma]_{\mathrm{st}}=\varphi(\lambda)[\sigma]
$$
