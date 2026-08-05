---
title: 机器学习 第四章 无监督模型
description: 机器学习第4章笔记
author: 阎梓瑜
date: 2026-07-31 21:30:00 +0800
categories: [笔记,机器学习]
tags: [机器学习]
pin: false
math: true
mermaid: true
---

**无监督学习：**指在没有人工标签的情况下，让模型自动从数据中发现隐藏结构、规律或分组的一类机器学习方法。

## 一、k均值聚类

### 1. k均值聚类算法

**核心思想:** 先随机选择 K 个聚类中心，然后把每个样本分配给距离它最近的中心，接着重新计算每一类样本的平均值作为新的中心，重复这个过程，直到聚类中心基本不再变化。

将所有样本到对应中心的距离之和作为损失函数，可以写为：

$$
\mathcal{L}(C_1,\cdots,C_K)
=
\sum_{i=1}^{K}
\sum_{x\in C_i}
d(x,\mu_i)
=
\sum_{i=1}^{K}
\sum_{j=1}^{M}
\mathbb{I}(x_j\in C_i)d(x_j,\mu_i)
$$

$$
\frac{\partial \mathcal{L}}{\partial \mu_i}
=
\sum_{x\in C_i}
\frac{\partial d(x,\mu_i)}{\partial \mu_i}
$$

如果使用欧氏距离的平方作为度量标准，即：

$$
d(x,\mu_i)=\|x-\mu_i\|^2
$$

则有：

$$
\frac{\partial \mathcal{L}}{\partial \mu_i}
=
\sum_{x\in C_i}
\frac{\partial \|x-\mu_i\|^2}{\partial \mu_i}
=
2\sum_{x\in C_i}(\mu_i-x)
=
2|C_i|\mu_i
-
2\sum_{x\in C_i}x
$$

令偏导数为 0，可以得到最优的簇中心：

$$
\mu_i
=
\frac{1}{|C_i|}
\sum_{x\in C_i}
x
$$

因此，K 均值算法中每个簇的新中心就是该簇内所有样本的平均值

### 2. k-means++算法

**核心思想：** 第一个中心随机选，后面的中心尽量选择离已有中心较远的样本点

$$
P(\mu_{k+1}=x)
=
\frac{D^2(x)}
{\sum_x D^2(x)}
$$

## 二、主成分分析(PCA)

### 1. 主成分与方差

对于高维的复杂数据来说，我们希望能从中提取出有代表性，能最大限度保留数据本身信息的几个特征，从而降低数据维度，这一过程称为**数据降维**。数据降维中的经典算法即为**主成分分析**

PCA算法希望变换后的数据相互独立，因此在计算主成分时，会保证每个主成分与之前所有的主成分都是正交的。同时，我们还希望选出的主成分保留最多的信息，应当不断选择数据方差最大的方向作为主成分

为了方便计算，我们通常会对数据进行中心化

$$
\mu_j
=
\frac{1}{m}
\sum_{i=1}^{m}
x_i^{(j)},
\quad
j=1,\cdots,d
$$

$$
x_i^{(j)}
\leftarrow
x_i^{(j)}-\mu_j,
\quad
i=1,\cdots,m
$$

### 2. 利用特征分解进行PCA

为了找到方差最大的方向，我们先计算样本在某个方向上的投影。设 $\mathbf{u}$ 为方向向量，满足 $\|\mathbf{u}\|=1$，向量 $\mathbf{x}$ 在方向 $\mathbf{u}$ 上的投影为：

$$
\mathbf{x}^{T}\mathbf{u}
$$

于是，所有样本在方向 $\mathbf{u}$ 上的方差为：

$$
\sigma_u
=
\frac{1}{m}
\sum_{i=1}^{m}
(\mathbf{x}_i^{T}\mathbf{u})^2
=
\frac{1}{m}
\sum_{i=1}^{m}
\mathbf{u}^{T}\mathbf{x}_i\mathbf{x}_i^{T}\mathbf{u}
=
\mathbf{u}^{T}
\left(
\frac{1}{m}
\sum_{i=1}^{m}
\mathbf{x}_i\mathbf{x}_i^{T}
\right)
\mathbf{u}

