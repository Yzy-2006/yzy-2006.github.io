---
title: 机器学习 第三章 非参数化模型
description: 机器学习第3章笔记
author: 阎梓瑜
date: 2026-07-28 17:00:00 +0800
categories: [机器学习, 非参数化模型]
tags: [机器学习]
pin: false
math: true
mermaid: true
---

## 一、支持向量机(SVM)

从无数个可以分割两个点集的超平面中挑选出一个平面，使其与任意一点间隔的最小值最大

### 1. 支持向量机的数学描述

$\hat{\gamma}_i=y_i\left(\mathbf{w}^T\mathbf{x}_i+b\right)$ 称为**函数间隔**,与函数参数的设计有关，将其归一化之后得到**几何间隔**$\gamma_i=\frac{\hat{\gamma}_i}{\|\mathbf{w}\|}$

令最近的点的函数间隔为1，可得支持向量机的优化目标(**即让最近的点的几何间隔最大**)为

$$
\max_{\mathbf{w}, b}
\frac{1}{\|\mathbf{w}\|}
$$

$$
\text{s.t.}
\quad
y_i
\left(
\mathbf{w}^T\mathbf{x}_i+b
\right)
\ge 1,
\quad
i=1,\cdots,m
$$

为了进一步简化，可以将优化目标写为

$$
\min_{\mathbf{w}, b}
\frac{1}{2}
\|\mathbf{w}\|^2
$$

$$
\text{s.t.}
\quad
y_i
\left(
\mathbf{w}^T\mathbf{x}_i+b
\right)
\ge 1,
\quad
i=1,\cdots,m
$$

但是，并不是所有数据都满足线性可分，所以我们引入松弛变量和惩罚系数

$$
\min_{\mathbf{w}, b, \xi_i}
\frac{1}{2}
\|\mathbf{w}\|^2
+
C
\sum_{i=1}^{m}
\xi_i
$$

$$
\text{s.t.}
\quad
y_i
\left(
\mathbf{w}^T\mathbf{x}_i+b
\right)
\ge
1-\xi_i
$$

$$
\xi_i \ge 0,
\quad
i=1,\cdots,m
$$

求解上式的凸优化问题等价于求解下面的二次规划

$$
\max_{\alpha} W(\alpha)
=
\max_{\alpha}
\left(
\sum_{i=1}^{m}\alpha_i
-
\frac{1}{2}
\sum_{i=1}^{m}
\sum_{j=1}^{m}
\alpha_i\alpha_j y_i y_j \mathbf{x}_i^T\mathbf{x}_j
\right)
$$

$$
\text{s.t.}
\quad
0 \le \alpha_i \le C,
\quad
i=1,\cdots,m
$$

$$
\sum_{i=1}^{m}
\alpha_i y_i
=
0
$$

当求解出最优参数$\alpha^*$之后，可以得到

$$
\mathbf{w}^*
=
\sum_{i=1}^{m}
\alpha_i^* y_i \mathbf{x}_i
$$

$$
b^*
=
-\frac{1}{2}
\left(
\max_{i,\,y_i=-1}
\mathbf{w}^{*T}\mathbf{x}_i
+
\min_{i,\,y_i=1}
\mathbf{w}^{*T}\mathbf{x}_i
\right)
$$

并且，这组参数满足

$$
\alpha_i^*
\left(
1-y_i
\left(
\mathbf{w}^{*T}\mathbf{x}_i+b^*\right)\right)=0
$$

可以推出,对于任意一个样本$x_i$,要么其对应的参数$\alpha_i^*=0$,要么$x_i$是所有样本中到超平面距离最小的，将这些$x_i$称为**支持向量**,在引入松弛变量后，对于那些类别与SVM的超平面相反的向量，由于$\alpha_i^* \ne 0$,所以这些也是**支持向量**

设支持向量的集合为$S$,上述的求和只需要在$S$中进行，所以用SVM预测的时间复杂度可以由$O(m) \text{ 变为 } O(|S|)$

### 2. SVM对偶问题的推导

对一般形式的凸优化问题

$$
\min_w f(w)
$$

$$
\text{s.t.}
\quad
g_i(w)\le 0,
\quad
i=1,\cdots,k
$$

$$
h_j(w)=0,
\quad
j=1,\cdots,l
$$

我们定义他的**拉格朗日函数**为

$$
\mathcal{L}(w,\alpha,\beta)
=
f(w)
+
\sum_{i=1}^{k}
\alpha_i g_i(w)
+
\sum_{i=1}^{l}
\beta_i h_i(w),
\quad
\alpha_i \ge 0
$$

由此，我们可以将原问题转化为

