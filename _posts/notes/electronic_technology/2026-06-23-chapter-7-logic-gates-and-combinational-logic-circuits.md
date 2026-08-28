---
title: 电子技术第7章笔记 门电路和组合逻辑电路
description: 电子技术第7章笔记
author: 阎梓瑜
date: 2026-06-23 18:30:00 +0800
categories: [笔记,电子技术]
tags: [电子技术]
pin: false
math: true
mermaid: true
---

## 1.数字电路基础

### 1-1 数制和码制

**格雷码：**相邻两个编码只有一位不同，相邻两个编码只有一位不同

### 1-2 逻辑代数

#### 逻辑代数关系

| 逻辑关系 | 表达式                     | 特点              |
| ---- | ----------------------- | --------------- |
| 与    | $Y=A\cdot B$            | 有 0 出 0，全 1 出 1 |
| 或    | $Y=A+B$                 | 有 1 出 1，全 0 出 0 |
| 非    | $Y=\overline{A}$        | 0 变 1，1 变 0     |
| 与非   | $Y=\overline{A\cdot B}$ | 有 0 出 1，全 1 出 0 |
| 或非   | $Y=\overline{A+B}$      | 有 1 出 0，全 0 出 1 |
| 异或   | $Y=A\oplus B$           | 相同出 0，不同出 1     |
| 同或   | $Y=A\odot B$            | 相同出 1，不同出 0     |

#### 逻辑代数运算法则

| 类型    | 公式                                                                                  |
| ----- | ----------------------------------------------------------------------------------- |
| 0、1 律 | $A+0=A,\ A\cdot1=A,\ A+1=1,\ A\cdot0=0$                                             |
| 重叠律   | $A+A=A,\ A\cdot A=A$                                                                |
| 互补律   | $A+\overline{A}=1,\ A\overline{A}=0$                                                |
| 双重否定律 | $\overline{\overline{A}}=A$                                                         |
| 交换律   | $A+B=B+A,\ AB=BA$                                                                   |
| 结合律   | $A+(B+C)=(A+B)+C,\ A(BC)=(AB)C$                                                     |
| 分配律   | $A(B+C)=AB+AC,\ A+BC=(A+B)(A+C)$                                                    |
| 吸收律   | $A+AB=A,\ A(A+B)=A$                                                                 |
| 德摩根定律 | $\overline{A+B}=\overline{A}\overline{B},\ \overline{AB}=\overline{A}+\overline{B}$ |

####  逻辑代数定理

**代入定理：**在一个已经成立的逻辑等式中，如果用同一个逻辑函数去代替等式中某个变量，则等式仍然成立。

**对偶定理：**如果一个逻辑等式成立，那么把等式中的“与”和“或”互换，0 和 1 互换后，所得的新等式也成立。

**反演定理：**在逻辑代数中，要求一个逻辑函数的反函数时，可以把原函数中的：
与变成或，或变成与；
0 变成 1，1 变成 0；
原变量变成反变量，反变量变成原变量。
这样得到的新表达式，就是原逻辑函数的反函数。

#### 逻辑函数的表示方式

| 表示方法      | 说明            |
| --------- | ------------- |
| 真值表 / 状态表 | 列出所有输入组合和对应输出 |
| 逻辑表达式     | 用与、或、非等运算表示   |
| 逻辑图       | 用门电路符号表示      |
| 卡诺图       | 用图形方法化简逻辑函数   |

#### 逻辑函数的化简

**公式法**

**卡诺图法**

任意两个相邻最小项之间只有一个变量改变

## 2.集成门电路

### 2-1 逻辑门电路的基本概念

门电路是数字电路中最基本的逻辑元件，它按照一定逻辑条件控制信号通过或不通过

### 2-2 分立元件基本逻辑门电路

#### 二级管”与“门电路

![](assets/img/posts/notes/electronic_technology/chapter7/7-1.png){:.w-25}

![](assets/img/posts/notes/electronic_technology/chapter7/7-2.png){:.w-25}


#### 二级管”或“门电路

![](assets/img/posts/notes/electronic_technology/chapter7/7-3.png){:.w-25}

![](assets/img/posts/notes/electronic_technology/chapter7/7-4.png){:.w-25}


#### 二级管”非“门电路

![](assets/img/posts/notes/electronic_technology/chapter7/7-5.png){:.w-25}

![](assets/img/posts/notes/electronic_technology/chapter7/7-6.png){:.w-25}