=
\mathbf{u}^{T}\Sigma \mathbf{u}
$$

其中，矩阵 $\Sigma$ 定义为：

$$
\Sigma
=
\frac{1}{m}
\sum_{i=1}^{m}
\mathbf{x}_i\mathbf{x}_i^{T}
\in \mathbb{R}^{d\times d}
$$

该矩阵称为样本的**协方差矩阵**。由于 $m$ 是常数，为了简化表达，下面可以省略因子 $\frac{1}{m}$。

因此，要找到使样本投影方差最大的方向，就等价于求解下面的优化问题：

$$
\max_{\mathbf{u}}
\mathbf{u}^{T}\Sigma \mathbf{u}
\quad
\text{s.t.}
\quad
\|\mathbf{u}\|=1
$$

由于协方差矩阵是实对称矩阵，所以可以进行如下所示的**矩阵的特征分解**

$$
\Sigma

=
(e_1,e_2,\cdots,e_d)
\begin{pmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_d
\end{pmatrix}
\begin{pmatrix}
e_1^{T} \\
e_2^{T} \\
\vdots \\
e_d^{T}
\end{pmatrix}

=
Q\Lambda Q^{T}
$$

并且由于由于协方差矩阵是**半正定矩阵**，所以它的所有特征值非负

如果我们要把 $d$ 维数据降到 $k$ 维，只需要计算 $\Sigma$ 最大的 $k$ 个特征值对应的特征向量即可。

设这 $k$ 个特征向量依次为：

$$
e_1,\cdots,e_k
$$

将它们组成矩阵：

$$
W=(e_1,\cdots,e_k)\in \mathbb{R}^{d\times k}
$$

原数据矩阵为：

$$
X=(x_1,\cdots,x_m)^T\in \mathbb{R}^{m\times d}
$$

那么降维后的数据为：

$$
\operatorname{PCA}(X)=XW
$$

## 三、概率图模型

**核心思想:** 用图结构描述变量之间的条件独立关系，从而把复杂的联合分布拆成若干个简单的局部概率模型

由依赖关系构成的概率图是有向图，称为**贝叶斯网络**，如果只知道两个特征之间相关，没有明确的依赖关系，可以用无向图来建模，称为**马尔可夫网络**

### 1. 贝叶斯网络

贝叶斯网络又称为**信念网络**

对于有 $K$ 个节点 $x_1,\cdots,x_K$ 的贝叶斯网络，记 $\rho(x)$ 为所有有边指向 $x$ 的节点，即 $x$ 在图上的父节点集，那么其联合概率分布为：

$$
p(x_1,\cdots,x_K)
=
\prod_{k=1}^{K}
p(x_k\mid \rho(x_k))
$$

#### 贝叶斯网络的三种依赖关系

| 结构类型 | 图结构                               | 含义              | 不观察中间节点时                     | 观察中间节点时                             | 典型例子             |
| ---- | --------------------------------- | --------------- | ---------------------------- | ----------------------------------- | ---------------- |
| 链式结构 | $ A \rightarrow B \rightarrow C $ | A 通过 B 间接影响 C   | A 和 C 一般相关：$ A \not\perp C $ | A 和 C 条件独立：$ A \perp C \mid B $     | 下雨 → 地面湿 → 路滑    |
| 分叉结构 | $ A \leftarrow B \rightarrow C $  | B 是 A 和 C 的共同原因 | A 和 C 一般相关：$ A \not\perp C $ | A 和 C 条件独立：$ A \perp C \mid B $     | 地面湿 ← 下雨 → 行人打伞  |
| 汇聚结构 | $ A \rightarrow B \leftarrow C $  | B 是 A 和 C 的共同结果 | A 和 C 一般独立：$ A \perp C $     | A 和 C 变得相关：$ A \not\perp C \mid B $ | 下雨 → 地面湿 ← 洒水车洒水 |

>链式结构和分叉结构中，观察中间节点会阻断依赖；汇聚结构中，观察中间节点会打开依赖
{: .prompt-info}

### 2. 最大后验估计

它的核心思想是：

**不仅要让参数很好地解释数据，还要让参数本身符合我们事先的假设。**

设模型参数为 $ \mathbf{w} $，观测数据为 $ X,\mathbf{y} $。最大后验估计的目标是寻找使后验概率最大的参数：

$$
\mathbf{w}_{MAP}
=
\arg\max_{\mathbf{w}}
p(\mathbf{w}\mid X,\mathbf{y})
$$

根据贝叶斯公式：

$$
p(\mathbf{w}\mid X,\mathbf{y})
=
\frac{
p(\mathbf{y}\mid X,\mathbf{w})p(\mathbf{w})
}{
p(\mathbf{y}\mid X)
}
$$

其中：

- $ p(\mathbf{w}\mid X,\mathbf{y}) $：后验概率，表示看到数据后参数 $ \mathbf{w} $ 的概率；
- $ p(\mathbf{y}\mid X,\mathbf{w}) $：似然函数，表示给定参数后，当前数据出现的概率；
- $ p(\mathbf{w}) $：先验分布，表示看到数据前对参数的假设；
- $ p(\mathbf{y}\mid X) $：归一化常数，与 $ \mathbf{w} $ 无关。

因为 $ p(\mathbf{y}\mid X) $ 和待优化参数 $ \mathbf{w} $ 无关，所以可以写成：

$$
\mathbf{w}_{MAP}
=
\arg\max_{\mathbf{w}}
p(\mathbf{y}\mid X,\mathbf{w})p(\mathbf{w})
$$

也就是：

$$
\text{最大后验}
=
\text{最大化似然}
\times
\text{先验}
$$

和最大似然估计相比，最大似然估计只考虑：

$$
\mathbf{w}_{MLE}
=
\arg\max_{\mathbf{w}}
p(\mathbf{y}\mid X,\mathbf{w})
$$

也就是只关心“哪个参数最能解释数据”。

而最大后验估计考虑的是：

$$
\mathbf{w}_{MAP}
=
\arg\max_{\mathbf{w}}
p(\mathbf{y}\mid X,\mathbf{w})p(\mathbf{w})
$$

也就是既关心“参数能否解释数据”，也关心“参数本身是否合理”。

例如在线性回归中，如果假设参数满足高斯先验：

$$
\mathbf{w}
\sim
\mathcal{N}(0,\alpha^2 I)
$$

这表示我们事先认为参数不应该太大，最好靠近 0。再假设标签服从高斯噪声模型：

$$
y_i
\sim
\mathcal{N}(\mathbf{w}^T\mathbf{x}_i,\sigma^2)
$$

那么通过最大后验估计，最后可以推出下面的优化目标：

$$
\min_{\mathbf{w}}
\sum_{i=1}^{N}
(y_i-\mathbf{w}^T\mathbf{x}_i)^2
+
\lambda\|\mathbf{w}\|^2
$$

这正是带 $ L_2 $ 正则化的线性回归，也就是岭回归。

所以可以这样理解：

**最大似然估计只相信数据；最大后验估计既相信数据，也加入了先验约束。**

一句话总结：**最大后验估计就是在已有数据的基础上，结合先验知识，寻找后验概率最大的参数。**

### 3. 马尔可夫网络

马尔可夫网络又被称为**马尔可夫随机场**

如果一张无向图中的节点两两相连，我们就称这些节点组成了一个**团**，定义不被其他团包含的团为**极大团**

整个网络的联合分布可以表示为

$$
p(\mathbf{x})
=
\frac{1}{Z}
\prod_c
\psi_c(\mathbf{x}_c)
$$

势函数$\psi(\mathbf{x})$用来描述一组变量取某种组合时的“相容程度”或“偏好程度”,如果某一组变量的取值更合理、更常见，那么势函数值就大,同时，势函数一般要求**非负**

如果势函数严格为正，可以将其转换为能量函数，从而将连乘转换为求和且能量函数没有形式上的限制

$$
p(\mathbf{x})
=
\frac{1}{Z}
\prod_{c}
\psi_c(\mathbf{x}_c)
=
\frac{1}{Z}
e^{-\sum_c E(\mathbf{x}_c)}
$$

## 四、EM算法(期望最大化算法)

**核心思想:** 当数据中有一些变量看不见时，EM 算法先根据当前参数估计这些隐变量，再利用估计出来的隐变量更新参数，如此反复迭代


**期望步骤（E-step）：** 固定各个参数，由数据集中的样本统计计算隐变量 $
z$ 的后验分布：

$$
p(z\mid X,\phi,\mu,\Sigma)
$$

**最大化步骤（M-step）：** 固定隐变量，最大化参数的对数似然：

$$
l(\phi,\mu,\Sigma)
$$

---

### EM 算法证明过程

EM 算法的证明主要说明两件事：

1. 为什么 E 步要计算隐变量的后验分布；
2. 为什么 EM 算法每次迭代都能保证似然函数不下降。

---

### 1. 从观测数据似然开始

设观测数据为：

$$
X=\{x_1,x_2,\cdots,x_N\}
$$

隐变量为：

$$
Z=\{z_1,z_2,\cdots,z_N\}
$$

模型参数为：

$$
\theta
$$

因为隐变量 $z_i$ 不可见，所以观测数据的对数似然为：

$$
l(\theta)
=
\log P(X\mid \theta)
$$

由于样本独立，有：

$$
l(\theta)
=
\log
\prod_{i=1}^{N}
P(x_i\mid \theta)
$$

利用对数运算性质，可以写成：

$$
l(\theta)
=
\sum_{i=1}^{N}
\log P(x_i\mid \theta)
$$

而每个样本 $x_i$ 的概率需要对所有可能的隐变量 $z_i$ 求和：

$$
P(x_i\mid \theta)
=
\sum_{z_i}
P(x_i,z_i\mid \theta)
$$

因此：

$$
l(\theta)
=
\sum_{i=1}^{N}
\log
\sum_{z_i}
P(x_i,z_i\mid \theta)
$$

这个式子的难点在于：

$$
\log
\sum_{z_i}
P(x_i,z_i\mid \theta)
$$

也就是对数里面有求和，直接最大化比较困难。

---

### 2. 如果隐变量已知，问题会简单很多

如果每个样本对应的隐变量 $z_i$ 已知，那么不需要再对 $z_i$ 求和，可以直接写成完整数据的对数似然：

$$
l(\theta)
=
\sum_{i=1}^{N}
\log P(x_i,z_i\mid \theta)
$$

根据联合概率分解，有：

$$
P(x_i,z_i\mid \theta)
=
P(x_i\mid z_i,\theta)P(z_i\mid \theta)
$$

所以：

$$
l(\theta)
=
\sum_{i=1}^{N}
\log P(x_i\mid z_i,\theta)
+
\sum_{i=1}^{N}
\log P(z_i\mid \theta)
$$

此时优化参数会比较容易。

但是实际问题中，隐变量 $z_i$ 是未知的，所以 EM 算法的核心思想是：

**先估计隐变量的分布，再利用这个估计结果更新参数。**

---

### 3. 引入 $q_i(z_i)$ 构造下界

设 $q_i(z_i)$ 是关于隐变量 $z_i$ 的一个分布，满足：

$$
\sum_{z_i}q_i(z_i)=1
$$

并且：

$$
q_i(z_i)\ge 0
$$

对原来的对数似然做变形：

$$
l(\theta)
=
\sum_{i=1}^{N}
\log
\sum_{z_i}
P(x_i,z_i\mid \theta)
$$

在求和内部同时乘除 $q_i(z_i)$，得到：

$$
l(\theta)
=
\sum_{i=1}^{N}
\log
\sum_{z_i}
q_i(z_i)
\frac{
P(x_i,z_i\mid \theta)
}{
q_i(z_i)
}
$$

这一步本质上没有改变原式，因为：

$$
q_i(z_i)
\frac{
P(x_i,z_i\mid \theta)
}{
q_i(z_i)
}
=
P(x_i,z_i\mid \theta)
$$

这样写的目的是把求和写成加权平均的形式，从而可以使用 Jensen 不等式。

---

### 4. 使用 Jensen 不等式得到下界

因为 $\log x$ 是凹函数，所以由 Jensen 不等式可得：

$$
\log
\sum_{z_i}
q_i(z_i)
\frac{
P(x_i,z_i\mid \theta)
}{
q_i(z_i)
}
\ge
\sum_{z_i}
q_i(z_i)
\log
\frac{
P(x_i,z_i\mid \theta)
}{
q_i(z_i)
}
$$

因此：

$$
l(\theta)
\ge
\sum_{i=1}^{N}
\sum_{z_i}
q_i(z_i)
\log
\frac{
P(x_i,z_i\mid \theta)
}{
q_i(z_i)
}
$$

记右侧为：

$$
J(\theta,q)
=
\sum_{i=1}^{N}
\sum_{z_i}
q_i(z_i)
\log
\frac{
P(x_i,z_i\mid \theta)
}{
q_i(z_i)
}
$$

于是有：

$$
l(\theta)\ge J(\theta,q)
$$

也就是说，$J(\theta,q)$ 是 $l(\theta)$ 的一个下界。

---

### 5. 为什么 E 步要计算后验分布

现在的问题是：如何选择 $q_i(z_i)$，才能让这个下界尽可能贴近真实的对数似然函数？

Jensen 不等式取等号的条件是：

$$
\frac{
P(x_i,z_i\mid \theta)
}{
q_i(z_i)
}
$$

对所有 $z_i$ 都为常数。

因此令：

$$
q_i(z_i)
=
\frac{1}{C}
P(x_i,z_i\mid \theta)
$$

其中 $C$ 是归一化常数。

因为 $q_i(z_i)$ 是概率分布，所以：

$$
\sum_{z_i}q_i(z_i)=1
$$

因此：

$$
C
=
\sum_{z_i}
P(x_i,z_i\mid \theta)
=
P(x_i\mid \theta)
$$

所以：

$$
q_i(z_i)
=
\frac{
P(x_i,z_i\mid \theta)
}{
P(x_i\mid \theta)
}
$$

根据条件概率公式：

$$
q_i(z_i)
=
P(z_i\mid x_i,\theta)
$$

这说明，为了让下界尽可能紧，应该令 $q_i(z_i)$ 等于当前参数下隐变量的后验分布。

因此，EM 算法的 E 步就是：

$$
q_i^{(t)}(z_i)
=
P(z_i\mid x_i,\theta^{(t)})
$$

---

### 6. M 步的含义

E 步确定 $q_i^{(t)}(z_i)$ 后，下界函数变为：

$$
J(\theta,q^{(t)})
=
\sum_{i=1}^{N}
\sum_{z_i}
q_i^{(t)}(z_i)
\log
\frac{
P(x_i,z_i\mid \theta)
}{
q_i^{(t)}(z_i)
}
$$

此时 $q_i^{(t)}(z_i)$ 已经固定，只有参数 $\theta$ 是变量。

所以 M 步就是最大化这个下界：

$$
\theta^{(t+1)}
=
\arg\max_{\theta}
J(\theta,q^{(t)})
$$

也就是说：

**E 步固定参数，估计隐变量分布；M 步固定隐变量分布，更新模型参数。**

---

### 7. EM 算法为什么能保证似然函数不下降

EM 算法的收敛性证明主要是说明：

$$
l(\theta^{(t+1)})
\ge
l(\theta^{(t)})
$$

也就是每次迭代后，对数似然函数不会下降。

首先，由 Jensen 不等式得到的下界关系可知，对于任意 $q$，都有：

$$
l(\theta)
\ge
J(\theta,q)
$$

因此：

$$
l(\theta^{(t+1)})
\ge
J(\theta^{(t+1)},q^{(t)})
$$

其次，M 步会最大化下界函数，所以有：

$$
J(\theta^{(t+1)},q^{(t)})
\ge
J(\theta^{(t)},q^{(t)})
$$

最后，由于 E 步选择的是：

$$
q_i^{(t)}(z_i)
=
P(z_i\mid x_i,\theta^{(t)})
$$

这个选择会使 Jensen 不等式在 $\theta^{(t)}$ 处取等号，因此：

$$
J(\theta^{(t)},q^{(t)})
=
l(\theta^{(t)})
$$

把上面三步连起来，得到：

$$
l(\theta^{(t+1)})
\ge
J(\theta^{(t+1)},q^{(t)})
\ge
J(\theta^{(t)},q^{(t)})
=
l(\theta^{(t)})
$$

所以：

$$
l(\theta^{(t+1)})
\ge
l(\theta^{(t)})
$$

这就证明了 EM 算法每次迭代都会使对数似然函数不下降。

---

### 8. 几何直观

可以把 $l(\theta)$ 看成真正想要优化的目标函数，但它直接优化很困难。

EM 算法每一轮做两件事：

1. E 步：在当前参数 $\theta^{(t)}$ 处，构造一个与 $l(\theta)$ 相切的下界；
2. M 步：最大化这个下界，得到新的参数 $\theta^{(t+1)}$。

由于下界始终不超过真实目标函数，并且在当前点与真实目标函数相等，所以只要 M 步提高了下界，真实的对数似然函数也不会下降。

---

### 9. EM 算法和坐标上升

定义下界函数：

$$
J(\theta,q)
=
\sum_{i=1}^{N}
\sum_{z_i}
q_i(z_i)
\log
\frac{
P(x_i,z_i\mid \theta)
}{
q_i(z_i)
}
$$

EM 算法可以看成对两个变量交替优化：

$$
\text{E 步：固定 } \theta,\ \text{优化 } q
$$

$$
\text{M 步：固定 } q,\ \text{优化 } \theta
$$

因此，EM 算法本质上也可以看作一种坐标上升算法。

---

### 10. 总结

EM 算法证明的核心逻辑是：

$$
l(\theta)
=
\sum_i
\log
\sum_{z_i}
P(x_i,z_i\mid \theta)
$$

直接优化困难，于是引入分布 $q_i(z_i)$，利用 Jensen 不等式构造下界：

$$
l(\theta)
\ge
J(\theta,q)
$$

为了让下界最紧，令：

$$
q_i(z_i)
=
P(z_i\mid x_i,\theta)
$$

这就是 E 步。

然后固定 $q$，最大化下界：

$$
\theta^{(t+1)}
=
\arg\max_{\theta}
J(\theta,q^{(t)})
$$

这就是 M 步。

最终得到：

$$
l(\theta^{(t+1)})
\ge
l(\theta^{(t)})
$$

因此，EM 算法可以保证每次迭代后对数似然函数不下降。

一句话总结：**EM 算法的证明本质是：利用 Jensen 不等式给难以直接优化的对数似然函数构造一个下界，然后交替让下界变紧、让下界变大，从而保证原始似然函数单调不下降。**

## 五、自编码器



自编码器（Autoencoder）是一种常用于无监督学习的神经网络模型。它的核心思想是：先把输入样本压缩成一个特征向量，再从这个特征向量尽可能恢复出原始样本。

整体结构可以写成：

$$
x \rightarrow z \rightarrow \tilde{x}
$$

其中，\(x\) 是原始输入样本，\(z\) 是编码后的特征向量，\(\tilde{x}\) 是解码器重构出的样本。

---

### 1. 编码器

设编码器表示的映射为 \(\phi\)，它把样本 \(x\) 转换为特征向量 \(z\)：

$$
z=\phi(x)
$$

以最简单的单层感知机为例，编码器可以表示为：

$$
\phi(x)=\sigma(W_{\phi}x+b_{\phi})
$$

其中，\(W_{\phi}\) 和 \(b_{\phi}\) 是网络参数，\(\sigma\) 是激活函数。

编码器的任务是将高维样本变换为低维特征，并且这些特征应该尽可能保留原始样本中的重要信息。

---

### 2. 为什么需要解码器

在监督学习中，神经网络可以根据样本标签计算损失，然后利用损失的梯度更新参数。

但是在无监督学习中，我们无法获得样本标签，因此很难直接评价编码器得到的特征质量，也很难构造训练损失。

为了解决这个问题，自编码器引入一个解码器 \(\psi\)，将特征 \(z\) 再映射回接近原始样本的输出 \(\tilde{x}\)：

$$
\tilde{x}=\psi(z)
$$

同样以单层感知机为例，解码器可以表示为：

$$
\tilde{x}
=
\psi(z)
=
\sigma(W_{\psi}z+b_{\psi})
$$

其中，\(W_{\psi}\) 和 \(b_{\psi}\) 是解码器的网络参数。

如果解码器可以根据特征 \(z\) 尽可能恢复出原始样本 \(x\)，就说明编码器得到的特征质量较高。

---

### 3. 重建损失

自编码器将重构样本 \(\tilde{x}\) 与原始样本 \(x\) 之间的差别作为特征质量的评价指标。

如果使用均方误差作为损失函数，则总损失可以写为：

$$
\mathcal{L}(\phi,\psi)
=
\frac{1}{2}
\sum_{i=1}^{N}
\|x_i-\tilde{x}_i\|^2
=
\frac{1}{2}
\sum_{i=1}^{N}
\|x_i-\psi(\phi(x_i))\|^2
$$

该损失又称为重建损失（reconstruction loss）。

由于 \(\psi\) 将编码映射回原空间，与编码器 \(\phi\) 的作用相反，因此我们希望最小化重建损失。通过重建损失的梯度，可以更新网络参数，这与监督学习的训练方式类似。

---

### 4. 自监督学习的含义

在自编码器中，训练时并不需要额外的人工标签，而是把输入样本本身作为监督信号：

$$
\text{输入：}x
\qquad
\text{目标输出：}x
$$

这种在无监督学习任务中，从数据本身构造监督信号进行学习的方法，称为**自监督学习（self-supervised learning）**。

需要注意的是，自监督学习中的监督信号来自样本自身，并没有引入额外标签，因此它仍然属于无监督学习的范畴。

---

### 5. 编码器和解码器的组合

将编码器和解码器组合起来，就得到了自编码器。

通常来说，自编码器的结构不一定复杂，简单的 MLP 就可以满足任务需求。若编码器包含 \(m\) 个隐层，对应的权重矩阵维度为：

$$
d\times h_1,\ h_1\times h_2,\ \cdots,\ h_m\times k
$$

其中，\(d\) 是输入维度，\(k\) 是编码后的特征维度。

一般会将解码器的隐含层大小依次设置为：

$$
h_m,\cdots,h_2,h_1
$$

与编码器相反。

不过，由于非线性激活函数的存在，编码过程和解码过程并不完全对称，二者的权重也并不相同。

---

### 6. 特征维度的设置

为了让自编码器真正学习到有效特征，通常会令编码后的特征维度小于原始输入维度：

$$
k<d
$$

这样模型不能简单地复制输入，而必须学习数据中更重要、更紧凑的表示。

---

### 7. 总结

自编码器的整体流程可以概括为：

$$
x
\overset{\phi}{\longrightarrow}
z
\overset{\psi}{\longrightarrow}
\tilde{x}
$$

其中，编码器 \(\phi\) 负责提取特征，解码器 \(\psi\) 负责根据特征重构样本。

自编码器通过最小化重建损失：

$$
\mathcal{L}(\phi,\psi)
=
\frac{1}{2}
\sum_{i=1}^{N}
\|x_i-\psi(\phi(x_i))\|^2
$$

来学习数据的低维表示。