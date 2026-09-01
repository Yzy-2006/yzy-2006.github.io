---
title: 机器学习 第二章 参数化模型
description: 机器学习第2章笔记
author: 阎梓瑜
date: 2026-07-24 21:30:00 +0800
categories: [机器学习, 参数化模型]
tags: [机器学习]
pin: false
math: true
mermaid: true
---

## 一、逻辑斯谛回归(对数几率回归)

### 1. 逻辑斯谛函数下的线性模型

对于二分类问题，我们同样可以作线性假设，但是线性回归的取值范围是$R$，我们需要把它映射到$[0,1]$，所以我们引入**逻辑斯谛函数**

$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

$$
\sigma'(x)=\sigma(x)(1-\sigma(x))
$$

>对于多分类问题，我们使用softmax函数来进行映射，$\mathrm{softmax}(z_i)=\frac{e^{z_i}}{\sum_{j=1}^{K}e^{z_j}}$,逻辑斯谛函数即为$K=2$时的特殊情况
{: .prompt-info}

### 2.最大似然估计(MLE)

模型将所有样本都预测正确的概率称为**似然函数**

$$
L(\theta)
=
\prod_{i=1}^{N}
p_i^{y_i}(1-p_i)^{1-y_i}
$$

为了便于计算，我们对似然函数两边取对数

$$
\ell(\theta)
=
\log L(\theta)
=
\sum_{i=1}^{N}
\left[
y_i\log p_i
+
(1-y_i)\log(1-p_i)
\right]
$$

$$
\nabla l(\theta)
=
\sum_{i=1}^{N}
\left[
\left(1-\sigma(\theta^Tx_i)\right)y_ix_i
-
\sigma(\theta^Tx_i)(1-y_i)x_i
\right]
$$

由于在机器学习中一般是取最小值，所以定义损失函数$J(\theta)=-l(\theta)$

$$
\nabla J(\theta)
=
-\nabla l(\theta)
=
X^T
\left(
y-\sigma(X\theta)
\right)
$$

$$
\theta
\leftarrow
\theta+
\eta X^T
\left(
y-\sigma(X\theta)
\right)
$$


之后，我们再为模型加入$L_2$正则化约束

$$
\min_{\theta}J(\theta)
=
\min_{\theta}
\left(
-l(\theta)
+
\frac{\lambda}{2}
\|\theta\|_2^2
\right)
$$

$$
\nabla J(\theta)
=
-X^T
\left(
y-\sigma(X\theta)
\right)
+
\lambda\theta
$$

$$
\theta
\leftarrow
(1-\lambda\eta)\theta
+
\eta X^T
\left(
y-\sigma(X\theta)
\right)
$$

### 3.分类问题的评价指标

**混淆矩阵：** 在机器学习中，我们常使用混淆矩阵来统计不同的分类结果

|       | 预测为正类 | 预测为负类 |
| ----- | ----: | ----: |
| 实际为正类 |    TP(真阳性) |    FN(假阴性) |
| 实际为负类 |    FP(假阳性) |    TN(真阴性) |

**准确率：** 所有样本中预测正确的比例

$$
Accuracy
=
\frac{TP+TN}{TP+TN+FP+FN}
$$

**查准率：** 测为正类的样本中，有多少是真的正类

$$
Precision
=
\frac{TP}{TP+FP}
$$

**查全率(TPR)：** 所有真实正类中，有多少被模型找出来了

$$
Recall
=
\frac{TP}{TP+FN}
$$

**假阳性率(FPR)** 真实负类中，被错误预测为正类的比例

$$
FPR
=
\frac{FP}{FP+TN}
$$

**F1分数：** 查准率和查全率的调和平均值

$$
F_1
=
\frac{2 \cdot Precision \cdot Recall}
{Precision+Recall}
$$

**F-beta分数** 查全率和查准率的加权综合

$$
F_\beta
=
(1+\beta^2)
\cdot
\frac{Precision \cdot Recall}
{\beta^2 \cdot Precision + Recall}
$$

**受试者操作特征(ROC)曲线：** 横轴为FPR,纵轴为TPR，每个点代表一个阈值，随着阈值的增大，找出更多正类，但也会产生更多误报