### 2-3 基本逻辑门电路的组合

#### 与非

![](assets/img/posts/notes/electronic_technology/chapter7/7-7.png){:.w-50}

#### 或非

![](assets/img/posts/notes/electronic_technology/chapter7/7-8.png){:.w-50}

#### 异或

![](assets/img/posts/notes/electronic_technology/chapter7/7-9.png){:.w-25}

#### 同或

![](assets/img/posts/notes/electronic_technology/chapter7/7-10.png){:.w-25}

### 2-4 TTL门电路（三极管-三极管逻辑门电路）

TTL门电路与分立元件相比，具有速度快、可靠性高和微型化等优点

#### TTL与非门电路

![](assets/img/posts/notes/electronic_technology/chapter7/7-11.png){:.w-50}

扇出系数 $N_O$ 表示一个门电路最多能带动同类门输入端的数量，反映门电路的带负载能力。TTL 与非门中，输入高电平电流 $I_{IH}$ 是输入端为高电平时流入输入端的电流，通常较小；输入低电平电流 $I_{IL}$ 是输入端为低电平时流出输入端的电流，通常较大。实际扇出系数要同时考虑高、低电平时的驱动能力，一般取两种情况下允许带动门数的较小值。

#### 三态输出"与非"门

![](assets/img/posts/notes/electronic_technology/chapter7/7-12.png){:.w-50}

三态输出与非门是在普通与非门的基础上，增加了一个控制端，使输出端除了能输出高电平、低电平之外，还能进入第三种状态：**高阻态**

| 使能端 (EN) | 输入 (A,B) | 输出 (Y)  |
| -------- | -------- | ------- |
| 1        | 00       | 1       |
| 1        | 01       | 1       |
| 1        | 10       | 1       |
| 1        | 11       | 0       |
| 0        | 任意       | 高阻态 (Z) |

>EN = 1 时：正常与非门工作  
EN = 0 时：输出端断开，Y = Z

**三态门的应用：**可以实现一条总线分时传送几个不同的数据或控制信号

## 3.组合逻辑电路的分析与综合

**组合逻辑电路：** 任何时刻电路的输出状态只取决于该时刻的输入状态，而与该时刻以前的电路状态无关

## 4.加法器

**加法器：**实现二进制加法运算的电路

**半加器：**不考虑低位来的进位

**全加器：**考虑低位来的进位

### 4-1 半加器

![](assets/img/posts/notes/electronic_technology/chapter7/7-13.png){:.w-50}

### 4-2 全加器

![](assets/img/posts/notes/electronic_technology/chapter7/7-14.png){:.w-50}

### 4-3 串行进位加法器

![](assets/img/posts/notes/electronic_technology/chapter7/7-15.png){:.w-50}

## 5. 编码器

**编码：**把二进制码按一定规律编排，使每组代码具有特定的含义

### 5-1 8线-3线编码器

![](assets/img/posts/notes/electronic_technology/chapter7/7-16.png){:.w-50}

### 5-2 优先编码器

允许几个信号同时有效，但电路只对其中优先级别高的信号进行编码，而对其它优先级别低的信号不予理睬。

优先编码器通常由两部分组成：

1. **优先排队电路**
2. **普通编码器**

其中，优先排队电路的作用是：当多个输入同时有效时，只允许优先级最高的信号送入后面的普通编码器。

优先排队电路的输出可写为：

$$
A=A_0\overline{A_1}\overline{A_2}\overline{A_3}
$$

$$
B=A_1\overline{A_2}\overline{A_3}
$$

$$
C=A_2\overline{A_3}
$$

$$
D=A_3
$$

因此，对应的编码关系为：

| 输入状态 | 输出 $B_1B_0$ |
|---|---|
| $0001$ | $00$ |
| $001X$ | $01$ |
| $01XX$ | $10$ |
| $1XXX$ | $11$ |

## 6.译码器

译码：编码的反过程，将代码的组合译成一个特定的输出信号

## 7.数据分配器和数据选择器

在数字电路中，当需要进行远距离多路数字传输时，为了减少传输线的数目，发送端常通过一条公共传输线，用多路选择器分时发送数据到接收端，接收端利用多路分配器分时将数据分配给各路接收端。

### 7-1 数据选择器

![](assets/img/posts/notes/electronic_technology/chapter7/7-17.png){:.w-50}

### 7-2 数据分配器

![](assets/img/posts/notes/electronic_technology/chapter7/7-18.png){:.w-50}