$$
\theta_P(w)
=
\max_{\alpha,\beta;\,\alpha_i\ge 0}
\mathcal{L}(w,\alpha,\beta)
=
\begin{cases}
f(w), & w\text{满足约束条件} \\
+\infty, & \text{其他情况}
\end{cases}
$$

所以我们可以将带约束问题转化为无约束问题

$$
\min_w \theta_P(w)
=
\min_w
\max_{\alpha,\beta;\,\alpha_i\ge 0}
\mathcal{L}(w,\alpha,\beta)
$$

记该问题的最优解为$p^*=\min_w\theta_P(w)$

原问题的对偶问题为

$$
\max_{\alpha,\beta;\,\alpha_i\ge 0}
\theta_D(\alpha,\beta)
=
\max_{\alpha,\beta;\,\alpha_i\ge 0}
\min_w
\mathcal{L}(w,\alpha,\beta)
$$

其中$\theta_D(\alpha,\beta)=\min_w\mathcal{L}(w,\alpha,\beta)$

记其最优值为$d^*=\max_{\alpha,\beta;\,\alpha_i\ge 0}\theta_D(\alpha,\beta)$，并且$d^* \le p^*$

在满足某些特殊条件的情况下，原问题和对偶问题的最优值是相等的，即：

$$
d^*=p^*
$$

对于一个凸优化问题，如果其约束条件可以被严格满足，即存在 $w$ 使得：

$$
g_i(w)<0
$$

且：

$$
h_i(w)=0
$$

那么必然存在 $w^*$、$\alpha^*$ 和 $\beta^*$，满足：

- $w^*$ 是原问题 $\min_w \theta_P(w)$ 的解；
- $\alpha^*$ 和 $\beta^*$ 是对偶问题 $\max_{\alpha,\beta;\alpha_i\ge 0}\theta_D(\alpha,\beta)$ 的解；
- 最优值满足：

$$
d^*=p^*=\mathcal{L}(w^*,\alpha^*,\beta^*)
$$

以及卡罗需—库恩—塔克条件，即 Karush-Kuhn-Tucker conditions，简称 **KKT 条件**。

KKT 条件包括：

- 稳定性：

$$
\nabla_w \mathcal{L}(w^*,\alpha^*,\beta^*)=0
$$

- 原问题满足性：

$$
g_i(w^*)\le 0
$$

$$
h_i(w^*)=0
$$

- 对偶问题满足性：

$$
\alpha_i^*\ge 0
$$

- 互补松弛性：

$$
\alpha_i^*g_i(w^*)=0
$$

反过来，如果某一组 $(w,\alpha,\beta)$ 满足 KKT 条件，那么它们也是原问题和对偶问题的解。

所以，对于满足KKT条件的凸优化问题，我们可以将其转化为凸优化问题进行求解

对于软间隔的SVM优化问题

$$
\mathcal{L}(\mathbf{w},b,\xi,\alpha,\mu)
=
\frac{1}{2}\|\mathbf{w}\|^2
+
C\sum_{i=1}^{m}\xi_i
+
\sum_{i=1}^{m}
\alpha_i
\left[
1-\xi_i-y_i(\mathbf{w}^T\mathbf{x}_i+b)
\right]
-
\sum_{i=1}^{m}
\mu_i\xi_i
$$

$$
\alpha_i\ge 0,
\quad
\mu_i\ge 0
$$

为了得到对偶问题，需要先对原变量 $\mathbf{w}$、$b$、$\xi_i$ 求最小值，因此分别令偏导数为 0。

对 $\mathbf{w}$ 求偏导：

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{w}}
=
\mathbf{w}
-
\sum_{i=1}^{m}
\alpha_i y_i\mathbf{x}_i
=
0
$$

因此：

$$
\mathbf{w}
=
\sum_{i=1}^{m}
\alpha_i y_i\mathbf{x}_i
$$

这说明最优分类超平面的法向量 $\mathbf{w}$ 可以表示为训练样本向量的线性组合。

对 $b$ 求偏导：

$$
\frac{\partial \mathcal{L}}{\partial b}
=
-
\sum_{i=1}^{m}
\alpha_i y_i
=
0
$$

因此：

$$
\sum_{i=1}^{m}
\alpha_i y_i
=
0
$$

这成为对偶问题中的等式约束。

对 $\xi_i$ 求偏导：

$$
\frac{\partial \mathcal{L}}{\partial \xi_i}
=
C-\alpha_i-\mu_i
=
0
$$

因此：

$$
\alpha_i+\mu_i=C
$$

又因为：

$$
\alpha_i\ge 0,
\quad
\mu_i\ge 0
$$

所以：

$$
0\le \alpha_i\le C
$$

这说明引入松弛变量和惩罚系数 $C$ 后，拉格朗日乘子 $\alpha_i$ 会多出一个上界 $C$。

接下来，将：