**ROC 曲线下面积(AUC):** 随机抽一个正样本和一个负样本，模型给正样本的分数高于负样本的概率。并不以来某一个固定的阈值，而是模型在所有阈值下的整体排序能力

### 4.交叉熵与最大似然

#### 熵的定义

在信息论中，事件发生的概率越小，其发生时提供的信息量也就越大，单个事件发生所能提供的信息量为

$$
I(x)
=
-\log p(x)
$$

对于事件离散且有限的情况，我们可以用**熵**来衡量分布的不确定程度

$$
H(X)
=
-\sum_{i=1}^{n}p(x_i)\log p(x_i)
$$

>当某个事件发生的概率为1,其他事件为0时，分布的熵最小，$H=0$；所有事件发生的概率相等时，分布的熵最大，$H=\log n$

#### 相对熵(KL散度)

如果关于随机变量存在两个概率分布，可以用**相对熵(KL散度)**来衡量这两个分布之间的距离

$$
D_{KL}(P\|Q)
=
\sum_x P(x)\log\frac{P(x)}{Q(x)}
$$

>它衡量了当真实分布是 $P$ 时，用另一个分布 $Q$ 去近似它所产生的平均额外信息损失。

#### 交叉熵

$$
H(P,Q)
=
-\sum_{i=1}^{n}p_i\log q_i
$$

$$
H(P,Q)
=
H(P)
+
D_{KL}(P\|Q)
$$

>交叉熵衡量“用预测分布 Q 描述真实分布 P 需要多少信息量”；KL 散度衡量“相比直接用真实分布 P，用 Q 会额外多付出多少信息量”。最小化交叉熵等价于最小化KL散度

二分类问题的总交叉熵恰好等于负的对数似然函数

$$
L
=
-\sum_{i=1}^{N}
\left[
y_i\log \hat y_i
+
(1-y_i)\log(1-\hat y_i)
\right]
$$

### 5.广义线性模型(GLM)

#### GLM的核心概念

GLM的核心写法为：

$$
g(\mathbb{E}[y \mid x]) = \theta^T x
$$

也可以写为：

$$
\eta = \theta^T x
$$

$$
g(\mu) = \eta
$$

其中：

$$
\mu = \mathbb{E}[y \mid x]
$$

$$
\mu = g^{-1}(\theta^T x)
$$

>模型先算一个线性值$\theta^T x$ ，再通过某个函数变换成合理的预测值。

#### 常见GLM对比

| 模型   | 输出类型 | 分布假设  | 连接函数     | 形式                            |
| ---- | ---- | ----- | -------- | ----------------------------- |
| 线性回归 | 连续值  | 高斯分布  | 恒等函数     | $\mu=\theta^Tx$               |
| 逻辑回归 | 二分类  | 伯努利分布 | logit 函数 | $\log\frac{p}{1-p}=\theta^Tx$ |
| 泊松回归 | 计数   | 泊松分布  | log 函数   | $\log\lambda=\theta^Tx$       |


#### 指数分布族

$$
p(y \mid \eta)
=
h(y)\exp\left(\eta^T T(y)-A(\eta)\right)
$$

| 符号        | 含义             |
| --------- | -------------- |
| $y$       | 随机变量           |
| $\eta$    | 自然参数           |
| $T(y)$    | 充分统计量,表示从数据$y$中提取出来的关键信息          |
| $A(\eta)$ | 对数配分函数，也叫归一化函数，用来保证概率和为1 |
| $h(y)$    | 基准测度，只和 $y$ 有关 |


#### 指数分布族与GLM的关系

指数分布族的核心是**自然参数$\eta$**,决定了这个分布的形状

同时，指数分布族有一条很重要的性质

$$
\mathbb{E}[T(y)] = \nabla_{\eta} A(\eta)
$$

如果$T(y)=y$，那么$\mathbb{E}[y] = A'(\eta)$

>指数分布族负责描述 y 的概率分布形式；GLM 负责让这个分布的参数随着输入 x 改变。
{: .prompt-info}

---

## 二、双线性模型

