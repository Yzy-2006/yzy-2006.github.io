---
title: 机器学习 第1章 机器学习基础
description: 机器学习第1章笔记
author: 阎梓瑜
date: 2026-07-17 13:00:00 +0800
categories: [笔记,机器学习]
tags: [机器学习]
pin: false
math: true
mermaid: true
---

## 一、机器学习的数学基础

### 1. 向量（Vector）

向量（vector）是具有大小和方向的数学对象。

在机器学习中，通常使用向量表示一个样本：

$$
x=
\begin{bmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{bmatrix}
$$

其中：

- $x_i$ 表示第 $i$ 个特征
- $n$ 表示特征维度



#### 1.1 向量运算



$$
x+y=
(x_1+y_1,x_2+y_2,\cdots,x_n+y_n)
$$

$$
ax=
(ax_1,ax_2,\cdots,ax_n)
$$

$$
x\cdot y=
\sum_{i=1}^{n}x_i y_i
$$


$$
x\cdot y=x^Ty
$$


#### 1.2 向量范数（Norm）

**L2范数**

最常用的欧几里得距离：

$$
||x||_2=
\sqrt{\sum_{i=1}^{n}x_i^2}
$$

**L0范数**

表示向量中非零元素的个数，常用于衡量向量的稀疏程度：

$$
||x||_0=
\#\{i\mid x_i\ne0\}
$$

严格来说，L0 范数并不是数学意义上的范数。

**L1范数**


定义：

$$
||x||_1=
\sum_{i=1}^{n}|x_i|
$$


表示各维度绝对值之和。

**L∞范数**


定义：

$$
||x||_\infty=
\max_i |x_i|
$$


表示向量中最大的绝对值。


---

### 2. 矩阵（Matrix）


机器学习中：

数据集通常表示为矩阵：

$$
X=
\begin{bmatrix}
x_1^T\\
x_2^T\\
\vdots\\
x_n^T
\end{bmatrix}
$$


其中：

- 每一行是一个样本
- 每一列是一种特征


#### 2.1 矩阵运算


**矩阵加法**

$$
A+B=C
$$


$$
c_{ij}=a_{ij}+b_{ij}
$$


**矩阵乘法**


$$
A\in R^{m\times n}
$$

$$
B\in R^{n\times k}
$$


$$
AB\in R^{m\times k}
$$


$$
c_{ij}
=
\sum_{l=1}^{n}a_{il}b_{lj}
$$


**转置矩阵**


$$
(A^T)_{ij}=A_{ji}
$$


$$
(AB)^T=B^TA^T
$$


**单位矩阵**


$$
I=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
$$


$$
AI=A
$$


**矩阵的逆**


$$
AA^{-1}=A^{-1}A=I
$$


$$
A^{-1}
$$

$$
Ax=b
$$


$$
A^{-1}
$$

$$
x=A^{-1}b
$$


机器学习中的应用：

线性回归解析解：

$$
\theta=(X^TX)^{-1}X^Ty
$$


---

### 3. 梯度（Gradient）


梯度表示函数变化最快的方向。


对于函数：

$$
f(x)
$$


梯度：

$$
\nabla f(x)
=
\begin{bmatrix}
\frac{\partial f}{\partial x_1}\\
\frac{\partial f}{\partial x_2}\\
\vdots\\
\frac{\partial f}{\partial x_n}
\end{bmatrix}
$$


含义：

梯度方向：

- 函数增长最快

负梯度方向：

- 函数下降最快


因此梯度下降算法：

$$
\theta
=
\theta-\alpha\nabla J(\theta)
$$


其中：

- $\theta$：模型参数
- $\alpha$：学习率
- $J(\theta)$：损失函数


#### 黑塞矩阵（Hessian Matrix）

对于二阶可导的标量函数 $f(x)$，黑塞矩阵由所有二阶偏导数组成：

$$
x=
\begin{bmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{bmatrix}
$$

$$
H_f(x)=\nabla^2 f(x)
=
\begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2}
&\frac{\partial^2 f}{\partial x_1\partial x_2}
&\cdots
&\frac{\partial^2 f}{\partial x_1\partial x_n}\\
\frac{\partial^2 f}{\partial x_2\partial x_1}
&\frac{\partial^2 f}{\partial x_2^2}
&\cdots
&\frac{\partial^2 f}{\partial x_2\partial x_n}\\
\vdots&\vdots&\ddots&\vdots\\
\frac{\partial^2 f}{\partial x_n\partial x_1}
&\frac{\partial^2 f}{\partial x_n\partial x_2}
&\cdots
&\frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}
$$

黑塞矩阵描述函数的二阶变化率，也就是函数曲面的曲率：

$$
(H_f(x))_{ij}
=
\frac{\partial^2 f}{\partial x_i\partial x_j}
$$

当二阶偏导连续时：

$$
H_f(x)^T=H_f(x)
$$

在优化中，牛顿法利用黑塞矩阵修正梯度下降的方向和步长：

$$
x_{k+1}
=
x_k-H_f(x_k)^{-1}\nabla f(x_k)
$$


---


### 4. 凸函数（Convex Function）


凸函数表示：

函数曲线中任意两点连线都位于函数上方。


数学定义：

对于任意：

$$
0\leq\lambda\leq1
$$


满足：

$$
f(\lambda x_1+(1-\lambda)x_2)
\leq
\lambda f(x_1)+(1-\lambda)f(x_2)
$$


特点：

- 局部最优一定是全局最优
- 优化更加容易


---

## 二、k近邻算法

**核心思想：** 让当前样本服从邻居中的多数来进行分类

