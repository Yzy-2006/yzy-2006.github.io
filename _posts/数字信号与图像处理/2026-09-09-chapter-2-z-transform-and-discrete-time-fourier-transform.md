---
title: 第2章 z变换与离散时间傅里叶变换
description: 数字信号与图像处理第2章笔记
author: 阎梓瑜
date: 2026-09-09 20:00:00 +0800
categories: [数字信号与图像处理]
tags: [数字信号与图像处理]
pin: false
math: true
mermaid: true
---

## 一、序列的$z$变换

### 1.$z$变换的定义

$z$ 变换：

$$
X(z)=\mathcal{Z}[x(n)]=\sum_{n=-\infty}^{\infty}x(n)z^{-n}
$$

$z$ 逆变换：

$$
x(n)=\mathcal{Z}^{-1}[X(z)]
=\frac{1}{2\pi j}\oint_c X(z)z^{n-1}\,dz
$$

- $z$ 的定义域为复平面，保证幂级数收敛的取值范围为 $z$ 变换的收敛域，$z$ 为连续量，$n$ 为离散量。

- $c$ 为收敛域内任一围绕原点的逆时针方向的封闭曲线。

### 2.$z$变换的收敛域

- 定义：对任意给定序列 $x(n)$，使 $|X(z)|<\infty$ 成立的所有 $z$ 值的集合称为 $X(z)$ 的收敛域。

- 充要条件：绝对可和

$$
\sum_{n=-\infty}^{\infty}\left|x(n)z^{-n}\right|=M<\infty
$$

- 收敛域内不能有极点

>对于一个确定的时域序列 $x(n)$，其 $z$ 变换 $X(z)$ 由其**表达式**及**收敛域**共同确定
{: .prompt-info}

### 3.四种典型序列$z$变换的收敛域

#### 有限长序列

有限长序列对应的收敛域至少是除 $z=0$ 和 $z=\infty$ 外的 $z$ 平面，称为有限 $z$ 平面。

>有限长序列的 $z$ 变换只有有限项，所以一般不会像无限长序列那样因为无穷级数而发散；真正可能出问题的地方主要只有 $z=0$ 和 $z=\infty$。
{: ,prompt-info}

| 序列位置   | Z 变换中的幂     | ROC           |
| ---------- | ---------------- | ------------- |
| 全在 n > 0 | 只有 z⁻¹、z⁻²、… | 0 < \|z\| ≤ ∞ |
| 全在 n < 0 | 只有 z、z²、…    | 0 ≤ \|z\| < ∞ |
| 两边都有   | 同时有正幂和负幂 | 0 < \|z\| < ∞ |

#### 右边序列(无限长度)

右边序列是指从某个有限时刻 $n_1$ 开始可能非零，并一直向 $+\infty$ 延伸的序列：

$$
x(n)=0,\qquad n<n_1
$$

由于右边无限长序列中随着 $n$ 增大，会出现越来越高次的负幂：

$$
z^{-1},\quad z^{-2},\quad z^{-3},\ldots
$$

因此通常需要 $|z|$ 足够大，才能使级数收敛。所以右边序列的 ROC 位于最外层有限极点之外。

若所有有限极点为：

$$
p_1,p_2,\ldots,p_N
$$

定义：

$$
R=\max_i |p_i|
$$

则右边无限长序列的收敛域通常为：

$$
\boxed{
|z|>R
}
$$

其中 $R$ 为模值最大的有限极点对应的半径。收敛域不能包含极点，因此边界 $|z|=R$ 不属于 ROC。

因果序列满足：

$$
x(n)=0,\qquad n<0
$$

因此因果序列属于右边序列的一种特殊情况。此时 Z 变换中只含：

$$
z^0,\quad z^{-1},\quad z^{-2},\ldots
$$

而不含：

$$
z,\quad z^2,\quad z^3,\ldots
$$

当：

$$
|z|\rightarrow\infty
$$

有：

$$
z^{-1},z^{-2},\ldots\rightarrow0
$$

因此：

$$
X(z)\rightarrow x(0)
$$

为有限值，所以因果序列的 ROC 包含 $z=\infty$。

在通常讨论的 Z 变换情形下，可以记为：

$$
\boxed{
x(n)=0,\ n<0
\iff
z=\infty\text{ 属于 ROC}
}
$$

因此，对于因果有理序列：

$$
\boxed{
\text{ROC 位于最外层极点之外，并延伸至 }z=\infty
}
$$

#### 左边序列(无限长度)

左边序列是指在某个有限时刻 $n_2$ 之前可能非零，并一直向 $-\infty$ 延伸的序列：

$$
x(n)=0,\qquad n>n_2
$$


由于左边无限长序列中随着 $n$ 向负方向增大，会出现越来越高次的正幂：

$$
z,\quad z^2,\quad z^3,\ldots
$$