$$
\mathbf{w}
=
\sum_{i=1}^{m}
\alpha_i y_i\mathbf{x}_i
$$

$$
\sum_{i=1}^{m}
\alpha_i y_i
=
0
$$

$$
C-\alpha_i-\mu_i=0
$$

代回拉格朗日函数。由于：

$$
\sum_{i=1}^{m}
(C-\alpha_i-\mu_i)\xi_i
=
0
$$

所以与 $\xi_i$ 有关的项消失。又因为：

$$
\sum_{i=1}^{m}
\alpha_i y_i
=
0
$$

所以与 $b$ 有关的项也消失。

最终得到只关于 $\alpha$ 的对偶目标函数：

$$
W(\alpha)
=
\sum_{i=1}^{m}\alpha_i
-
\frac{1}{2}
\sum_{i=1}^{m}
\sum_{j=1}^{m}
\alpha_i\alpha_jy_iy_j
\mathbf{x}_i^T\mathbf{x}_j
$$

因此，软间隔 SVM 的对偶问题为：

$$
\max_{\alpha} W(\alpha)
=
\max_{\alpha}
\left(
\sum_{i=1}^{m}\alpha_i
-
\frac{1}{2}
\sum_{i=1}^{m}
\sum_{j=1}^{m}
\alpha_i\alpha_jy_iy_j
\mathbf{x}_i^T\mathbf{x}_j
\right)
$$

$$
\text{s.t.}
\quad
0\le \alpha_i \le C,
\quad i=1,\cdots,m
$$

$$
\sum_{i=1}^{m}
\alpha_i y_i
=
0
$$

与硬间隔 SVM 相比，软间隔 SVM 的对偶目标函数形式没有变化，主要变化在于约束条件从：

$$
\alpha_i\ge 0
$$

变为：

$$
0\le \alpha_i\le C
$$

求得最优解 $\alpha_i^*$ 后，可以得到：

$$
\mathbf{w}^*
=
\sum_{i=1}^{m}
\alpha_i^* y_i \mathbf{x}_i
$$

分类函数为：

$$
f(\mathbf{x})
=
\mathbf{w}^{*T}\mathbf{x}+b^*
$$

代入 $\mathbf{w}^*$ 得：

$$
f(\mathbf{x})
=
\sum_{i=1}^{m}
\alpha_i^*y_i
\mathbf{x}_i^T\mathbf{x}
+
b^*
$$


对于满足 $0<\alpha_i^*<C$ 的样本，由 KKT 条件可知它正好位于间隔边界上，因此：

$$
y_i
\left(
\mathbf{w}^{*T}\mathbf{x}_i+b^*
\right)
=
1
$$

所以：

$$
b^*
=
y_i
-
\mathbf{w}^{*T}\mathbf{x}_i
$$



软间隔 SVM 中还需要满足 KKT 互补松弛条件：

$$
\alpha_i
\left[
1-\xi_i-y_i(\mathbf{w}^T\mathbf{x}_i+b)
\right]
=
0
$$

$$
\mu_i\xi_i=0
$$

又因为：

$$
\alpha_i+\mu_i=C
$$

所以：

$$
(C-\alpha_i)\xi_i=0
$$

由此可以得到样本位置与 $\alpha_i$ 的关系：

| 情况 | 条件 | 样本位置 | 是否为支持向量 |
|---|---|---|---|
| $\alpha_i=0$ | $y_if(\mathbf{x}_i)>1$ | 间隔外，分类正确 | 否 |
| $0<\alpha_i<C$ | $y_if(\mathbf{x}_i)=1$ | 正好在间隔边界上 | 是 |
| $\alpha_i=C$ | $y_if(\mathbf{x}_i)\le 1$ | 间隔内或被分错 | 是 |

因此，软间隔 SVM 的支持向量不仅包括正好落在间隔边界上的样本，也包括进入间隔内部甚至被分错的样本。

### 3. 序列最小优化(SMO)

**核心思想：** 每次选择两个不同的参数$\alpha_i$和$\alpha_j$，固定其他参数，只优化这两个参数。

此时的优化目标变为

$$
\max_{\alpha_1,\alpha_2} W(\alpha_1,\alpha_2)
=
\max_{\alpha_1,\alpha_2}
\left(
\alpha_1+\alpha_2
-
\frac{1}{2}
\left\|
\alpha_1 y_1 \mathbf{x}_1
+
\alpha_2 y_2 \mathbf{x}_2
\right\|^2
-
\left(
\alpha_1 y_1 \mathbf{x}_1
+
\alpha_2 y_2 \mathbf{x}_2
\right)^T
\left(
\sum_{i=3}^{m}
\alpha_i y_i \mathbf{x}_i
\right)
+
A_0
\right)
$$

$$
\text{s.t.}
\quad
0\le \alpha_1,\alpha_2\le C
$$

