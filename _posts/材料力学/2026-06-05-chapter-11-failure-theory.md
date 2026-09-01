---
title: 材料力学 第11章 材料失效及强度理论
description: 材料力学11章笔记
author: 阎梓瑜
date: 2026-06-05 18:00:00 +0800
categories: [材料力学]
tags: [材料力学]
pin: false
math: true
mermaid: true
---

## 11-1 材料的失效模式及强度理论概念

### 11.1.1 常用工程材料的失效模式

**屈服**与**断裂**是材料的两种基本失效模式
> 脆性断裂：断裂之前不发生塑性变形或塑性变形很小
> 韧性断裂：断裂在发生之前产生塑形变形

### 11.1.2 强度理论

**广义强度：** 构件或结构抵抗破坏的能力，与**材料属性、载荷类型、结构和构件尺寸**有关

**强度：** 当受一定类型的应力作用时，材料内某一点能承受的不致于破坏的最大“相当应力”，只与**材料属性、应力状态**有关，与**尺寸**无关

不管简单模型还是复杂模型均可获得危险点的三个主应力进而获得多种极限破坏值

$$
\varepsilon_1
=
\frac{1}{E}
\left[
\sigma_1-\nu(\sigma_2+\sigma_3)
\right]
$$

$$
\tau_{\max}
=
\frac{1}{2} 
\left(
\sigma_1-\sigma_3
\right)
$$

$$
e_f
=
\frac{1+\nu}{6E}
\left[
(\sigma_1-\sigma_2)^2
+
(\sigma_2-\sigma_3)^2
+
(\sigma_3-\sigma_1)^2
\right]
$$

## 11-2 关于断裂的强度理论

### 11.2.1 最大拉应力理论（第一强度理论）

只要最大拉应力$\sigma_1$达到材料单向拉伸试验脆断使得极限拉应力值$\sigma_{1u}$(即强度极限$\sigma_b$)

$$
\sigma_1=\sigma_{1u}=\sigma_b
$$

>适用于脆性材料拉伸断裂、存在压应力的脆断失效，不适用于剪断失效和三向压应力状态
{: .prompt-info}

### 11.2.2 最大拉应变理论（第二强度理论）

只要最大拉应变$\varepsilon_1$达到材料单向拉伸试验脆断时的极限应变值$\varepsilon_{1u}$,就发生脆断失效

$$
\varepsilon_1=\varepsilon_{1u}
$$

$$
\sigma_1-\nu(\sigma_2+\sigma_3)=\sigma_b
$$

>适用于脆性材料双向拉伸-压缩应力状态且压应力大于拉应力
{: .prompt-info}

### 11.2.3 相当应力

上边两种理论本质上是在用主应力的某一综合值与材料单向拉伸时的极限应力比较，这一综合值称为**相当应力**，用$\sigma_r$表示

$$
\sigma_{r1}=\sigma_1
$$

$$
\sigma_{r2}
=
\sigma_1-\nu(\sigma_2+\sigma_3)
$$ 

## 11-3 关于屈服的强度理论

### 11.3.1 最大切应力理论（第三强度理论）

$$
\sigma_{r3}
=
\sigma_1-\sigma_3
=
\sigma_s
$$

### 11.3.2 形变应变能理论（第四强度理论）

$$
\sigma_{r4}
=
\sqrt{
\frac{1}{2}
\left[
(\sigma_1-\sigma_2)^2
+
(\sigma_2-\sigma_3)^2
+
(\sigma_3-\sigma_1)^2
\right]
}
=
\sigma_s
$$

### 11.3.3 圆轴弯扭的扩展公式

#### 应力形式

$$
\sigma_{r3}
=
\sqrt{\sigma^2+4\tau^2}
\leq [\sigma]
$$

$$
\sigma_{r4}
=
\sqrt{\sigma^2+3\tau^2}
\leq [\sigma]
$$

#### 内力形式

$$
\sigma_{r3}
=
\frac{1}{W_z}
\sqrt{M^2+T^2}
\leq [\sigma]
$$

$$
\sigma_{r4}
=
\frac{1}{W_z}
\sqrt{M^2+0.75T^2}
\leq [\sigma]
$$

>内力形式偏心变形不适用，$W$是$W_z$
{: .prompt-info}

## 11-4 莫尔强度理论

**极限应力圆：** 材料失效时对应的应力圆

**极限曲线：** 极限应力圆的包络线

$$
\sigma_{r\mathrm{M}}
=
\sigma_1
-
\frac{\sigma_{tu}}{\sigma_{cu}}\sigma_3
=
\sigma_{tu}
$$

$\sigma_{tu}$为材料在单向拉伸时的极限应力，$\sigma_{cu}$为材料在单向压缩时的极限应力的绝对值