因此通常需要 $|z|$ 足够小，才能使级数收敛。所以左边序列的 ROC 位于最内层有限极点以内。

若所有有限极点为：

$$
p_1,p_2,\ldots,p_N
$$

定义：

$$
R=\min_i |p_i|
$$

则左边无限长序列的收敛域通常为：

$$
\boxed{
|z|<R
}
$$

其中 $R$ 为模值最小的有限极点对应的半径。收敛域不能包含极点，因此边界 $|z|=R$ 不属于 ROC。

反因果序列通常满足：

$$
x(n)=0,\qquad n>0
$$

因此反因果序列属于左边序列的一种特殊情况。此时 Z 变换中只含：

$$
z^0,\quad z,\quad z^2,\quad z^3,\ldots
$$

而不含：

$$
z^{-1},\quad z^{-2},\quad z^{-3},\ldots
$$

当：

$$
z\rightarrow0
$$

有：

$$
z,z^2,z^3,\ldots\rightarrow0
$$

因此：

$$
X(z)\rightarrow x(0)
$$

为有限值，所以反因果序列的 ROC 包含 $z=0$。

在通常讨论的 Z 变换情形下，可以记为：

$$
\boxed{
x(n)=0,\ n>0
\iff
z=0\text{ 属于 ROC}
}
$$

因此，对于反因果有理序列：

$$
\boxed{
\text{ROC 位于最内层极点以内，并延伸至 }z=0
}
$$

#### 双边序列(无限长度)


双边序列是指在某个范围内向 $+\infty$ 和 $-\infty$ 两个方向都无限延伸，并且两侧都可能存在非零样本的序列。

双边序列的 Z 变换必须同时满足两个条件，因此其收敛域通常为两个圆之间的环形区域：

$$
\boxed{
R_1<|z|<R_2
}
$$

其中：

- $R_1$ 对应内侧边界；
- $R_2$ 对应外侧边界；
- 必须满足 $R_1<R_2$，否则不存在公共收敛区域。

### 4.$z$逆变换的定义及求解

**定义：**给定序列 $x(n)$ 的对应的 $z$ 变换 $X(z)$ 的**表达式**及**收敛域**，求解原序列。

依照定义

$$
X(z)=\sum_{n=-\infty}^{\infty}x(n)z^{-n}
$$

$z$ 逆变换即求解 $X(z)$ 幂级数展开式的系数。

求解方法：
  - 闭合曲线积分法（留数法）
  - 部分分式法
  - 长除法（幂级数法）

#### 闭合曲线积分法

$$
x(n)
=
\frac{1}{2\pi j}\oint_c X(z)z^{n-1}\,dz
=
\sum_k \operatorname{Res}\left[X(z)z^{n-1}\right]_{z=z_k}
=
-\sum_m \operatorname{Res}\left[X(z)z^{n-1}\right]_{z=z_m}
$$

- 具体采用留数计算。
- $c$ 为收敛域内任一围绕原点的逆时针方向的封闭曲线。
- $\{z_k\}$ 和 $\{z_m\}$ 分别为被积函数在闭合曲线 $c$ 内部和外部的极点集，可根据情况灵活选用哪种方式。

留数计算公式(对应单阶极点)：

$$
\left.\operatorname{Res}\left[X(z)z^{n-1}\right]\right|_{z=z_r}
=
\left[(z-z_r)X(z)z^{n-1}\right]_{z=z_r}
$$

> 计算极点时要考虑0和无穷远处
{: .prompt-info}

#### 留数的概念

留数（Residue）是复变函数在某个极点附近与 $\frac{1}{z-z_r}$ 对应项的系数。在利用闭合曲线积分法求 Z 逆变换时，可通过留数定理将复杂的闭合曲线积分转化为对曲线内部各极点留数的求和。

若函数 $F(z)$ 在 $z=z_r$ 处存在单阶极点，则其留数为：

$$
\operatorname{Res}[F(z)]_{z=z_r}
=
\lim_{z\rightarrow z_r}
(z-z_r)F(z)
$$

对于 Z 逆变换：

$$
x(n)
=
\frac{1}{2\pi j}
\oint_C
X(z)z^{n-1}\,dz
$$

需要计算的实际是函数：

$$
F(z)=X(z)z^{n-1}
$$

在各极点处的留数。因此对于单阶极点 $z=z_r$，有：

$$
\operatorname{Res}
\left[
X(z)z^{n-1}
\right]_{z=z_r}
=
\lim_{z\rightarrow z_r}
(z-z_r)X(z)z^{n-1}
$$

实际计算时可以理解为：

1. 找到单阶极点 $z_r$；
2. 将函数乘以 $(z-z_r)$；
3. 约去导致极点的因子 $(z-z_r)$；
4. 再令 $z=z_r$，所得有限值即为该极点的留数。