$$
\alpha_1 y_1+\alpha_2 y_2
=
-
\sum_{i=3}^{m}
\alpha_i y_i
$$

整理化简得

$$
\arg\max_{\alpha_1} W(\alpha_1)
=
-\frac{q}{2p}
=
\alpha_1
+
\frac{
\left(g(\mathbf{x}_2)-y_2\right)
-
\left(g(\mathbf{x}_1)-y_1\right)
}{
K_{11}+K_{22}-2K_{12}
}
y_1
$$

### 4. 核函数

| 核函数         | 公式                                                                                         | 特点               |
| ----------- | ------------------------------------------------------------------------------------------ | ---------------- |
| 线性核         | $$K(\mathbf{x},\mathbf{z})=\mathbf{x}^T\mathbf{z}$$                                        | 不做高维映射，相当于线性 SVM |
| 多项式核        | $$K(\mathbf{x},\mathbf{z})=(\mathbf{x}^T\mathbf{z}+c)^d$$                                  | 能表示多项式特征         |
| 高斯核 / RBF 核 | $$K(\mathbf{x},\mathbf{z})=\exp\left(-\frac{\|\mathbf{x}-\mathbf{z}\|^2}{2\sigma^2}\right)$$ | 最常用，可映射到无限维空间    |
| Sigmoid 核   | $$K(\mathbf{x},\mathbf{z})=\tanh(\kappa\mathbf{x}^T\mathbf{z}+c)$$                         | 与神经网络有一定联系       |

---

## 二、决策树

决策树是一种通过树形结构进行分类或回归的机器学习算法。它从根节点开始，根据样本的不同特征不断进行判断和划分，最后到达叶节点并给出预测结果。

### 1. 决策树的构造

每一步都应该选择能获得**更大信息增益**的特征作为分类特征

**信息熵：** 表示随机变量$X$自身的不确定性有多大

$$
H(X)
=
-\sum_{i=1}^{n}
P(X=i)\log P(X=i)
$$

**交叉熵：** 用分布 $Y$ 去描述真实分布 $X$ 时，平均需要多少信息量

$$
H(X,Y)
=
-\sum_{i=1}^{n}
P(X_i)\log P(Y_i)
$$

**条件熵：** 在已经知道 $Y=j$ 的条件下，随机变量 $X$ 还剩下多少不确定性

$$
H(X\mid Y_j)
=
-\sum_{i=1}^{n}
P(X_i\mid Y_j)\log P(X_i\mid Y_j)
$$

如果给出的条件是$Y$的分布，那么条件熵为

$$
H(X \mid Y)
=
E_Y\left[H(X \mid Y_j)\right]
=
-\sum_{j=1}^{n} P(Y_j)H(X \mid Y_j)
=
-\sum_{i=1}^{n}\sum_{j=1}^{n}
P(X_i,Y_j)\log P(X_i \mid Y_j)
$$

**信息增益：** 数据不确定性减少了多少

$$
I(X \mid Y)=H(X)-H(X \mid Y)
$$

为了削弱信息增益对多取值属性的偏好，从而降低过拟合的风险，我们引入**信息增益率**

$$
I_R(X,Y)
=
\frac{I(X,Y)}{H_Y(X)}
=
\frac{H(X)-H(X\mid Y)}{H_Y(X)}
$$

其中 

$$
H_Y(X)=-\sum_{y\in \mathcal{Y}}\frac{|X_{Y=y}|}{|X|}\log\frac{|X_{Y=y}|}{|X|}
$$

用于衡量 $Y$ 把数据集切分的有多碎

### 2. ID3算法与C4.5算法

#### ID3算法

**算法思想：** 从根节点开始，每次选择使信息增益最大的特征进行分类，并对产生的子节点进行递归处理，知道所有节点上的点都属于同一类别为止

#### C4.5算法

**算法思想：** 为了防止ID3算法使用信息增益导致的过拟合现象，所以使用信息增益率来代替信息

#### 代价函数

$$
H_t(T)
=
-\sum_k
\frac{N_{tk}}{N_t}
\log
\frac{N_{tk}}{N_t}
$$

可以用来衡量每个叶子节点中**样本的混乱程度**，在此基础上，我们再引入正则化的思想，控制一下叶子节点的数量，，从而得到代价函数为

$$
C(T)
=
\sum_{t=1}^{|T|}
N_tH_t(T)
+
\lambda |T|
$$

>信息增益和信息增益率用于确定使用哪个特征进行划分；而代价函数总用于判断是否要继续划分，如果代价函数增大，就不再分裂当前的叶子节点
{:.prompt-info}


### 3. CART算法

ID3和C4.5是以离散随机变量的熵为基础的，不能很好衡量回归问题中划分带来的收益，因此，**分类和回归树(CART)**采用误差的平方和作为回归问题寻找最优特征的标准。