**双线性模型：** 二元函数固定任意一个自变量时，函数关于另一个自变量是线性的

### 1. 矩阵分解(MF)

**核心思想：** 把一个大的评分矩阵，分解成两个较小的低维矩阵，用它们的乘积来近似原矩阵。

**损失函数：**

$$
J(P,Q)
=
\sum_{i=1}^{N}
\sum_{j=1}^{M}
I_{ij}
\mathcal{L}
\left(
p_i^T q_j,\ r_{ij}
\right)
$$

优化目标(加入$L_2$正则化)为

$$
\min_{P,Q}J(P,Q)
=
\min_{P,Q}
\left(
\frac{1}{2}
\sum_{i=1}^{N}
\sum_{j=1}^{M}
I_{ij}
\left[
\left(
p_i^Tq_j-r_{ij}
\right)^2
+
\lambda
\left(
\|p_i\|^2+\|q_j\|^2
\right)
\right]
\right)
$$

梯度为

$$
\nabla_{p_{ik}}J(P,Q)
=
I_{ij}
\left(
p_i^Tq_j-r_{ij}
\right)
q_{jk}
+
\lambda p_{ik}
$$

$$
\nabla_{q_{jk}}J(P,Q)
=
I_{ij}
\left(
p_i^Tq_j-r_{ij}
\right)
p_{ik}
+
\lambda q_{jk}
$$

### 2. 因子分解机(FM)

**核心思想：** 在线性模型的基础上，自动学习特征之间的二阶交互关系，并且用低维向量内积来表示这种交互

**核心公式**

$$
\hat y(x)
=
w_0
+
\sum_{i=1}^{n}w_ix_i
+
\sum_{i=1}^{n}
\sum_{j=i+1}^{n}
w_{ij} x_ix_j
$$

该公式的**向量形式**

$$
\hat{y}(x)
=
\theta_0
+
\theta^T x
+
\frac{1}{2}x^T W x
$$

由于特征向量的稀疏性，通常难以对$w_{ij}$进行更新，所以我们对权重矩阵进分解

$$
W = VV^T
$$

$$
\hat y(x)
=
w_0
+
\sum_{i=1}^{n}w_ix_i
+
\sum_{i=1}^{n}
\sum_{j=i+1}^{n}
\langle v_i,v_j\rangle x_ix_j
$$

其中$v_i$实际上就是每个特征对应的隐向量，对$v_s$求梯度的结果为

$$
\nabla_{v_s}\hat{y}
=
x_s
\sum_{i=1}^{d}
x_iv_i
-
x_s^2v_s
$$

>**为什么能解决特征向量稀疏的问题?**   
如果直接学习$w_{ij}$，只有在$x_i$和$x_j$都不为0时才能学习，而某个特征的隐向量可以来自它与其他所有出现特征之间的交互，可学习的样本大大增多
{: .prompt-info}

为了降低额外的计算开销，我们通过改变计算顺序的方法

$$
\hat{y}(x)
=
\theta_0
+
\sum_{i=1}^{d}\theta_i x_i
+
\frac{1}{2}
\sum_{l=1}^{k}
\left[
\left(
\sum_{i=1}^{d}v_{il}x_i
\right)^2
-
\sum_{i=1}^{d}v_{il}^{2}x_i^{2}
\right]
$$

### 3. 概率矩阵分解(PMF)

可以理解为矩阵分解的概率版本，认为

$$
r_{ij} \sim \mathcal{N}(p_i^Tq_j,\sigma^2)
$$

那么我们观测到的$R$的出现概率为

$$
p(R \mid P,Q,\sigma^2)
=
\prod_{i=1}^{N}
\prod_{j=1}^{M}
\left[
\mathcal{N}
\left(
r_{ij}\mid p_i^Tq_j,\sigma^2
\right)
\right]^{I_{ij}}
$$

同时假设用户向量和物品向量本身也服从正态分布

$$
p_i \sim \mathcal{N}(0, \sigma_P^2 I)
$$

$$
q_j \sim \mathcal{N}(0, \sigma_Q^2 I)
$$

认为用户向量和物品向量大概率分布在 0 附近，这其实就是 L2 正则化的概率解释