对于逆 Z 变换，闭合曲线 $C$ 内各极点的留数之和即得到对应的序列值：

$$
x(n)
=
\sum_k
\operatorname{Res}
\left[
X(z)z^{n-1}
\right]_{z=z_k}
$$

因此可以将留数简单理解为：

$$
\boxed{
\text{留数是极点对闭合曲线积分所产生贡献的系数}
}
$$

#### 部分分式法

Z 变换可表达为有理分式，并分解为部分分式，如

$$
X(z)=\frac{B(z)}{A(z)}
= X_1(z)+X_2(z)+\cdots+X_k(z)
$$

则

$$
x(n)=\mathcal{Z}^{-1}\left[\frac{B(z)}{A(z)}\right]
$$

$$
=\mathcal{Z}^{-1}[X_1(z)]
+\mathcal{Z}^{-1}[X_2(z)]
+\cdots
+\mathcal{Z}^{-1}[X_k(z)]
$$

根据各项分别得到对应的时域表达式

---
- 解法1

$$
X(z)
=
\underbrace{\sum B_n z^{-n}}_{\text{多项式部分}}
+
\underbrace{\sum \frac{A_k}{1-z_kz^{-1}}}_{\text{单阶极点}}
+
\underbrace{\sum \frac{C_j}{(1-z_i z^{-1})^j}}_{\text{重极点}}
$$

它们分别对应：


$$
B_n z^{-n}
$$

对应移位冲激：

$$
\boxed{B_n\delta(n-n_0)}
$$

严格按索引写：

$$
B_k z^{-k}
\longleftrightarrow
B_k\delta(n-k)
$$

$$
\frac{A_k}{1-z_kz^{-1}}
$$

对应指数序列，例如右边情况：

$$
\boxed{A_k z_k^n u(n)}
$$

$$
\frac{C_j}{(1-z_i z^{-1})^j}
$$

对应：

> 指数序列乘一个关于 $n$ 的多项式。

例如右边 ROC 时：

$$
\boxed{
\frac{1}{(1-pz^{-1})^j}
\longleftrightarrow
\binom{n+j-1}{j-1}p^n u(n)
}
$$

例如 $j=1$：

$$
p^n u(n)
$$

$j=2$：

$$
(n+1)p^n u(n)
$$

$j=3$：

$$
\frac{(n+1)(n+2)}{2}p^n u(n)
$$

---

- 解法2

$X(z)$ 表达式采用 $z$ 的正幂级数

展开为部分分式形式

$$
\frac{X(z)}{z}
=
\frac{A_0}{z}
+
\sum_{k=1}^{N-r}\frac{A_k}{z-z_k}
+
\sum_{j=1}^{r}\frac{D_j}{(z-z_i)^j}
$$

系数可用留数法计算

$$
A_k
=
\left.
\operatorname{Res}
\left[
\frac{X(z)}{z}
\right]
\right|_{z=z_k}
=
\left.
(1-z_k z^{-1})X(z)
\right|_{z=z_k}
$$

$$
D_j
=
\frac{1}{(r-j)!}
\cdot
\frac{d^{\,r-j}}{dz^{\,r-j}}
\left[
(z-z_i)^r\frac{X(z)}{z}
\right]
\Bigg|_{z=z_k}
$$

---

#### 长除法

- 对于单边序列，首先根据收敛域确定按 $z^{-1}$ 的**升幂**还是**降幂**排列，然后再进行除法操作

- 通常不能得到 $x(n)$ 的整体显式表达式

- 不适合于直接求解双边序列，可将双边序列分解为两个单边序列操作

### 3.$z$变换的性质与定理

#### 线性

若

$$
\mathcal{Z}[x(n)] = X(z), \qquad R_{x-} < |z| < R_{x+}
$$

$$
\mathcal{Z}[y(n)] = Y(z), \qquad R_{y-} < |z| < R_{y+}
$$

则

$$
\mathcal{Z}[ax(n)+by(n)]
=
aX(z)+bY(z),
$$

$$
R_- < |z| < R_+
$$

其中

$$
R_-=\max(R_{x-},R_{y-}),
$$

$$
R_+=\min(R_{x+},R_{y+})
$$

收敛域为原收敛域的交集，如果出现零极点对消，收敛域有可能扩大

#### 序列的移位

- 双边 $z$ 变换的移位

$$
\mathcal{Z}[x(n-m)] = z^{-m}\cdot X(z)
$$

$$
\mathcal{Z}[x(n+m)] = z^{m}\cdot X(z)
$$

- 单边 $z$ 变换的定义：

$$
\mathcal{Z}^{+}[x(n)]
=
X^{+}(z)
=
\sum_{n=0}^{\infty}x(n)z^{-n}
$$

- 单边 $z$ 变换的移位