由于要处理**回归问题**，我们不仅要确定划分特征$j$,还要确定阈值$s$

$$
\min_{j,s}
\sum_{x_i \in R_1(j,s)}
(x_i-\hat{c}_1)^2
+
\sum_{x_i \in R_2(j,s)}
(x_i-\hat{c}_2)^2
$$

其中$\hat{c}$为区域内所有样本的平均值

在求解这个问题时，对于划分所使用的特征，我们只能枚举，但是划分的阈值可以利用类似前缀和的思想来进行处理


$$
L_q
=
-
\frac{1}{q}
\left(
\sum_{k=1}^{q}y_k
\right)^2
-
\frac{1}{r-q}
\left(
\sum_{k=q+1}^{r}y_k
\right)^2
+
C
$$

为了快速计算，可以定义前缀和：

$$
S_q=\sum_{k=1}^{q}y_k
$$

总和为：

$$
S_r=\sum_{k=1}^{r}y_k
$$

那么右侧区域的和为：

$$
\sum_{k=q+1}^{r}y_k=S_r-S_q
$$

所以通式可以写成：

$$
L_q
=
C
-
\frac{S_q^2}{q}
-
\frac{(S_r-S_q)^2}{r-q}
$$

因此只需要遍历所有可能的划分位置 $q=1,2,\cdots,r-1$，计算：

$$
-\frac{S_q^2}{q}
-
\frac{(S_r-S_q)^2}{r-q}
$$

取最小的那个划分点即可。

除了回归树，CART算法同样也可以用来构建分类树，在这里我们引入**基尼不纯度**

$$
Gini(p)
=
\sum_{k=1}^{K}p(k)(1-p(k))
=
1-\sum_{k=1}^{K}p(k)^2
$$

>如果从一个节点中随机抽取一个样本，并按照该节点的类别分布随机给它分类，那么分类错误的概率就是基尼不纯度。

在实际使用的过程中，我们用不同样本的比例来确定概率

$$
Gini(D)
=
1-\sum_{k=1}^{K}
\left(
\frac{|D^k|}{|D|}
\right)^2
$$

### 4. 三种算法的区别

| 指标    | 使用算法 | 衡量内容          | 选择标准 | 主要特点        |
| ----- | ---- | ------------- | ---- | ----------- |
| 信息增益  | ID3  | 熵减少多少         | 越大越好 | 容易偏向多取值属性   |
| 信息增益率 | C4.5 | 单位划分复杂度下的信息增益 | 越大越好 | 缓解多取值属性偏好   |
| 基尼不纯度 | CART | 节点类别混杂程度      | 越小越好 | 计算简单，适合二叉划分 |

---

## 三、集成学习与梯度提升决策树

**集成学习：** 将不同算法得到的模型按某些方式进行组合，取长补短，从而得到比任意单个模型表现都要好的模型

### 1. 自举聚合(bagging)与随机森林

#### 自举采样

**自举采样：** 为了保证随机性，尽可能降低不同子数据集之间的相关性，采用了允许重复的有放回采样

**OOB(out-of-bag)误差:** 对于数据集中的每个样本 $x$，我们选择那些训练集中不包含 $x$ 的模型进行测试，将它们的输出用与集成模型相同的集成方式组合起来，得到 $x$ 的预测结果，并用该结果与真实值计算误差，即 OOB 误差。

>由于自举采样保持了合适的采样比例，用OOB误差进行评估与单独划分测试集进行评估的结果没有显著区别

#### 偏差-方差分解

设数据的分布为$y=f(x)+\epsilon$,满足$E(\epsilon)=0$,$Var(\epsilon)=\sigma_{\epsilon}^{2}$

对于某个机器学习模型$\hat{f}(x)$,在样本$x$上的期望误差平方损失为

$$
\mathcal{L}(x)
=
E\left(((f(x)+\epsilon-\hat f(x))^2)\right)
=
\operatorname{Bias}^2(\hat f(x))
+
\operatorname{Var}(\hat f(x))
+
\sigma_{\epsilon}^{2}
$$

由于bagging算法建立每个模型的过程是相同的，其期望和方差可以认为相同，记为$\mu(x)$和$\sigma^2/(x)$,同时假设不同模型之间的相关系数为$\rho$

$$
\operatorname{Bias}(\hat f(x))
=
\mu(x)
$$

$$
\operatorname{Var}(\hat f(x))
=
\frac{1-\rho}{B}
\sigma^2(x)
+
\rho\sigma^2(x)
$$

可以看出，聚合模型并不改变单一模型的期望偏差，但是可以减小模型预测的方差，因此，bagging算法对低偏差、高方差模型(如神经网络、决策树)的稳定性有很大帮助

#### 随机森林