根据贝叶斯公式可得后验概率为

$$
\log P(P,Q \mid R,\sigma,\sigma_p,\sigma_q)
=
\sum_{i=1}^{N}
\sum_{j=1}^{M}
I_{ij}
\log p_N
\left(
r_{ij}\mid p_i^Tq_j,\sigma^2
\right)
+
\sum_{i=1}^{N}
\log p_N
\left(
p_i\mid 0,\sigma_p^2I
\right)
+
\sum_{j=1}^{M}
\log p_N
\left(
q_j\mid 0,\sigma_q^2I
\right)
+
\log C
$$

代入正态分布公式得

$$
\log P(P,Q \mid R,\sigma,\sigma_p,\sigma_q)
=
-\frac{1}{\sigma^2}
\left[
\frac{1}{2}
\sum_{i=1}^{N}
\sum_{j=1}^{M}
I_{ij}
\left(
r_{ij}-p_i^Tq_j
\right)^2
+
\frac{\lambda_p}{2}
\|P\|_F^2
+
\frac{\lambda_q}{2}
\|Q\|_F^2
\right]
+
C_1
$$

$$
\lambda_p
=
\frac{\sigma^2}{\sigma_p^2}
$$

$$
\lambda_q
=
\frac{\sigma^2}{\sigma_q^2}
$$

我们定义损失函数为

$$
J(P,Q)
=
\frac{1}{2}
\sum_{i=1}^{N}
\sum_{j=1}^{M}
I_{ij}
\left(
r_{ij}-p_i^Tq_j
\right)^2
+
\frac{\lambda_p}{2}
\|P\|_F^2
+
\frac{\lambda_q}{2}
\|Q\|_F^2
$$

这就是带有$L_2$正则化的MF模型

---

## 三、神经网络与多层感知机

### 1. 感知机

![感知机](assets/img/posts/notes/machine_learning/1.png)

$$
\hat{y}
=
\mathbb{I}
\left(
\sum_{i=1}^{m} w_i x_i + b \ge 0
\right)
$$

$$
w_i
\leftarrow
w_i
-
\eta(\hat{y}-y)x_i
$$

$$
b
\leftarrow
b
-
\eta(\hat{y}-y)
$$

用于处理二分类问题并且参数可以自动调整，但是只能处理线性问题

### 2. 隐含层与多层感知机

**前馈结构：** 每一层之与前后解耦相邻层的神经元连接

**多层感知机：** 将多个单层感知及按前馈结构组合起来

![多层感知机](assets/img/posts/notes/machine_learning/2.png)

#### 常见激活函数

| 激活函数 | 公式 | 输出范围 | 特点 |
|---|---|---|---|
| Sigmoid | $$\sigma(x)=\frac{1}{1+e^{-x}}$$ | $$(0,1)$$ | 平滑可导，输出可看作概率 |
| Tanh | $$\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}$$ | $$(-1,1)$$ | 以 0 为中心，仍然是 S 型曲线 |
| ReLU | $$\operatorname{ReLU}(x)=\max(x,0)$$ | $$[0,+\infty)$$ | 计算简单，大于 0 时梯度稳定，是深度网络常用激活函数 |

### 3. 反向传播

本质上就是求导的链式法则

$$
\frac{\partial L}{\partial W}
=
\frac{\partial L}{\partial \hat{y}}
\cdot
\frac{\partial \hat{y}}{\partial z}
\cdot
\frac{\partial z}{\partial W}
$$

---

## 四、卷积神经网络(CNN)

在图像处理等任务中，我们需要提取高维特征，所以引入**卷积神经网络**

### 1. 卷积

**二维离散卷积公式：**

$$
(f * g)(m,n)
=
\sum_{k=-\infty}^{+\infty}
\sum_{l=-\infty}^{+\infty}
f(k,l)\,g(m-k,n-l)
$$

经过一些不影响实际结果的变形后，我们可以得到

$$
(f * g)(m,n)
=
\sum_{k=-\infty}^{+\infty}
\sum_{l=-\infty}^{+\infty}
f(k,l)\,g(m-k,n-l)
$$