$$
\mathcal{Z}^{+}[x(n-m)]
=
z^{-m}
\left[
X^{+}(z)
+
\sum_{i=-m}^{-1}x(i)z^{-i}
\right]
$$

$$
\mathcal{Z}^{+}[x(n+m)]
=
z^{m}
\left[
X^{+}(z)
-
\sum_{i=0}^{m-1}x(i)z^{-i}
\right]
$$

> 单边主要是为了保持前后定义域的一致性
{: .prompt-info}

#### $z$域尺度变换性

若

$$
\mathcal{Z}[x(n)] = X(z), \qquad R_{x-} < |z| < R_{x+}
$$

则有

$$
\mathcal{Z}[a^n x(n)]
=
X\left(\frac{z}{a}\right),
\qquad
|a|R_{x-} < |z| < |a|R_{x+}
$$

其中非零常数 $a$ 为 $z$ 平面内的尺度变换因子或压缩 / 扩展因子。

#### 线性加权（$z$ 域求导）性

$$
\mathcal{Z}[n x(n)]
=
-z\cdot \frac{d}{dz}X(z),
\qquad
R_{x-}<|z|<R_{x+}
$$

#### 序列共轭性

$$
\mathcal{Z}[x^*(n)]
=
X^*(z^*),
\qquad
R_{x-}<|z|<R_{x+}
$$

#### 序列翻折性

$$
\mathcal{Z}[x(-n)]
=
X\left(\frac{1}{z}\right),
\qquad
\frac{1}{R_{x+}}<|z|<\frac{1}{R_{x-}}
$$

#### 初值定理

对于**因果序列** $x(n)$：

$$
\lim_{z\to\infty} X(z) = x(0)
$$

> $z \to \infty$ 时所有 $z^{-1}, z^{-2}, \ldots$ 都消失，只留下 $x(0)$
{: .prompt-info}

#### 终值定理

对于**因果序列** $x(n)$，且 $X(z)$ 的极点均位于单位圆以内（在单位圆上至多在 $z=1$ 处存在一阶极点）：

$$
\lim_{n\to\infty} x(n)
=
\lim_{z\to 1}\left[(z-1)X(z)\right]
$$

应用条件：

$$
\lim_{n\to\infty} x(n)=M<\infty
$$

>单位圆内的极点对应衰减项，$z=1$ 的单极点对应最终留下的常数项；只要没有增长或持续振荡的模式，终值就可以直接从 $X(z)$ 在 $z=1$ 附近的行为求出来
{: .prompt-info}

#### 因果序列的累加性

若对于因果序列 $x(n)$

$$
\mathcal{Z}[x(n)] = X(z),
\qquad
R_{x-} < |z|
$$

则有

$$
\mathcal{Z}
\left[
\sum_{m=0}^{n} x(m)
\right]
=
\frac{z}{z-1}X(z),
\qquad
\max(R_{x-},1)<|z|
$$

#### 时域卷积和定理

若

$$
y(n)=x(n)*h(n)
$$

$$
\mathcal{Z}[x(n)]=X(z),
\qquad
R_{x-}<|z|<R_{x+}
$$

$$
\mathcal{Z}[h(n)]=H(z),
\qquad
R_{h-}<|z|<R_{h+}
$$

则

$$
Y(z)=H(z)X(z),
\qquad
\max[R_{x-},R_{h-}]
<
|z|
<
\min[R_{x+},R_{h+}]
$$

#### $z$ 域复卷积定理

若

$$
y(n)=x(n)\cdot h(n)
$$

$$
\mathcal{Z}[x(n)]=X(z),
\qquad
R_{x-}<|z|<R_{x+}
$$

$$
\mathcal{Z}[h(n)]=H(z),
\qquad
R_{h-}<|z|<R_{h+}
$$

则

$$
Y(z)
=
\frac{1}{2\pi j}
\oint_C
X\left(\frac{z}{v}\right)
H(v)v^{-1}\,dv,
\qquad
R_{x-}R_{h-}
<
|z|
<
R_{x+}R_{h+}
$$

| 时域操作    | Z 域操作                  |
| ----------- | ------------------------- |
| $x(n)*h(n)$ | $X(z)H(z)$                |
| $x(n)h(n)$  | $X(z)$ 与 $H(z)$ 的复卷积 |


#### 帕塞瓦定理(不要求)

若

$$
\mathcal{Z}[x(n)] = X(z),
\qquad
R_{x-} < |z| < R_{x+}
$$

$$
\mathcal{Z}[h(n)] = H(z),
\qquad
R_{h-} < |z| < R_{h+}
$$

且

$$
R_{x-}R_{h-} < 1 < R_{x+}R_{h+}
$$

则

$$
\sum_{n=-\infty}^{\infty} x(n)h^*(n)
=
\frac{1}{2\pi j}
\oint_C
X(v)
H^*\left(\frac{1}{v^*}\right)
v^{-1}\,dv
$$