对于决策树模型，其bagging算法的改进版本叫作**随机森林**

**核心思想：** 为了进一步降低模型的相关性，在决策树每次分裂节点前，从全部的$M$个特征中采样$m$个特征，从中选择最优划分特征

### 2. 集成学习器

bagging算法要求底层的基础模型是同一种类，否则各个模型具有相同的期望偏差和方差的假设不再成立。由此我们提出一种**集成学习器**。

我们训练一个新模型，将$n$个模型的预测结果作为输入，由新模型给出最终输出。将底层的模型称为**集学习器**，将这个新模型称为**元学习器**

#### 堆垛算法(stacking)

![堆垛算法](assets/img/posts/notes/machine_learning/6.png)

把整个数据集均匀划分为 $k$ 份，让 $f_i$ 分别在其中 $k-1$ 份上训练，再在剩余的一份上进行测试，给出其预测结果。这样，当整个训练过程完成时，数据集中的每一份数据都有 $f_i$ 的预测结果，且进行预测的模型必定没有将其用于训练。

$$
s=\left(f_1(x),\cdots,f_n(x)\right)^T
$$

对于元学习器的测试集，我们不再像训练集那样做划分，而是将同一个基学习器在数据集的 $k$ 个不同部分训练出的结果取平均值，作为新的训练数据。

$$
s=
\left(
\frac{1}{k}\sum_{j=1}^{k} f_1^{(j)}(x),
\cdots,
\frac{1}{k}\sum_{j=1}^{k} f_n^{(j)}(x)
\right)^T
$$

>这是因为测试集中的数据没有参与过任何一个基学习器的训练
{: .prompt-info}

理论上只要元学习器的模型合适，就可以替代任何集成学习算法。但考虑到训练难度等问题，通常采用**逻辑斯谛回归**作为元学习器

### 3. 提升算法(boosting)

**基本思想：** 利用当前模型的偏差来调整训练数据的权重，使下一个模型更多关注偏差较大的部分

#### 适应提升

我们可以用加性模型（additive model）来表示强学习器：

$$
F(x)=\sum_{i=1}^{M}\alpha_i f_i(x)
$$

其中，$M$ 是弱学习器的数量，$f_i(x)$ 是弱学习器，$\alpha_i$ 是权重。采用不同的损失函数就可以导出不同的算法。

---

##### Adaboost算法

对于二分类问题($y \in \{-1,1\}$)，引入一种新的损失函数：

$$
\mathcal{L}(F)=E_x\left(e^{-yF(x)}\right)
$$

>**指数损失：** 分对且越自信损失越小；分错且越自信损失急剧增大
{: .prompt-info}

对于单个样本$x$,记$p$为样本$x$的类别$y=1$的概率,损失函数为

$$
E\left(e^{-yF(x)}\mid x\right)
=
pe^{-F(x)}
+
(1-p)e^{F(x)}
$$

当损失函数最小时，关于$F(x)$的偏导数应该为0

$$
0
=
\frac{\partial E\left(e^{-yF(x)}\mid x\right)}
{\partial F(x)}
=
-pe^{-F(x)}
+
(1-p)e^{F(x)}
$$

$$
p
=
\frac{1}{1+e^{-2F(x)}}
=
\sigma(2F(x))
$$

所以，Adaboost与逻辑斯谛回归在本质上是等价的。

要优化诸如Adaboost的加性模型，我们可以采用**前向分步**，向模型中不断添加弱学习器

记

$$
F_m(x)=\sum_{i=1}^{m}\alpha_i f_i(x)
$$

假设前 $m-1$ 步的优化已经完成，我们得到了模型 $F_{m-1}$ 并将其固定。在第 $m$ 步的模型

$$
F_m=F_{m-1}+\alpha_m f_m
$$

中，我们只需要优化 $\alpha_m$ 和 $\gamma_m$ 就可以了

对于二分类问题，我们假设每个弱学习器 $f_i(x)$ 的输出都是具体的类别 $-1$ 或 $1$。将 优化目标函数 $\mathcal{L}(F)=E_x(e^{-yF(x)})$ 应用到第 $m$ 步上，就得到

$$
\mathcal{L}(F_m)
=
E_x\left(e^{-yF_{m-1}(x)}e^{-y\alpha_m f_m(x)}\right)
=
E_x\left(w_xe^{-y\alpha_m f_m(x)}\right)
=
E_w\left(e^{-y\alpha_m f_m(x)}\right)
$$

>上一轮模型分错的样本会有更大的权重，$\omega$实际上来自于指数损失
{: .prompt-info}

为了求 $\mathcal{L}(F_m)$ 的最小值，我们令其对 $\alpha_m$ 和 $f_m(x)$ 的偏导数分别等于零。