>用一个小的卷积核在输入数据上滑动，每次对局部区域做加权求和，从而提取局部特征

在进行卷积操作之后，图像的尺寸通常会变小，所以需要对图像进行**填充**

| 填充方式  | 英文                  | 做法                       | 特点                | 常见用途              |
| ----- | ------------------- | ------------------------ | ----------------- | ----------------- |
| 无填充   | Valid Padding       | 不在边缘补任何值                 | 输出尺寸会变小，边缘信息容易丢失  | 想减少特征图尺寸时使用       |
| 零填充   | Zero Padding        | 在边缘补 0                   | 最常见，简单有效，可以控制输出尺寸 | CNN 中最常用          |
| 同尺寸填充 | Same Padding        | 通过补 0，使输出尺寸和输入尺寸相同       | 便于堆叠多层卷积，保持特征图大小  | 深度 CNN 中常用        |
| 全填充   | Full Padding        | 补充较多边界，使卷积核只要和输入有一点重叠就计算 | 输出尺寸比输入更大         | 信号处理里较常见，CNN 中较少用 |
| 复制填充  | Replication Padding | 用边缘像素值向外复制               | 边缘过渡更自然，不会引入 0 边界 | 图像处理任务            |
| 反射填充  | Reflection Padding  | 用边缘附近像素镜像填充              | 边缘连续性较好，减少边界伪影    | 图像生成、风格迁移、超分辨率    |
| 循环填充  | Circular Padding    | 把图像看成首尾相接，用另一侧像素填充       | 适合周期性数据           | 周期信号、特殊图像任务       |


**池化：** 在局部区域中提取代表性信息，从而减少特征图尺寸，降低计算量，并增强模型对局部位置变化的鲁棒性

| 池化方式   | 英文                     | 做法             | 特点                    | 常见用途        |
| ------ | ---------------------- | -------------- | --------------------- | ----------- |
| 最大池化   | Max Pooling            | 取局部区域中的最大值     | 保留最强特征响应，突出边缘、纹理等明显特征 | CNN 中最常用    |
| 平均池化   | Average Pooling        | 取局部区域的平均值      | 保留整体平滑信息，特征更均衡        | 图像分类、早期 CNN |
| 全局平均池化 | Global Average Pooling | 对整张特征图每个通道求平均  | 大幅减少参数量，可代替全连接层       | 现代 CNN 分类网络 |
| 全局最大池化 | Global Max Pooling     | 对整张特征图每个通道取最大值 | 保留每个通道最强响应            | 目标检测、特征提取   |
| 随机池化   | Stochastic Pooling     | 按概率随机选择池化区域中的值 | 有一定正则化效果              | 较少使用        |
| Lp 池化  | Lp Pooling             | 对区域内值做 Lp 范数计算 | 介于最大池化和平均池化之间         | 较少使用        |

### 2. LeNet-5网络

![LeNet-5网络](assets/img/posts/notes/machine_learning/3.png)

| 层      | 类型   | 输出尺寸                     | 说明                    |
| ------ | ---- | ------------------------ | --------------------- |
| Input  | 输入层  | $32 \times 32$           | 输入灰度图像                |
| C1     | 卷积层  | $6 \times 28 \times 28$  | 6 个 $5 \times 5$ 卷积核  |
| S2     | 池化层  | $6 \times 14 \times 14$  | $2 \times 2$ 池化，下采样   |
| C3     | 卷积层  | $16 \times 10 \times 10$ | 16 个 $5 \times 5$ 卷积核 |
| S4     | 池化层  | $16 \times 5 \times 5$   | $2 \times 2$ 池化       |
| C5     | 卷积层  | $120 \times 1 \times 1$  | 相当于全连接到 120 个神经元      |
| F6     | 全连接层 | $84$                     | 84 个神经元               |
| Output | 输出层  | $10$                     | 对应 10 个数字类别           |

#### 如何理解卷积核的尺寸

卷积核的完整尺寸不仅包括空间大小 

$$K_h \times K_w$$

还包括输入通道数，因此一个卷积核组的实际尺寸是

$$
C_{in} \times K_h \times K_w
$$

