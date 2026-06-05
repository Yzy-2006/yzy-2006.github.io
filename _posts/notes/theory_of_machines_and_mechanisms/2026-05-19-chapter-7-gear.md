---
title: 机械原理 第7章 齿轮机构及其设计
description: 机械原理第7章笔记
author: 阎梓瑜
date: 2026-05-19 16:00:00 +0800
categories: [笔记,机械原理]
tags: [机械原理]
pin: false
math: true
mermaid: true
---

# 7-1 齿轮机构的类型和应用

1. 平行轴齿轮机构
2. 相交轴齿轮机构
3. 交错轴齿轮机构
# 7-2 瞬时传动比与齿廓曲线

## 一、齿廓啮合基本定律

对于整周来说，两齿轮的传动比总等于齿数的反比，即$\frac{n_1}{n_2}=\frac{z_2}{z_1}$,但是瞬时传动比和齿廓的形状有关

![齿廓啮合基本定律](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-1.png)

**齿廓啮合基本定律：**具有任意齿廓的两齿轮啮合时，其瞬时角速度的比值等于接触点公法线将其中心距分成两段长度的反比，即$i_{12}=\frac{\omega_1}{\omega_2}=\frac{\overline{O_2C}}{\overline{O_1C}}$

相对速度瞬心$C$称为**啮合节点**，简称**节点**

为实现定传动比传动，要求$C$为中心线上的一个固定点，$C$在两轮各自运动平面内的轨迹称为**相对瞬心线**，分别是以$O_1$,$O_2$为圆心的圆，称为齿轮的**节圆**，齿轮的啮合传动相当于两个节圆作无滑动的纯滚动

## 二、共轭齿廓的形成

**共轭齿廓:**满足齿廓基本啮合定律的传动比为常数或按一定规律变化的一对齿廓

共轭齿廓啮合时，两齿廓在啮合点相切，其啮合点的公法线过节点$C$

# 7-3 渐开线和渐开线齿廓啮合传动的特点

## 一、渐开线和渐开线方程

### 1.渐开线及其性质

![渐开线](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-5.png)

当直线 $x-x$ 沿半径为 $r_b$ 的圆作纯滚动时，该直线上任一点 $K$ 的轨迹称为该圆的**渐开线**，该圆称为渐开线的**基圆**，直线 $x-x$ 称为渐开线的**发生线**，角 $\theta_k$ 称为渐开线 $AK$ 段的**展角**

**渐开线的性质：**

1. $\overline{KN}=\overset{\frown}{AN}$
2. 渐开线上任一点的法线切于基圆
3. 基圆以内没有渐开线
4. 渐开线的形状仅取决于基圆大小
5. 同一基圆上，任意两条渐开线间的法向距离为定值

### 2.渐开线方程

根据渐开线的性质1

$$
r_b(\theta_k+\alpha_k)=\overset{\frown}{AN}
=\overline{KN}=r_b\tan\alpha_k
$$

$$
\theta_k=\tan\alpha_k-\alpha_k
$$

所以渐开线的**极坐标参数方程**为