- $C$ 为 $X(v)$ 和 $H^*\left(\dfrac{1}{v^*}\right)$ 的公共收敛域内的闭合曲线

>Z 变换虽然改变了信号的表示方式，但并没有把这种“总的相关程度/能量信息”丢掉
{: .prompt-info}

### 4.利用$z$变换求解差分方程

利用 Z 变换求解差分方程的基本思想是：先将时域中的差分方程转换为 Z 域中的代数方程，求出 $Y(z)$ 后，再通过 Z 逆变换得到时域响应 $y(n)$。

线性常系数差分方程的一般形式为：

$$
\sum_{i=0}^{N} a_i y(n-i)
=
\sum_{m=0}^{M} b_m x(n-m)
$$

其中：

- $x(n)$：系统输入；
- $y(n)$：系统输出；
- $a_i,b_m$：常数系数；
- $N$：系统关于输出的阶数。

由于系统可能具有非零初始状态，因此通常采用**单边 Z 变换**。对于延迟序列，有：

$$
\mathcal Z^+[y(n-i)]
=
z^{-i}
\left[
Y^+(z)
+
\sum_{r=-i}^{-1}y(r)z^{-r}
\right]
$$

以及：

$$
\mathcal Z^+[x(n-m)]
=
z^{-m}
\left[
X^+(z)
+
\sum_{l=-m}^{-1}x(l)z^{-l}
\right]
$$

因此，对整个差分方程进行单边 Z 变换可得：

$$
\sum_{i=0}^{N}
a_i z^{-i}
\left[
Y^+(z)
+
\sum_{r=-i}^{-1}y(r)z^{-r}
\right]
=
\sum_{m=0}^{M}
b_m z^{-m}
\left[
X^+(z)
+
\sum_{l=-m}^{-1}x(l)z^{-l}
\right]
$$

系统的总响应可以分解为：

$$
\boxed{
y(n)=y_{zi}(n)+y_{zs}(n)
}
$$

其中：

- $y_{zi}(n)$：零输入响应，由系统初始状态产生；
- $y_{zs}(n)$：零状态响应，由外部输入产生。

#### 零输入响应

当输入为零：

$$
x(n)=0
$$

但初始状态可以非零，此时：

$$
\sum_{i=0}^{N}
a_i z^{-i}
\left[
Y^+(z)
+
\sum_{r=-i}^{-1}y(r)z^{-r}
\right]
=0
$$

整理可得：

$$
Y^+(z)
=
-
\frac{
\displaystyle
\sum_{i=0}^{N}
a_i z^{-i}
\sum_{r=-i}^{-1}y(r)z^{-r}
}{
\displaystyle
\sum_{i=0}^{N}a_i z^{-i}
}
$$

因此零输入响应为：

$$
\boxed{
y_{zi}(n)
=
(\mathcal Z^+)^{-1}[Y^+(z)]
}
$$

零输入响应完全由初始条件：

$$
y(-1),y(-2),\ldots
$$

决定。

#### 零状态响应

当系统处于零初始状态：

$$
y(-1)=y(-2)=\cdots=y(-N)=0
$$

则差分方程在 Z 域中化为：

$$
\sum_{i=0}^{N}
a_i z^{-i}Y^+(z)
=
\sum_{m=0}^{M}
b_m z^{-m}
\left[
X^+(z)
+
\sum_{l=-m}^{-1}x(l)z^{-l}
\right]
$$

从而：

$$
Y^+(z)
=
\frac{
\displaystyle
\sum_{m=0}^{M}
b_m z^{-m}
\left[
X^+(z)
+
\sum_{l=-m}^{-1}x(l)z^{-l}
\right]
}{
\displaystyle
\sum_{i=0}^{N}a_i z^{-i}
}
$$

因此零状态响应为：

$$
\boxed{
y_{zs}(n)
=
(\mathcal Z^+)^{-1}[Y^+(z)]
}
$$

#### 零初始状态且输入为因果序列

若进一步有：

$$
x(n)=0,\qquad n<0
$$

则输入的负时间样本全部为零，单边 Z 变换中的修正项消失：

$$
\sum_{l=-m}^{-1}x(l)z^{-l}=0
$$

于是：

$$
\sum_{i=0}^{N}a_i z^{-i}Y(z)
=
\sum_{m=0}^{M}b_m z^{-m}X(z)
$$

得到：

$$
Y(z)
=
\frac{
\displaystyle\sum_{m=0}^{M}b_m z^{-m}
}{
\displaystyle\sum_{i=0}^{N}a_i z^{-i}
}
X(z)
$$

定义系统函数：

$$
\boxed{
H(z)
=
\frac{Y(z)}{X(z)}
=
\frac{
\displaystyle\sum_{m=0}^{M}b_m z^{-m}
}{
\displaystyle\sum_{i=0}^{N}a_i z^{-i}
}
}
$$