### 1. 用KNN算法完成分类

统计k个邻居中出现最多的类别

```py
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
# 数据
X = np.array([
    [1, 1],
    [2, 2],
    [3, 3],
    [6, 6],
    [7, 7],
    [8, 8]
])
y = np.array([0, 0, 0, 1, 1, 1])
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0
)
# 创建KNN分类器
knn = KNeighborsClassifier(
    n_neighbors=3
)
# 训练
knn.fit(X_train, y_train)
# 预测
y_pred = knn.predict(X_test)
# 评价
print("Accuracy:", accuracy_score(y_test, y_pred))
```

### 2. 用KNN算法完成回归

对k个邻居对应的值进行加权平均

```py
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
# 数据
X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
])
y = np.array([
    10,
    20,
    30,
    40,
    50,
    60
])
# 划分数据
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0
)
# 创建KNN回归器
knn = KNeighborsRegressor(
    n_neighbors=3
)
# 训练
knn.fit(X_train, y_train)
# 预测
y_pred = knn.predict(X_test)
# 评价
print("MSE:", mean_squared_error(y_test, y_pred))
```
### 3. 一些小巧思

1. 在使用knn回归来进行色彩风格迁移的时候，因为单个像素包含的信息太少，所以我们可以使用一个窗口

 ---

## 三、线性回归

### 1.线性回归的映射形式和学习目标

$$
f_\theta(x)=\theta^Tx
$$

$$
J(\theta)=\frac{1}{N}\sum_{i=1}^{N}\mathcal{L}(y_i,f_\theta(x_i))
$$

$$
\mathcal{L}(y_i,f_\theta(x_i))
=
\frac{1}{2}(y_i-f_\theta(x_i))^2
$$

### 2.线性回归的解析方法

$$
\theta=(X^{T}X)^{-1}X^{T}y
$$

$$
f_\theta(X)=X\theta=X(X^{T}X)^{-1}X^{T}y
$$

```py
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# 构造数据
X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
])
y = np.array([
    3,
    5,
    7,
    9,
    11,
    13
])
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=0
)
# 创建线性回归模型
model = LinearRegression()
# 模型训练
model.fit(
    X_train,
    y_train
)
# 预测
y_pred = model.predict(
    X_test
)
# 模型评价
mse = mean_squared_error(
    y_test,
    y_pred
)
print("预测结果:", y_pred)
print("均方误差:", mse)
# 查看模型参数
print("权重 theta:", model.coef_)
print("偏置 b:", model.intercept_)
```

### 3. 梯度下降(GD)算法

$$
\theta=\theta-\frac{\eta}{N}X^T(f_\theta(X)-y)
$$

由于样本量很大时，矩阵向量乘法很耗时，同时矩阵的存储也比较困难，所以我们可以每次只选择一个样本来计算梯度，称为**随机梯度下降(SGD)**

$$
\theta \leftarrow \theta-\eta(\theta^{T}x_k-y_k)x_k
$$

但是这样做会引入随机性，为了在随机性和时间复杂度之间取得平衡，我们通常使用**小批量梯度下降(MBGD)**

$$
\theta \leftarrow
\theta-\frac{\eta}{B}
X_{(i)}^{T}
\left(
f_\theta(X_{(i)})-y_{(i)}
\right)
$$

---

## 四、机器学习的基本思想

### 1. 欠拟合与过拟合

**欠拟合：** 训练损失和测试损失都较大

1. 模型复杂度小于数据本身复杂度
2. 迭代次数较少或学习率过低

**过拟合：** 训练损失小和测试损失大

1. 模型复杂度大于数据复杂度
2. 梯度下降迭代次数太大

### 2. 正则化约束

**正则化：** 对参数的复杂度进行约束的方法

$$
J(\theta)
=
\frac{1}{2}
(y-X\theta)^{T}(y-X\theta)
+
\frac{\lambda}{2}
\|\theta\|_{2}^{2}
$$

$$
\theta
=
(X^{T}X+\lambda I)^{-1}X^{T}y
$$

使用$L_2$正则化的线性回归称为**岭回归**

使用$L_1$范数对$L_0$范数进行近似正则化的线性回归称为**最小绝对值收敛和选择算子(LASSO)回归**

### 3. 输入特征与相似度

**特征映射函数：** 把原始的特征经过某种筛选或变换，得到更能反映样本本质的特征

$$
\Phi
=
\left[
\begin{array}{c}
\phi(x_1)^T\\
\phi(x_2)^T\\
\vdots\\
\phi(x_n)^T
\end{array}
\right]
=
\left[
\begin{array}{cccc}
\phi_1(x_1)&\phi_2(x_1)&\cdots&\phi_h(x_1)\\
\phi_1(x_2)&\phi_2(x_2)&\cdots&\phi_h(x_2)\\
\vdots&\vdots&\ddots&\vdots\\
\phi_1(x_n)&\phi_2(x_n)&\cdots&\phi_h(x_n)
\end{array}
\right]
$$

**核技巧：** 不显式计算高维映射，而直接计算高维空间中的内积

**核矩阵**

$$
K=\Phi\Phi^T
$$

**核函数**

$$
K(x_i,x_j)=\phi(x_i)^T\phi(x_j)
$$

### 4. 参数与超参数

**超参数：** 需要人为指定的参数

### 5.数据集划分与交叉验证

1. 对数据集中的数据进行标准化时，只用训练集计算均值和方差等信息
2. 训练集与测试集的数据分布相同
3. 交叉验证：每次用不同的数据作为验证集，求误差平均值作为最终误差