对于 $f_m$，直接计算梯度求解比较困难，我们利用 $e^t$ 函数在 $t=1$ 处的二阶泰勒展开

$$
e^t \approx 1+t+\frac{1}{2}t^2
$$

以及

$$
f_m^2(x)=1
$$

得到 $\mathcal{L}(F_m)$ 的近似形式为

$$
\mathcal{L}(F_m)
\approx
E_w
\left(
1-y\alpha_m f_m(x)
+
\frac{1}{2}\alpha_m^2
\right)
$$

假设分类错误率小于 $0.5$，那么 $\alpha_m>0$。令损失函数最小，可以得到

$$
f_m(x)
=
\arg\min_f \mathcal{L}(F_m(x))
$$

$$
\approx
\arg\min_f
E_w
\left(
1-y\alpha_m f(x)
+
\frac{1}{2}\alpha_m^2
\mid x
\right)
$$

$$
=
\arg\min_f
E_w
\left(
-y\alpha_m f(x)
\mid x
\right)
$$

$$
=
\arg\max_f
E_w
\left(
yf(x)
\mid x
\right)
$$

由于我们考虑的是 $f_m$ 对某个样本的作用，因此上式右端的期望中限定了 $x$。这一结果提示我们，我们在训练 $f_m$ 时，应当为数据集中的样本添加权重

$$
w_x=e^{-yF_{m-1}(x)}
$$

考虑到 $f_m(x)\in\{-1,1\}$，上式的解为

$$
f_m(x)
=
\begin{cases}
1, & E_w(y\mid x)>0 \\
-1, & \text{其他}
\end{cases}
$$
对于 $\alpha_m$，有

$$
0
=
\frac{
\partial E_w\left(e^{-y\alpha_m f_m(x)}\right)
}{
\partial \alpha_m
}
=
E_w\left(-yf_m(x)e^{-y\alpha_m f_m(x)}\right)
$$

注意，$y$ 和 $f_m(x)$ 都属于 $\{-1,1\}$，其乘积当 $y=f_m(x)$ 时为 $1$，当 $y\ne f_m(x)$ 时为 $-1$，上式可以转化为

$$
0
=
E_w\left(-yf_m(x)e^{-y\alpha_m f_m(x)}\right)
$$

$$
=
E_w\left(
P(y\ne f_m(x))\cdot e^{\alpha_m}
+
(1-P(y\ne f_m(x)))\cdot(-e^{-\alpha_m})
\right)
$$

$$
=
\mathrm{err}\cdot e^{\alpha_m}
-
(1-\mathrm{err})\cdot e^{-\alpha_m}
$$

$$
\Rightarrow
\alpha_m
=
\frac{1}{2}
\log
\frac{1-\mathrm{err}}{\mathrm{err}}
$$

>其中$err$表示以$w$加权后$f_m$的分类错误率
{: .prompt-info}

综上所属，Adaboost算法的流程为：

1. 初始化样本权重。设数据集大小为 $N$，为所有样本赋予相同的权重：

   $$
   w_x=\frac{1}{N}
   $$

2. 开始迭代，令：

   $$
   m=1,2,\cdots,M
   $$

   在每一轮迭代中执行以下步骤：

   - 在加权的数据集上训练弱分类器：

     $$
     f_m(x)
     $$

   - 计算分类器的加权误差：

     $$
     \mathrm{err}
     =
     E_w\left(
     \mathbb{I}(y\ne f_m(x))
     \right)
     $$

   - 计算分类器的权重：

     $$
     \alpha_m
     =
     \frac{1}{2}
     \log
     \frac{1-\mathrm{err}}{\mathrm{err}}
     $$

   - 更新数据集中样本的权重：

     $$
     w_x
     \leftarrow
     w_x e^{-y\alpha_m f_m(x)}
     $$

3. 迭代完成后，得到强学习器：

   $$
   F(x)
   =
   \operatorname{sgn}
   \left(
   \sum_{m=1}^{M}
   \alpha_m f_m(x)
   \right)
   $$

上述Adaboost算法由于弱分类器的输出只有两个值，因此又称为**离散适应提升**

当弱分类器的输出为连续的实数时，可以将其看作离散的弱分类器乘以分类器权重的结果，称为**实适应提升**

1. 初始化样本权重。设数据集大小为 $N$，为所有样本赋予相同的初始权重：

   $$
   w_x=\frac{1}{N}
   $$