因此：

$$
\boxed{
Y(z)=H(z)X(z)
}
$$

系统的零状态响应为：

$$
\boxed{
y_{zs}(n)
=
\mathcal Z^{-1}[H(z)X(z)]
}
$$

最终系统总响应为：

$$
\boxed{
y(n)=y_{zi}(n)+y_{zs}(n)
}
$$

因此，利用 Z 变换求解差分方程的核心过程可以概括为：

$$
\boxed{
\text{差分方程}
\rightarrow
\text{单边 Z 变换}
\rightarrow
\text{代数方程}
\rightarrow
Y(z)
\rightarrow
\text{Z 逆变换}
\rightarrow
y(n)
}
$$

其中，单边 Z 变换的主要作用是将系统的初始条件自然带入 Z 域方程；在零初始状态且输入为因果序列时，关系可进一步简化为：

$$
\boxed{
Y(z)=H(z)X(z)
}
$$

### 5.关于差分方程阶次的补充说明

对于系统函数：

$$
H(z)=\frac{B(z)}{A(z)}
$$

若关于 $z$ 的分子阶数为 $M$，分母阶数为 $N$，则可实时实现的因果系统应满足：

$$
\boxed{
N\ge M
}
$$

其原因是：$z^{-1}$ 对应一个采样周期的延迟，可以利用已有的过去数据实现；而 $z$ 对应超前一个采样周期，需要未来输入，实时系统无法获得。因此当 $N\ge M$ 时，系统函数可以整理为只含 $z^{-1},z^{-2},\ldots$ 的形式，不需要使用未来输入，系统具有因果实时可实现性。

例如：

$$
y(n)-y(n-1)
=
x(n)+x(n-1)+x(n-2)
$$

只使用当前和过去的输入，因此是因果系统；而：

$$
y(n)-y(n-1)
=
x(n)+x(n+1)
$$

需要未来输入 $x(n+1)$，因此是非因果系统。

## 二、离散时间傅立叶变换(DTFT)

### 1.傅立叶级数

连续周期函数可分解为一系列相互正交的基函数加权组合

#### 复指数形式

$$
x(t)=\sum_{k=-\infty}^{\infty} c_k e^{jk\omega_0 t}
$$

其中系数

$$
c_k=\frac{1}{T_0}\int_{T_0}x(t)e^{-jk\omega_0 t}\,dt
$$

$T_0$ 为信号的周期，满足

$$
T_0=\frac{2\pi}{\omega_0}
$$

#### 三角形式

$$
x(t)=\frac{a_0}{2}+\sum_{k=1}^{\infty}\left[a_k\cos(k\omega_0t)+b_k\sin(k\omega_0t)\right]
$$

其中系数

$$
a_0=\frac{2}{T_0}\int_{-T_0/2}^{T_0/2}x(t)\,dt
$$

$$
a_k=\frac{1}{T_0}\int_{-T_0/2}^{T_0/2}x(t)\cos(k\omega_0t)\,dt
$$

$$
b_k=\frac{1}{T_0}\int_{-T_0/2}^{T_0/2}x(t)\sin(k\omega_0t)\,dt
$$

> 二者可以通过$\cos\theta=\frac{e^{j\theta}+e^{-j\theta}}{2}$和$\sin\theta=\frac{e^{j\theta}-e^{-j\theta}}{2j}$相互转化
{: .prompt-info}

### 2.傅里叶变换

**核心思想:** 将非周期函数视为一个周期为无限长的周期函
数,于是频率无限小，求和转为积分

$$
x(t)=\mathcal{F}^{-1}[X(\omega)]
=\frac{1}{2\pi}\int_{-\infty}^{\infty}X(\omega)e^{j\omega t}\,d\omega
$$

$$
X(\omega)=\mathcal{F}[x(t)]=\int_{-\infty}^{\infty}x(t)e^{-j\omega t}\,dt
$$

### 3.离散时间傅立叶变换(DTFT)

#### 离散时间傅立叶变换的定义

离散时间傅立叶变换是$z$变换在复平面内单位圆上的特例，其中$z=e^{j\omega}$

$$
x(n)=\operatorname{IDTFT}[X(e^{j\omega})]
=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\omega})e^{j\omega n}\,d\omega
$$

$$
X(e^{j\omega})=\operatorname{DTFT}[x(n)]
=\sum_{n=-\infty}^{\infty}x(n)e^{-j\omega n}
$$

其中$\omega$ 为连续实变量，$n$ 为离散量

#### 离散时间傅立叶变换的收敛性

**概念：** 对应 $z$ 变换的收敛域包括复平面内的单位圆

**充分条件：一致收敛**