而有多少个输出通道，就有多少个这样的卷积核组。

### 3. AlexNet

![AlexNet](assets/img/posts/notes/machine_learning/4.png)

| 层     | 类型   | 主要参数                             | 作用                |
| ----- | ---- | -------------------------------- | ----------------- |
| Input | 输入层  | $227 \times 227 \times 3$        | 输入 RGB 彩色图像       |
| Conv1 | 卷积层  | 96 个 $11 \times 11$ 卷积核，stride=4 | 提取低级特征            |
| Pool1 | 最大池化 | $3 \times 3$，stride=2            | 降低尺寸              |
| Conv2 | 卷积层  | 256 个 $5 \times 5$ 卷积核           | 提取更复杂特征           |
| Pool2 | 最大池化 | $3 \times 3$，stride=2            | 降低尺寸              |
| Conv3 | 卷积层  | 384 个 $3 \times 3$ 卷积核           | 提取高级特征            |
| Conv4 | 卷积层  | 384 个 $3 \times 3$ 卷积核           | 提取高级特征            |
| Conv5 | 卷积层  | 256 个 $3 \times 3$ 卷积核           | 提取高级特征            |
| Pool5 | 最大池化 | $3 \times 3$，stride=2            | 得到较小特征图           |
| FC6   | 全连接层 | 4096 个神经元                        | 综合特征              |
| FC7   | 全连接层 | 4096 个神经元                        | 综合特征              |
| FC8   | 输出层  | 1000 个神经元                        | ImageNet 1000 类分类 |

**暂退法：** 训练时，随机让一部分神经元暂时不参与计算；测试时，所有神经元都正常参与计算。防止模型过拟合，提高模型的泛化能力

### 4.VCG网络

![VCG网络](assets/img/posts/notes/machine_learning/5.png)

| 阶段    | 网络层          | 输出通道数 | 输出尺寸变化             |
| ----- | ------------ | ----- | ------------------ |
| 输入    | Input        | 3     | $$224 \times 224$$ |
| 第 1 组 | Conv 3×3 × 2 | 64    | $$224 \times 224$$ |
|       | Max Pooling  | 64    | $$112 \times 112$$ |
| 第 2 组 | Conv 3×3 × 2 | เ128  | $$112 \times 112$$ |
|       | Max Pooling  | 128   | $$56 \times 56$$   |
| 第 3 组 | Conv 3×3 × 3 | 256   | $$56 \times 56$$   |
|       | Max Pooling  | 256   | $$28 \times 28$$   |
| 第 4 组 | Conv 3×3 × 3 | 512   | $$28 \times 28$$   |
|       | Max Pooling  | 512   | $$14 \times 14$$   |
| 第 5 组 | Conv 3×3 × 3 | 512   | $$14 \times 14$$   |
|       | Max Pooling  | 512   | $$7 \times 7$$     |
| 分类部分  | 全连接层         | 4096  | -                  |
|       | 全连接层         | 4096  | -                  |
| 输出层   | 全连接层         | 1000  | ImageNet 1000 类    |

>VCG网络证明了用更深的网络和连续的小卷积核，可以得到更强的特征提取能力。
{: .prompt-info}

在卷积层之后，通常还会有**激活层**

| 网络      | 是否使用激活函数 | 常用激活函数         | 说明                           |
| ------- | -------- | -------------- | ---------------------------- |
| LeNet-5 | 使用       | Sigmoid / Tanh | 早期 CNN，原始版本常用 Sigmoid 或 Tanh |
| AlexNet | 使用       | ReLU           | AlexNet 的重要改进之一就是大量使用 ReLU   |
| VGG     | 使用       | ReLU           | VGG 中几乎每个卷积层后面都会接 ReLU       |
| 输出层     | 使用或隐含使用  | Softmax        | 分类任务中通常用 Softmax 得到类别概率      |

### 5. 内容表示与风格表示

设提取内容的模型为 $f_c$，输入图像的矩阵为 $X$，内容图像的矩阵为 $C$，我们直接用平方误差作为内容上的损失：

