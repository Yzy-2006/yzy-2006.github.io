---
title: 材料力学 第4章 应力-应变关系
description: 材料力学第4章笔记
author: 阎梓瑜
date: 2026-06-12 15:00:00 +0800
categories: [笔记,材料力学]
tags: [材料力学]
pin: false
math: true
mermaid: true
---

## 4-1 材料的力学性能

### 4.1.1 低碳钢的拉伸试验

![低碳钢的拉伸试验](assets/img/posts/notes/machanics_of_materials/chapter4/4-1.png){: .w-50 ,normal}



#### 第一阶段——弹性变形阶段（ob段）


**弹性极限**

$$
\sigma_e=\frac{F_e}{A}
$$

**比例极限**

$$
\sigma_p=\frac{F_p}{A}
$$


#### 第二阶段——屈服（流动）阶段（bc段）


**屈服点**

$$
\sigma_s=\frac{F_s}{A}
$$



#### 第三阶段——强化阶段（ce段）


**强度极限**

$$
\sigma_b=\frac{F_b}{A}
$$


#### 第四阶段——颈缩破坏阶段

#### 卸载定律

在强化阶段卸载时，应力与应变呈线性关系

**应用：** 冷作硬化使材料的比例极限提高，塑形变形减小

### 4.1.2 低碳钢的压缩试验

![低碳钢的压缩试验](assets/img/posts/notes/machanics_of_materials/chapter4/4-2.png){: .w-25 ,normal}

### 4.1.3 铸铁的拉伸试验

![铸铁的拉伸试验](assets/img/posts/notes/machanics_of_materials/chapter4/4-3.png){: .w-25 ,normal}


### 4.1.4 铸铁的压缩试验

![铸铁的压缩试验](assets/img/posts/notes/machanics_of_materials/chapter4/4-4.png){: .w-25 ,normal}


铸铁受压缩发生断裂时的断裂面与轴线夹角大约为$45^\circ$，表明铸铁受压断裂是最大切应力导致的

## 4-2 胡克定律

### 4.2.1 简单拉压胡克定律

$$
\sigma_x=E\varepsilon_x
$$

$$
\nu=-\frac{\varepsilon_y}{\varepsilon_x}
$$

其中$\nu$称为**泊松比**，是材料常数

### 4.2.2 简单剪切胡克定律

$$
\tau_{xy}=G\gamma_{xy}
$$

其中$G$称为材料的**切变模量**

### 4.2.3 广义拉压胡克定律

$$
\varepsilon_x
=
\frac{1}{E}
\left[
\sigma_x-\nu\left(\sigma_y+\sigma_z\right)
\right]
$$

**主应变与主应力次序的对应关系？**

$$
\sigma_x>\sigma_y>\sigma_z
\quad\Longleftrightarrow\quad
\varepsilon_x>\varepsilon_y>\varepsilon_z
$$

### 4.2.4 广义剪切胡克定律

$$
\gamma_{xy}=\frac{\tau{xy}}{G}
$$

### 4.2.5 体积胡克定律

$$
\theta
=
\varepsilon_1+\varepsilon_2+\varepsilon_3
=
\frac{1-2\nu}{E}
\left(
\sigma_1+\sigma_2+\sigma_3
\right)
=
\frac{3(1-2\nu)}{E}
\cdot
\frac{\sigma_1+\sigma_2+\sigma_3}{3}
=
\frac{\sigma_m}{K}
$$

其中，$K=\frac{E}{3(1-2\nu)}$为体积模量，$\sigma_m=\frac{\sigma_1+\sigma_2+\sigma_3}{3}=\frac{\sigma_x+\sigma_y+\sigma_z}{3}$为平均正应力

>**体积应变与形状变形的关系？**
>体积应变有单元体各面上平均应力引起，形状变形由应力偏移量引起

## 4-3 应变能

### 4.3.1 简单应力状态下的应变能

单位体积中的应变能称为**应变比能**或**应变能密度**

**纯拉压应变能密度**

$$
e=\frac{1}{2}\sigma_x\varepsilon_x
$$

**纯剪切应变能密度**

$$
e=\frac{1}{2}\tau_{xy}\gamma_{xy}
$$

### 4.3.2 空间应力状态下的应变能

总能量=体积改变比能+形状改变比能$\qquad e=e_v+e_f$

#### 总比能

在三向主应力作用下，应变能密度为

$$
e
=
\frac{1}{2}\left(\sigma_1\varepsilon_1+\sigma_2\varepsilon_2+\sigma_3\varepsilon_3\right)
=
\frac{1}{2E}
\left[
\sigma_1^2+\sigma_2^2+\sigma_3^2
-
2\nu
\left(
\sigma_1\sigma_2+\sigma_2\sigma_3+\sigma_3\sigma_1
\right)
\right]
$$

>因为是三向主应力状态所以不需要考虑切应力
{: .prompt-info}

#### 体积改变比能

$$
e_v
=
3\left(
\frac{1}{2}\sigma_m\varepsilon_m
\right)
=
\frac{\sigma_m^2}{2K}
=
\frac{3(1-2\nu)}{2E}
\left(
\frac{\sigma_1+\sigma_2+\sigma_3}{3}
\right)^2
=
\frac{1-2\nu}{6E}
\left(
\sigma_1+\sigma_2+\sigma_3
\right)^2
$$

#### 形状改变比能

$$
e_f=e-e_v
=
\frac{1+\nu}{6E}
\left[
(2\tau_{12})^2
+
(2\tau_{23})^2
+
(2\tau_{31})^2
\right]
$$

## 4-4 各向同性材料弹性常数之间的关系

$$
G=\frac{E}{2(1+\nu)}
$$