$$
\begin{aligned}
|X(e^{j\omega})|
&= \left|\sum_{n=-\infty}^{\infty}x(n)e^{-j\omega n}\right| \\
&\leq \sum_{n=-\infty}^{\infty}|x(n)|\cdot|e^{-j\omega n}| \\
&\leq \sum_{n=-\infty}^{\infty}|x(n)| < \infty
\end{aligned}
$$

**意义**

$$
\lim_{N\to\infty}
\left|
X(e^{j\omega})
-
\sum_{n=-N}^{N}x(n)e^{-j\omega n}
\right|
=0
$$

> 加入越来越多的 $x(n)$ 项后，频谱近似越来越准确
{: .prompt-info}

**充分条件：均方收敛**

$$
\sum_{n=-\infty}^{\infty}|x(n)|^2<\infty
$$

> 均方收敛相较于一致收敛要求更弱
{: ,prompt-info}

**意义**

$$
\lim_{N\to\infty}
\frac{1}{2\pi}
\int_{-\pi}^{\pi}
\left|
X(e^{j\omega})
-
\sum_{n=-N}^{N}x(n)e^{-j\omega n}
\right|^2
d\omega
=0
$$

>把整个频率区间里的“平方误差”取平均以后，误差趋近于 0
{: .prompt-info}

#### 吉布斯现象

当原信号在某处突然跳变时，傅里叶级数的有限项近似会在跳变点附近出现明显的振荡和过冲；即使增加更多谐波，这个过冲也不会完全消失，只会越来越集中在跳变点附近。

![](assets/img/posts/notes/digital_signal_and_image_processing/1.png)

#### 离散时间傅立叶变换的主要性质

- **线性**

$$
\mathrm{DTFT}\left[a x_1(n)+b x_2(n)\right]
=
aX_1\left(e^{j\omega}\right)
+
bX_2\left(e^{j\omega}\right)
$$

- **序列移位**

$$
\mathrm{DTFT}\left[x(n-m)\right]
=
e^{-j\omega m}X\left(e^{j\omega}\right)
$$

- **乘以指数序列**

$$
\mathrm{DTFT}\left[a^n x(n)\right]
=
X\left(\frac{1}{a}e^{j\omega}\right)
$$

- **乘以复指数序列（调制性）**

$$
\mathrm{DTFT}\left[e^{j\omega_0 n}x(n)\right]
=
X\left(e^{j(\omega-\omega_0)}\right)
$$

- **线性加权序列**

$$
\mathrm{DTFT}\left[nx(n)\right]
=
j\frac{\mathrm{d}}{\mathrm{d}\omega}
\left[
X\left(e^{j\omega}\right)
\right]
$$

- **序列共轭性**

$$
\mathrm{DTFT}\left[x^*(n)\right]
=
X^*\left(e^{-j\omega}\right)
$$

- **序列翻折**

$$
\mathrm{DTFT}\left[x(-n)\right]
=
X\left(e^{-j\omega}\right)
$$

- **时域卷积定理**

$$
\mathrm{DTFT}\left[x(n)*h(n)\right]
=
X\left(e^{j\omega}\right)
H\left(e^{j\omega}\right)
$$

> **时域卷积 ⇔ 频域相乘**

- **频域卷积定理**

$$
\mathrm{DTFT}\left[x(n)\cdot y(n)\right]
=
\frac{1}{2\pi}
\left[
X\left(e^{j\omega}\right)
*
Y\left(e^{j\omega}\right)
\right]
$$

即

$$
\mathrm{DTFT}\left[x(n)\cdot y(n)\right]
=
\frac{1}{2\pi}
\int_{-\pi}^{\pi}
X\left(e^{j\theta}\right)
Y\left(e^{j(\omega-\theta)}\right)
\,\mathrm{d}\theta
$$

> **时域相乘 ⇔ 频域周期卷积**

- **帕塞瓦定理**

$$
\sum_{n=-\infty}^{\infty}x(n)y(n)
=
\frac{1}{2\pi}
\int_{-\pi}^{\pi}
X\left(e^{j\omega}\right)
Y\left(e^{-j\omega}\right)
\,\mathrm{d}\omega
$$

特别地：

$$
\sum_{n=-\infty}^{\infty}|x(n)|^2
=
\frac{1}{2\pi}
\int_{-\pi}^{\pi}
\left|X\left(e^{j\omega}\right)\right|^2
\,\mathrm{d}\omega
$$

其意义为：

> **同一信号序列的总能量，在时域与频域中的表达始终相等。**

### 4.序列及其傅立叶变换的一些对称性质

**实序列可分解为奇对称序列和偶对称序列之和**

$$
x(n)=x_e(n)+x_o(n)
$$

二者分别满足：

$$
x_e(n)=x_e(-n)
$$

$$
x_o(n)=-x_o(-n)
$$

**序列的傅立叶变换同样可分解为共轭对称分量和共轭反对称分量之和**

$$
X\left(e^{j\omega}\right)
=
X_e\left(e^{j\omega}\right)
+
X_o\left(e^{j\omega}\right)
$$