$$
\mathcal{L}_c(X)
=
\frac{1}{2}
\left\|
f_c(X)-f_c(C)
\right\|_F^2
$$

假设某一层卷积网络输出的特征图为：

$$
F \in \mathbb{R}^{C \times H \times W}
$$

其中：

- $C$：通道数，也就是有多少张特征图
- $H$：特征图高度
- $W$：特征图宽度

通常会先把空间维度展平：

$$
F \in \mathbb{R}^{C \times HW}
$$

然后计算格拉姆矩阵：

$$
G = FF^T
$$

此时：

$$
G \in \mathbb{R}^{C \times C}
$$

格拉姆矩阵中的元素为：

$$
G_{ij}
=
\sum_{k=1}^{HW}
F_{ik}F_{jk}
$$

这里：

- $i$：第 $i$ 个通道
- $j$：第 $j$ 个通道
- $k$：空间位置
- $F_{ik}$：第 $i$ 个通道在第 $k$ 个位置的特征值

所以 $G_{ij}$ 表示：

> 第 $i$ 个通道和第 $j$ 个通道在整张特征图上的共同响应程度。


所以第$i$个卷积层上风格损失函数为

$$
\mathcal{L}_s^{(i)}(X)
=
\frac{1}{4N_{(i)}^2M_{(i)}^2}
\left\|
G_X^{(i)}-G_s^{(i)}
\right\|_F^2
$$

不同卷积层之间加权平均得

$$
\mathcal{L}_s(X)
=
\sum_i w_i\mathcal{L}_s^{(i)}(X)
$$

所以总的损失函数为

$$
\mathcal{L}(X)
=
\mathcal{L}_c(X)
+
\lambda \mathcal{L}_s(X)
$$

### 6. 数据增强

| 数据增强方式 | 英文                    | 具体做法                            | 作用                | 注意事项                |
| ------ | --------------------- | ------------------------------- | ----------------- | ------------------- |
| 随机裁剪   | Random Crop           | 从原图中随机截取一块区域作为输入                | 增强模型对目标位置变化的适应能力  | 裁剪不能把关键目标完全裁掉       |
| 中心裁剪   | Center Crop           | 从图像中心裁剪固定大小区域                   | 常用于验证集或测试集预处理     | 训练时一般不如随机裁剪丰富       |
| 随机翻转   | Random Flip           | 水平或垂直翻转图像                       | 增加样本多样性，提升泛化能力    | 数字、文字、医学图像中要谨慎使用    |
| 随机旋转   | Random Rotation       | 将图像随机旋转一定角度                     | 增强模型对角度变化的鲁棒性     | 旋转角度过大会改变类别含义       |
| 随机缩放   | Random Rescale / Zoom | 放大或缩小图像                         | 增强模型对目标大小变化的适应能力  | 缩放过大会丢失细节           |
| 平移变换   | Translation           | 图像在水平或竖直方向移动                    | 增强模型对目标位置偏移的鲁棒性   | 边界区域通常需要填充          |
| 仿射变换   | Affine Transform      | 旋转、缩放、平移、错切等组合变换                | 模拟拍摄角度和形状变化       | 变换过强会使图像失真          |
| 颜色抖动   | Color Jitter          | 随机改变亮度、对比度、饱和度、色相               | 增强模型对光照和颜色变化的适应能力 | 对颜色敏感任务要谨慎          |
| 随机灰度化  | Random Grayscale      | 随机把彩色图像转为灰度图                    | 减少模型对颜色的过度依赖      | 如果颜色是重要特征，不宜过多使用    |
| 加噪声    | Gaussian Noise        | 向图像加入随机噪声                       | 提高模型对噪声干扰的鲁棒性     | 噪声过大会破坏图像内容         |
| 模糊处理   | Blur                  | 使用高斯模糊、运动模糊等                    | 模拟拍摄模糊，提高鲁棒性      | 模糊过强会丢失边缘细节         |
| 随机擦除   | Random Erasing        | 随机遮挡图像中的一块区域                    | 减少模型对局部区域的依赖      | 遮挡区域不能过大            |
| Cutout | Cutout                | 在图像中随机挖掉一个方块区域                  | 类似随机擦除，增强鲁棒性      | 适合分类任务              |
| Mixup  | Mixup                 | 将两张图像按比例混合，标签也按比例混合             | 提高模型泛化能力，缓解过拟合    | 标签不再是单一类别           |
| CutMix | CutMix                | 把一张图像的一块区域替换成另一张图像的区域，标签按区域比例混合 | 同时保留局部信息和混合标签     | 实现比 Mixup 稍复杂       |
| 标准化    | Normalize             | 对图像像素做均值和标准差归一化                 | 加快训练收敛，使输入分布更稳定   | 严格来说属于预处理，但常和增强一起使用 |