$$
\left\{
\begin{aligned}
r_k&=\frac{r_b}{\cos\alpha_k}\\
\theta_k&=\operatorname{inv}\alpha_k=\tan\alpha_k-\alpha_k
\end{aligned}
\right.
$$

其中$\alpha_k$称为渐开线在$K$点的**压力角**；展角$\theta_k$称为压力角$\alpha_k$的**渐开线函数**，工程上常用$\operatorname{inv}\alpha_k$表示

## 二、渐开线齿廓啮合传动的特点

![渐开线齿廓啮合传动](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-8.png)

1. 传动比恒定
2. 中心距不影响传动比
3. 啮合线是过节点的直线

$$
i_{12}
=
\frac{\omega_1}{\omega_2}
=
\frac{\overline{O_2C}}{\overline{O_1C}}
=
\frac{r_2'}{r_1'}
=
\frac{r_{b2}}{r_{b1}}
$$

**啮合线：**一对齿轮啮合过程中，齿轮啮合点在固定坐标系中的轨迹

两渐开线齿轮基圆的内公切线$N_1 N_2$为渐开线齿轮的**理论啮合线**，$N_1$和$N_2$称为**极限啮合点**，啮合线$N_1 N_2$与中心连线$O_1 O_2$的垂线间的夹角称为**啮合角**$\alpha'$，它是渐开线齿廓在节点$C处的压力角。

# 7-4 渐开线圆柱齿轮及其基本参数与几何尺寸

![渐开线圆柱齿轮参数](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-9.png)

## 一、齿轮的各部分名称

**齿顶圆**  
过齿轮各轮齿顶端的圆，其直径用 $d_a$、半径用 $r_a$ 表示。

**齿根圆**  
与齿轮各轮齿齿槽底部相切的圆，其直径用 $d_f$、半径用 $r_f$ 表示。

**齿厚**  
任意圆周上一个轮齿的两侧齿廓间的弧线长度称为该圆上的齿厚，用 $s_i$ 表示。

**齿槽宽**  
相邻两齿间的空间称为齿槽，任意圆周上齿槽两侧齿廓间的弧线长度称为该圆上的齿槽宽，用 $e_i$ 表示。

**齿距（周节）**  
任意圆周上相邻两齿同侧齿廓间的弧线长度称为齿距，或称周节，用 $p_i$ 表示，有$p_i=s_i+e_i$

**分度圆**  
为设计和制造的方便而规定的一个参考圆，用它作为度量齿轮尺寸的基准圆，其直径用 $d$、半径用 $r$ 表示。规定标准齿轮分度圆上的齿厚 $s$ 与齿槽宽 $e$ 相等，即$s=e=\frac{1}{2}p$

**齿顶高**  
位于齿顶圆与分度圆之间的轮齿部分称为齿顶。齿顶部分的径向高度称为齿顶高，用 $h_a$ 表示。

**齿根高**  
位于齿根圆与分度圆之间的轮齿部分称为齿根。齿根部分的径向高度称为齿根高，用 $h_f$ 表示。

**全齿高**  
齿顶圆与齿根圆之间的径向距离，用 $h$ 表示。有$h=h_a+h_f$

## 二、渐开线齿轮的基本参数

### 1. 齿数

在齿轮的整圆周上的轮齿总数，用 $z$ 表示，$z$ 应为整数。

### 2. 模数

齿轮的分度圆是计算各部分尺寸的基准，其周长为 $\pi d = zp$，分度圆直径为

$$
d=\frac{p}{\pi}z
$$

式中，无理数 $\pi$ 对设计、制造和测量均不方便，为此，取 $p/\pi$ 为一个有理数列，称为模数，并用 $m$ 表示，即

$$
m=\frac{p}{\pi}
$$

模数 $m$ 是齿轮的一个基本参数，其单位为 $\text{mm}$。从而得

$$
\left\{
\begin{aligned}
p&=\pi m\\
d&=mz
\end{aligned}
\right.
$$

模数反映了齿轮的轮齿及各部分尺寸的大小。当齿数 $z$ 不变时，模数增大，其齿距、齿厚、齿高和分度圆直径都相应增大。

### 3. 分度圆压力角（齿形角）

渐开线齿廓上任一点 $K$ 处的压力角 $\alpha_k$：

$$
\alpha_k=\arccos(r_b/r_k)
$$

可见，对于同一渐开线齿廓，$r_k$ 不同，$\alpha_k$ 也不同，$r_k$ 越接近于基圆，$\alpha_k$ 就越小。基圆上的压力角为零。若用 $\alpha$ 表示分度圆上的压力角，则有

$$
\alpha=\arccos(r_b/r)
$$

或

$$
r_b=r\cos\alpha=\frac{1}{2}mz\cos\alpha
$$

可见，当齿轮的齿数 $z$ 和模数 $m$ 一定时，分度圆大小一定；若分度圆压力角 $\alpha$ 不同，其基圆大小就不同，渐开线齿廓的形状也就不同。因此，分度圆压力角 $\alpha$ 就成为决定渐开线齿廓形状的基本参数。

为设计、制造和检验的方便，国家标准中规定分度圆压力角 $\alpha$ 为标准值，$\alpha=20^\circ$

这样，渐开线齿轮的分度圆还可完整地定义如下：齿轮上具有标准模数和标准压力角的圆。

### 4. 其他齿形参数

**齿顶高系数 $h_a^*$**  
齿顶高 $h_a$ 与模数的比值，即

$$
h_a^*=\frac{h_a}{m}
$$

齿顶高

$$
h_a=h_a^*m
$$

两齿轮啮合时，为避免一个齿轮的齿顶与相啮合齿轮的齿槽底部干涉，应使两者之间留有一定的径向间隙，称为顶隙，用 $c$ 表示，故规定：

**顶隙系数 $c^*$**  
顶隙 $c$ 与模数的比值，即

$$
c^*=\frac{c}{m}
$$

顶隙

$$
c=c^*m
$$

齿根高

$$
h_f=(h_a^*+c^*)m
$$

齿顶高系数 $ h_a^* $ 和顶隙系数 $ c^* $ 均为标准值，其值由基本齿廓规定。

正常齿标准：

$$
h_a^*=1,\quad c^*=0.25
$$

## 三、渐开线标准直齿圆柱齿轮的几何尺寸

确定了基本参数之后，剩下的尺寸就可以按下表中的公式来进行计算

![渐开线标准直齿圆柱齿轮几何尺寸公式](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/sheet7-5.png)

# 7-5 渐开线标准直齿圆柱齿轮的啮合传动

## 一、一对渐开线齿轮的正确啮合条件

![渐开线齿轮啮合](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-12.png)

图中$K B_2$的长度即为齿轮的法向齿距$p_n$,亦为齿轮的基圆齿距$p_b$。齿轮的正确啮合条件为**两齿轮的基圆齿距相等**

>法向齿距是两齿轮公共的，基圆齿距是各自的
{: .prompt-info }

$$
p_b=\frac{\pi d_b}{z}
=\frac{\pi m z \cos\alpha}{z}
=\pi m\cos\alpha
$$

$$
m_1\cos\alpha_1=m_2\cos\alpha_2
$$

由于模数和分度圆压力角都已经标准化了，所以

$$
\left\{
\begin{aligned}
m_1&=m_2=m\\
\alpha_1&=\alpha_2=\alpha
\end{aligned}
\right.
$$

## 二、标准齿轮传动的中心矩和啮合角

**一对齿轮无侧隙啮合的几何条件：**一齿轮的节圆齿厚等于另一齿轮的节圆齿槽宽

一对标准齿轮，只要保证分度圆相切，就可以保证两齿轮间无侧隙啮合传动，此时两齿轮间的中心距为**标准中心距**

$$
a=r_1 + r_2 = \frac{1}{2} m (z_1 + z_2)
$$

两标准齿轮按标准中心距安装时称为**标准安装**，其啮合角$\alpha '$等于其分度圆压力角$\alpha$

>**标准齿轮：**模数$m$、分度圆压力角$\alpha$、齿顶高系数 $h_a^∗$​、顶隙系数$c^*$等参数均取标准值，且分度圆上齿厚等于齿槽宽的齿轮。
{: .prompt-info }

## 三、渐开线齿轮连续传动条件

### 1.重合度的基本概念

![重合度](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-14.png)

线段$B_1 B_2$称为**实际啮合线**，为保证传动的连续性，它的长度要大于基圆齿距$P_b$,二者的比值称为重合度

$$
\varepsilon_\alpha=\frac{\overline{B_1B_2}}{P_b}
$$

>$B_1$和$B_2$为齿顶圆和啮合线的交点
{: .prompt-info }

### 2.重合度的计算

***1）外啮合直齿圆柱齿轮***

$$
\varepsilon_\alpha
=
\frac{1}{2\pi}
\left[
z_1\left(\tan\alpha_{a1}-\tan\alpha'\right)
+
z_2\left(\tan\alpha_{a2}-\tan\alpha'\right)
\right]
$$

式中，$\alpha'$为啮合角，$\alpha_{a1}$、$\alpha_{a2}$分别为两齿轮的齿顶压力角

$$
\alpha_{a1}=\arccos\left(\frac{r_{b1}}{r_{a1}}\right),
\quad
\alpha_{a2}=\arccos\left(\frac{r_{b2}}{r_{a2}}\right)   
$$

***2）外啮合直齿圆柱齿轮***

$$
\varepsilon_\alpha
=
\frac{1}{2\pi}
\left[
z_1\left(\tan\alpha_{a1}-\tan\alpha'\right)
-
z_2\left(\tan\alpha_{a2}-\tan\alpha'\right)
\right]
$$

>1 号轮通常是小外齿轮，2 号轮通常是大内齿轮
{: .prompt-info }

***3）外啮合直齿圆柱齿轮***

$$
\varepsilon_\alpha
=
\frac{1}{2\pi}
\left[
z_1\left(\tan\alpha_{a1}-\tan\alpha'\right)
-
\frac{4h_a^*}{\sin 2\alpha}
\right]
$$

### 3.重合度的物理意义及影响因素

重合度的大小表明**同时参与啮合轮齿对数的平均值**

影响因素：

1. **齿顶高系数$h_a^*$:**增大齿顶高系数可以是实际啮合线加长从而增大重合度
2. **齿数：**，齿数增多可以使实际啮合线加长从而增大重合度
3. **啮合角$\alpha'$:**其他条件不变时，增大安装的中心距会使啮合角增大，重合度减小

# 7-6 渐开线齿廓的加工原理

## 一、仿形法

## 二、展成法

### 1.基本齿廓及刀锯齿形

![基本齿廓](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-21.png)

齿轮的齿数无穷多时，齿轮上的各个圆变成直线，变成齿条，称为齿轮的**基本齿廓**，主要特点为：

1. 齿条的同侧齿廓为平行直线，各点具有相同的压力角，即为其齿形角$\alpha$,等于齿轮的分度圆压力角
2. 与齿顶线平行的直线上具有相同的齿距$p=\pi m$
3. 与齿顶线平行且齿厚等于齿槽宽的直线称为分度线，是计算齿条尺寸的基准线

### 2.切削过程中的运动

![7-22](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-22.png)
![7-23](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-23.png)

### 3.滚齿加工的特点

切削连续，生产效率高

### 4.标准齿轮及变位齿轮的加工

![齿轮加工](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-25.png)

***1）标准齿轮加工***

齿条刀具的分度线与齿轮毛坯的分度圆相切作纯滚动时，加工出齿轮的分度圆等于刀具的齿形角$\alpha$

***2）变位齿轮加工***

使刀具的分度线距离轮坯分度圆为$xm$是加工出的齿轮称为**变位齿轮**，$x$称为**变位系数**，当刀具远离轮坯中心时，$x$为正值，称为正变位

**标准齿轮和变位齿轮的异同？**

**相同：**齿轮齿数、模数、压力角、齿距和基圆

**不同：**齿顶高、齿根高、齿厚和齿槽宽

![变位齿轮](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-26.png)

### 5.根切现象及其避免方法

***1）根切现象及产生原因***

**根切现象：**刀具齿顶把被加工齿轮根部的渐开线齿廓切去一部分，从而导致齿根强度和传动的重合度降低

**产生原因：**刀具齿顶线超过了极限啮合点

![根切产生原因](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-28.png)

***2）避免根切的方法***

$$
z_{\min}=\frac{2h_a^*}{\sin^2\alpha}
$$

$$
x_{\min}=h_a^*\frac{z_{\min}-z}{z_{\min}}
$$

1. 选用$z>z_{\min}$的齿数
2. 选用$x>x_{\min}$的变位齿轮
3. 改变齿形参数，但需要换刀具，所以一般不采用

# 7-7 渐开线变位直齿圆柱齿轮啮合传动计算

## 一、变位齿轮的齿厚及测量

### 1.分度圆的齿厚和齿槽宽

$$
s=m\left(\frac{\pi}{2}+2x\tan\alpha\right)
$$

$$
e=m\left(\frac{\pi}{2}-2x\tan\alpha\right)
$$

### 2.任意圆上的弧齿厚

![任意圆上的齿厚](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-30.png)

$$
s_i=s\frac{r_i}{r}-2r_i\left(\operatorname{inv}\alpha_i-\operatorname{inv}\alpha\right)
$$ 

### 3.齿厚的测量

![齿厚测量](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-31.png)

$$
W_k=(k-1)p_b+s_b
$$

$$
k=\frac{z}{180^\circ}\arccos\frac{z\cos\alpha}{z+2x}+0.5
$$

## 二、变位齿轮的啮合传动计算

### 1.齿轮传动的啮合角$\alpha'$——无侧隙啮合方程式

**啮合条件：**节圆齿距等于两齿轮的节圆齿厚之和

**无侧隙啮合方程式**

$$
\operatorname{inv}\alpha'
=
\operatorname{inv}\alpha
+
\frac{2(x_1+x_2)}{z_1+z_2}\tan\alpha
$$

### 2.中心距$a'$及中心距变动系数$y$

$$
a'
=
\frac{1}{2}m(z_1+z_2)\frac{\cos\alpha}{\cos\alpha'}
$$

$$
a'-(r_1+r_2)
=
a'-a
=
ym
=
a\left(\frac{\cos\alpha}{\cos\alpha'}-1\right)
$$

$$
y
=
\frac{1}{2}(z_1+z_2)
\left(
\frac{\cos\alpha}{\cos\alpha'}-1
\right)
=
\frac{a'-a}{m}
$$

### 3.齿顶高及齿顶高变动系数

要保证同时满足无侧隙啮合与标准顶隙条件，要将两齿轮的齿顶高各削去一段$\Delta y m$,$\Delta y$称为**齿顶高变动系数**

$$
\Delta y
=
x_1+x_2-y
$$

齿顶圆半径为

$$
r_a
=
\frac{mz}{2}
+
(h_a^*+x-\Delta y)m
$$

![圆柱齿轮传动计算](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/sheet7-7.png)

# 7-8 变位齿轮传动的设计

## 一、变位齿轮的功用

1. 提高齿轮的承载能力
2. 配凑中心距
3. 避免根切
4. 修复已磨损的旧齿轮

# 7-9 斜齿圆柱齿轮传动

## 一、斜齿圆柱齿轮齿廓曲面的形成

![斜齿轮形成](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-36.png)

$$
\tan\beta_b=\frac{\pi d_b}{L}
$$

$$
\tan\beta=\frac{\pi d}{L}
$$

$$
\frac{\tan\beta_b}{\tan\beta}=\frac{d_b}{d}
$$

## 二、斜齿轮的基本参数

![斜齿轮参数](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-37.png)

### 1.法面模数$m_n$与端面模数$m_t$

$$
m_n=m_t\cos\beta
$$

### 2.齿顶高系数

$$
c_t^*=c_n^*\cos\beta
$$

### 3.压力角

$$
\tan\alpha_n=\tan\alpha_t\cos\beta
$$

### 4.变位系数

$$
x_n=x_t\cos\beta
$$

### 5.分度圆柱螺旋角$\beta$与基圆柱螺旋角$\beta_b$

## 三、斜齿轮传动的几何尺寸计算

斜齿轮的几何尺寸计算应在**端面**内进行

## 四、斜齿轮的正确啮合条件

1. 模数相等
2. 压力角相等
3. 螺旋角大小相等，外啮合时旋向相反，内啮合时旋向相同

## 五、斜齿轮传动的总重合度

![斜齿轮重合度](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-38.png)

从端面看，斜齿轮的啮合与直齿轮完全一样，端面重合度

$$
\varepsilon_{\alpha}
=
\frac{1}{2\pi}
\left[
z_1\left(\tan \alpha_{at1}-\tan \alpha_t'\right)
+
z_2\left(\tan \alpha_{at2}-\tan \alpha_t'\right)
\right]
$$

轴面重合度

$$
\varepsilon_{\beta}
=
\frac{\Delta L}{p_{bt}}
=
\frac{B \tan \beta_b}{p_{bt}}
$$

化简得

$$
\varepsilon_{\beta}
=
\frac{B \sin \beta}{\pi m_n}
$$

斜齿轮传动的总重合度

$$
\varepsilon_{\gamma}
=
\varepsilon_{\alpha}
+
\varepsilon_{\beta}
$$

通常为了保证重合度$\varepsilon_{\gamma}\geq2$

$$
B \geq \frac{0.9\pi m_n}{\sin \beta}
$$

## 六、斜齿轮的法面齿形及当量齿数

![斜齿轮法面齿形](assets/img/posts/notes/theory_of_machines_and_machanism/chapter7/7-39.png)

斜齿轮的法面齿形比较复杂，通常采用近似计算

$$
b = r, \qquad a = \frac{r}{\cos \beta}
$$

C处的曲率半径为

$$
\rho = \frac{a^2}{b}
= \frac{r}{\cos^2 \beta}
$$

以$\rho$为分度圆半径，以参数$m_n、\alpha_n$确定一个假想的直齿轮，称为斜齿轮的**当量齿轮**，当量齿轮的齿数称为**当量齿数**

$$
z_v
=
\frac{2\rho}{m_n}
=
\frac{2r}{m_n \cos^2 \beta}
=
\frac{m_t z}{m_n \cos^2 \beta}
=
\frac{z}{\cos^3 \beta}
$$

## 七、斜齿轮传动特点

1. 啮合性能好，承载能力大
2. 结构尺寸紧凑
3. 有轴向力

# 7-10 交错轴斜齿轮传动（自学）

# 7-11 蜗杆蜗轮传动

**蜗杆蜗轮的旋向？**

蜗杆像螺纹，左低右高为右旋；

蜗轮配蜗杆，旋向必须同。

# 7-12 锥齿轮传动

锥齿轮参数在大端上