**各种分量对应关系**

$$
x(n)
=
\operatorname{Re}[x(n)]
+
j\operatorname{Im}[x(n)]
$$

对应关系为：

$$
\begin{aligned}
x(n)
&\longleftrightarrow
X\left(e^{j\omega}\right) \\[4pt]
\operatorname{Re}[x(n)]
&\longleftrightarrow
X_e\left(e^{j\omega}\right) \\[4pt]
j\operatorname{Im}[x(n)]
&\longleftrightarrow
X_o\left(e^{j\omega}\right)
\end{aligned}
$$

以及：

$$
x(n)
=
x_e(n)
+
x_o(n)
$$

对应关系为：

$$
\begin{aligned}
x(n)
&\longleftrightarrow
X\left(e^{j\omega}\right) \\[4pt]
x_e(n)
&\longleftrightarrow
\operatorname{Re}\left[X\left(e^{j\omega}\right)\right] \\[4pt]
x_o(n)
&\longleftrightarrow
j\operatorname{Im}\left[X\left(e^{j\omega}\right)\right]
\end{aligned}
$$

### 5.周期序列的傅立叶变换

**周期为 $N$ 的单位采样序列**

$$
x(n)
=
\sum_{i=-\infty}^{\infty}
\delta(n-iN)
$$

对应傅立叶变换：

$$
X\left(e^{j\omega}\right)
=
\frac{2\pi}{N}
\sum_{i=-\infty}^{\infty}
\delta\left(
\omega-\frac{2\pi}{N}i
\right)
$$

**周期为 $N$ 的通用周期序列**

$$
\tilde{x}(n)
=
x(n)
*
\sum_{i=-\infty}^{\infty}
\delta(n-iN)
$$

对应傅立叶变换：

$$
\tilde{X}\left(e^{j\omega}\right)
=
\frac{2\pi}{N}
\sum_{i=-\infty}^{\infty}
X\left(
e^{j\frac{2\pi}{N}i}
\right)
\delta\left(
\omega-\frac{2\pi}{N}i
\right)
$$

## 三、$s$平面到$z$平面的映射

### 1.拉普拉斯变换

- **正变换**

$$
X(s)
=
\mathcal{L}[x(t)]
=
\int_{0}^{\infty}
x(t)e^{-st}\,\mathrm{d}t
$$

- **逆变换**

$$
x(t)
=
\mathcal{L}^{-1}[X(s)]
=
\frac{1}{2\pi i}
\lim_{T\to\infty}
\int_{\gamma-iT}^{\gamma+iT}
e^{st}X(s)\,\mathrm{d}s
$$

其中，$x(t)$ 为连续函数，$s=\sigma+j\omega$ 为复数，$\sigma$ 为衰减因子。

与傅立叶变换相比，拉普拉斯变换增加了衰减因子。

## 四、LSI系统的频域表征 

### 1.LSI系统的描述方法

- **单位采样响应（时域）**

$$
h(n)=\mathcal{T}[\delta(n)]
$$

- **常系数差分方程（时域）**

$$
y(n)
=
\sum_{m=0}^{M} b_m x(n-m)
-
\sum_{k=1}^{N} a_k y(n-k)
$$

- **系统函数（z 域）**

$$
H(z)
=
\mathcal{Z}[h(n)]
=
\frac{Y(z)}{X(z)}
$$

- **频率响应（频域）**

$$
H\left(e^{j\omega}\right)
=
\frac{Y\left(e^{j\omega}\right)}
{X\left(e^{j\omega}\right)}
=
\frac{
\displaystyle \sum_{m=0}^{M} b_m e^{-j\omega m}
}{
\displaystyle 1+\sum_{k=1}^{N} a_k e^{-j\omega k}
}
$$

### 2.LSI系统的频率响应

**当输入为复指数序列**

$$
x(n)=e^{j\omega n},\qquad -\infty<n<\infty
$$

**则输出为**

$$
y(n)
=
H\left(e^{j\omega}\right)e^{j\omega n}
$$

**频率响应即为 $h(n)$ 的离散时间傅立叶变换**

$$
H\left(e^{j\omega}\right)
=
\sum_{n=-\infty}^{\infty}
h(n)e^{-j\omega n}
$$

### 3.LSI系统的频率响应特性

- 若 $h(n)$ 绝对可和，即系统稳定，则 $H\left(e^{j\omega}\right)$ 一定存在且连续。

- $H\left(e^{j\omega}\right)$ 具有周期性，周期为 $2\pi$。

- 一个周期内，$\omega=0$ 和 $\omega=2\pi$ 共同代表最低频率，$\omega=\pi$ 代表最高频率。

- 若输入为正弦序列，则稳态输出为同频的正弦序列，其幅值和相位受到系统频率响应的影响。