2. 开始迭代，令：

   $$
   m=1,2,\cdots,M
   $$

   在每一轮迭代中执行以下步骤：

   - 在当前加权数据集上训练弱学习器，并估计样本属于正类 $1$ 的概率：

     $$
     p_m(x)=E_w(y=1\mid x)
     $$

     其中，$p_m(x)\in[0,1]$。

   - 根据概率构造连续输出的弱学习器：

     $$
     f_m'(x)
     =
     \frac{1}{2}
     \log
     \frac{p_m(x)}{1-p_m(x)}
     $$

     这里的 $f_m'(x)$ 不再只是输出 $-1$ 或 $1$，而是输出一个连续值，用来表示分类方向和分类置信度。

   - 更新样本权重：

     $$
     w_x
     \leftarrow
     w_x e^{-y f_m'(x)}
     $$

     如果样本被正确分类，则 $y f_m'(x)>0$，权重减小；如果样本被错误分类，则 $y f_m'(x)<0$，权重增大。

   - 对样本权重进行归一化，使所有样本权重之和为 $1$。

3. 迭代完成后，得到最终强学习器：

   $$
   F(x)
   =
   \operatorname{sgn}
   \left(
   \sum_{m=1}^{M}
   f_m'(x)
   \right)
   $$

| 对比                | 离散 AdaBoost       | 实 AdaBoost |
| ----------------- | ----------------- | ---------- |
| 弱分类器输出            | -1 或 1        | 连续实数       |
| 是否单独计算 $\alpha_m$ | 需要                | 通常不需要      |
| 更新权重用什么           | $\alpha_m f_m(x)$ | $f'_m(x)$  |
| 是否表达置信度           | 较弱                | 更强         |

#### 梯度提升

我们可以换一个视角来考虑加性模型的优化过程。考虑连续的回归问题，和实 AdaBoost 一样，将弱学习器的权重与学习器本身合并，记

$$
F_{m-1}
=
\sum_{i=1}^{m-1}
f_i(x)
$$

是到第 $m-1$ 步为止的学习器，这些弱学习器已经固定，不再训练。

设总损失函数为

$$
\mathcal{L}(F)
$$

单个样本的损失函数为

$$
l(y,\hat{y})
$$

其中，$y$ 表示真实值，$\hat{y}$ 表示模型预测值。

$$
f_m
=
\arg\min_f
E_x
\left(
l\left(
y,
\hat{y}_{m-1}+f(x)
\right)
\right)
$$

分别求对每个样本$x$上预测值$F(x)$的梯度

$$
\nabla_{F(x)}\mathcal{L}(\hat{y}_{m-1})
=
\nabla_{F(x)}l(y,\hat{y}_{m-1})
$$

做一步梯度下降得到$F_m$

$$
F_m(x)
=
\hat{y}_{m-1}
-
\eta_m
\nabla_{F(x)}\mathcal{L}(\hat{y}_{m-1})
$$

于是新的弱学习器为

$$
f_m(x)
=
-\eta_m
\nabla_{F(x)}\mathcal{L}(\hat{y}_{m-1})
$$

##### 极限梯度提升(XGBoost)

梯度提升算法要求各个弱学习器的模型一致，在实践中常与决策树模型结合。而极限梯度提升则在损失函数中引入了与决策树复杂度相关的正则化约束

$$
\mathcal{L}(F_m)
=
\sum_x
l\left(y,\hat{y}_{m-1}+f_m(x)\right)
+
\Omega(f_m)
$$

$$
\Omega(f_m)
=
\gamma T
+
\frac{1}{2}\lambda \|w\|^2
$$

>一颗叶子节点的输出表示第m轮的修正量，如果太大可能导致过拟合
{: .prompt-info}

我们在$F_{m-1}$处进行泰勒展开并保留到二阶项

$$
\mathcal{L}(F_m)
\approx
\sum_x
\left(
l(y,\hat{y}_{m-1})
+
g(x)f_m(x)
+
\frac{1}{2}h(x)f_m^2(x)
\right)
+
\Omega(f_m)
$$

$$
g(x)
=
\nabla_{F(x)}
l(y,\hat{y}_{m-1})
$$

$$
h(x)
=
\nabla_{F(x)}^2
l(y,\hat{y}_{m-1})
$$

舍去常数项整理得

$$
\mathcal{L}(F_m)
=
\sum_{j=1}^{T}
\left[
G_jw_j
+
\frac{1}{2}
(H_j+\lambda)w_j^2
\right]
+
\gamma T
$$

其中$G_j=\sum_{x\in I_j}g(x)$,$H_j=\sum_{x\in I_j}h(x)$

在决策树结构固定的情况下，是一个关于$\omega$二次规划问题

$$
w_j^*
=
\left(
\arg\min_w \mathcal{L}(F_m)
\right)_j
=
-\frac{G_j}{H_j+\lambda}
$$

$$
\mathcal{L}(F_m;w^*)
=
-\frac{1}{2}
\sum_{j=1}^{T}
\frac{G_j^2}{H_j+\lambda}
+
\gamma T
$$

因此，我们在决策树的节点分裂之前先计算损失函数是否会降低，然后决定是否继续分裂决策树