## 五、循环神经网络(RNN)

### 1.循环神经网络的基本原理

对于具有序列特征的数据，我们使用循环神经网络，它通过隐藏状态把前面时间步的信息传递到后面，从而建模数据中的时间依赖关系

在这里，我们引入隐藏状态$h_t$，而从隐藏状态到输出$y_t$之间一般要再进行一次线性变换

$$
h_t
=
f_h
\left(
W_h h_{t-1}
+
W_i x_t
+
b_i
\right)
$$

根据求导的链式法则得

$$
\frac{\partial \mathcal{L}_t}{\partial W_i}
=
\frac{\partial \mathcal{L}_t}{\partial y_t}
\frac{\partial y_t}{\partial h_t}
\left(
x_t
+
\sum_{j=1}^{t-1}
\left(
\prod_{k=j+1}^{t}
f_h' W_h
\right)
x_j
\right)
$$

由于梯度中存在一些连乘项，所以可能会出现**梯度消失**和**梯度爆炸**

### 2.门控循环单元(GRU)

| 门   | 英文          | 作用                    |
| --- | ----------- | --------------------- |
| 更新门 | Update Gate | 控制保留多少旧记忆，以及更新多少新记忆   |
| 重置门 | Reset Gate  | 控制在生成候选记忆时，要不要使用过去的信息 |

$$
z_t
=
\sigma
\left(
W_z x_t
+
U_z h_{t-1}
+
b_z
\right)
$$

$$
r_t
=
\sigma
\left(
W_r x_t
+
U_r h_{t-1}
+
b_r
\right)
$$

利用重置单元 $r_t$，我们对过去的信息 $h_{t-1}$ 进行选择性遗忘：

$$
h'_{t-1}=r_t \odot h_{t-1}
$$

其中，$\odot$ 称为阿达马积（Hadamard product），表示向量或矩阵的逐元素相乘。例如，形状均为 $m \times n$ 的矩阵 $A$ 和 $B$ 的阿达马积为：

$$
A \odot B
=
\begin{bmatrix}
a_{11}b_{11} & a_{12}b_{12} & \cdots & a_{1n}b_{1n} \\
a_{21}b_{21} & a_{22}b_{22} & \cdots & a_{2n}b_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1}b_{m1} & a_{m2}b_{m2} & \cdots & a_{mn}b_{mn}
\end{bmatrix}
$$

当 $r_t$ 某一维度的值接近 0 时，网络就更倾向于遗忘 $h_{t-1}$ 的相应维度；反之，当 $r_t$ 某一维度的值接近 1 时，网络更倾向于保留 $h_{t-1}$ 的相应维度。之后，我们再将重置过的 $h'_{t-1}$ 与 $x_t$ 组合，得到 $\hat{h}_t$：

$$
\hat{h}_t
=
\tanh
\left(
W_hx_t
+
U_hh'_{t-1}
+
b_h
\right)
$$

最后，我们要决定 $h_t$ 是倾向于旧的信息 $h_{t-1}$，还是倾向于旧信息与新输入 $x_t$ 的混合 $\hat{h}_t$。利用更新单元 $z_t$，我们令：

$$
h_t
=
z_t \odot h_{t-1}
+
(1-z_t)\odot \hat{h}_t
$$


**为什么能够解决梯度消失？**
加法结构能使旧状态可以比较直接地传递到新状态。如果网络认为某些信息很重要，就可以让门控值接近 1，使信息沿时间方向保存更久。因此，梯度也更容易沿着这条路径向前传回去
