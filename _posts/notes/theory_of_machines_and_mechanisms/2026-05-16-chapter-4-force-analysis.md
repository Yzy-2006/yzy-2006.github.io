---
title: 机械原理 第4章 平面机构的力分析和机械效率
description: 机械原理第4章笔记
author: 阎梓瑜
date: 2026-05-16 09:00:00 +0800
categories: [笔记,机械原理]
tags: [机械原理]
pin: false
math: true
mermaid: true
---

## 4-1 力分析的基本知识

**驱动力（输入力）：**驱使机械运动的力，所作的功为输入功

**阻力：**阻碍机械运动的力，所作的功称为损耗功

## 4-3 运动副中的摩擦和计及摩擦时机构的力分析

### 一、移动副中的摩擦与自锁

#### 1.移动副中的摩擦

**平面移动副**

![平面移动副](assets/img/posts/notes/theory_of_machines_and_machanism/chapter4/planar_prismatic_pair.png)

$$
F_{f21} = fF_{N21} = fG
$$

$$
tan\varphi =\frac{F_{f21}}{F_{N21}}=f
$$


摩擦力$F_{f21}$的方向总与滑块相对导路的移动速度相反，总反力$F_{R21}$与滑块移动速度方向的夹角为$(90^\circ+\varphi)$ 

**槽面移动副**

![槽面移动副](assets/img/posts/notes/theory_of_machines_and_machanism/chapter4/grooved_sliding_pair.png)

$$
G = F_{N21}\sin\theta
$$

$$
F_{N21} = \frac{G}{\sin\theta}
$$

式中的 $\theta$ 为**槽型半角**

$$
F_{f21} = fF_{N21} = \frac{fG}{\sin\theta}
$$

若令当量摩擦系数$f_v = \frac{f}{\sin\theta}$,则有

$$
F_{f21} = f_v G
$$

>由于$f_v>f$,所以使用V带传动可以增大摩擦力
{: .prompt-info }

**斜面移动副**

![斜面移动副](assets/img/posts/notes/theory_of_machines_and_machanism/chapter4/inclined_sliding_pair.png)

***1）滑块沿斜面等速上升***

总反力$F_{R21}$为

$$
F_{R21}=\frac{G}{\cos(\lambda+\varphi)}
$$

法向反力$F_{N21}$为

$$
F_{N21}=F_{R21} \cos\varphi = \frac{\cos\varphi}{\cos(\lambda+\varphi)} f G
$$


当量摩擦系数$f_v$为

$$
f_v = \frac{\cos\varphi}{\cos(\lambda+\varphi)} f
$$

***2）滑块沿斜面等速下降***

总反力$F_{R21}$为

$$
F_{R21}=\frac{G}{\cos(\lambda-\varphi)}
$$

法向反力$F_{N21}$为

$$
F_{N21}=F_{R21} \cos\varphi = \frac{\cos\varphi}{\cos(\lambda-\varphi)} f G
$$


当量摩擦系数$f_v$为

$$
f_v = \frac{\cos\varphi}{\cos(\lambda-\varphi)} f
$$

>滑块下滑时，$F$可能是驱动力也可能是阻力，$\lambda>\varphi$时，$F$为阻力，$\lambda<\varphi$时，$F$为驱动力
{: .prompt-info }

>这个可以依据矢量三角形来记忆，$\lambda-\varphi$为正值的时候在竖直方向左边
{: .prompt-tip }

**螺旋副**

***1）矩形螺旋副***

![矩形螺旋副](assets/img/posts/notes/theory_of_machines_and_machanism/chapter4/rectangular_screw_pair.png)

$$
\tan\lambda = \frac{P_h}{\pi d} = \frac{nP}{\pi d}
$$

式中$d$为螺纹中径，$P_h$为螺纹导程，$z$为螺纹线数，$p$是螺距

拧紧螺母时，相当于滑块沿斜面上升

$$
f_v = \frac{\cos\varphi}{\cos(\lambda+\varphi)} f
$$

$$
M = F\frac{d}{2}
  = \frac{d}{2}G\tan(\lambda+\varphi)
$$

放松螺母时，相当于滑块沿斜面下降


$$
f'_v = \frac{\cos\varphi}{\cos(\lambda-\varphi)} f
$$

$$
M' = F\frac{d}{2}
  = \frac{d}{2}G\tan(\lambda-\varphi)
$$

>当$\lambda>\varphi$时,$M'$为阻止螺母加速松脱的阻力矩，当$\lambda<\varphi$时,$M'$为使螺母等速松脱的驱动力矩。
{: .prompt-info }

***2）三角螺纹螺旋副***

![三角螺纹螺旋副](assets/img/posts/notes/theory_of_machines_and_machanism/chapter4/V-thread_screw_pair.png)

可简化为槽面摩擦和斜面摩擦的组合

$$
\theta = 90^\circ - \beta
$$

$$
f'_v = \frac{1}{\sin\theta}f
     = \frac{1}{\sin(90^\circ-\beta)}f
     = \frac{1}{\cos\beta}f
$$

$$
\varphi'_v = \arctan f'_v
           = \arctan\left(\frac{1}{\cos\beta}f\right)
$$

拧紧螺母时

$$
f_v = \frac{\cos\varphi'_v}{\cos(\lambda+\varphi'_v)} f
$$

$$
M = F\frac{d}{2}
  = \frac{d}{2}G\tan(\lambda+\varphi'_v)
\tag{4-28}
$$

放松螺母时

$$
f'_v = \frac{\cos\varphi'_v}{\cos(\lambda-\varphi'_v)} f
$$

$$
M' = F'\frac{d}{2}
   = \frac{d}{2}G\tan(\lambda-\varphi'_v)
$$

>当$\lambda>\varphi'_v$时,$M'$为阻止螺母加速松脱的阻力矩，当$\lambda<\varphi'_v$时,$M'$为使螺母等速松脱的驱动力矩。
{: .prompt-info }

>三角形螺纹摩擦力矩较大，用于紧固连接；矩形螺纹摩擦力矩较小，传动效率高
{: .prompt-info }

#### 2.移动副的自锁

![移动副自锁](assets/img/posts/notes/theory_of_machines_and_machanism/chapter4/planar_prismatic_pair.png)

$$
移动副的自锁条件为\beta<\varphi
$$

### 二、转动副的摩擦与自锁

#### 1.径向轴颈与轴承的摩擦

![径向轴颈](assets/img/posts/notes/theory_of_machines_and_machanism/chapter4/radial_journal.png)

***1）未经过跑合***

$$
F_{f21} = \frac{\pi}{2} fG
$$

***2）跑合后***

**假设**
1. 轴承的径向磨损按余弦规律变化
2. 轴承的径向磨损与压强成正比

$$
F_{f21} = \frac{4}{\pi} fG
$$

***3）存在少许间隙的径向轴颈与轴承***

$$
F_{f21} = fF_{N21} = \frac{f}{\sqrt{1+f^2}}G
$$

>以上三种情况都是基于一定的假设，实际应用中在$f~\frac{\pi}{2} f$中间选取，计算机械效率时取大值，考虑机械自锁时取小值
{: .prompt-info }

#### 2.径向轴颈与轴承的自锁

![轴向自锁](assets/img/posts/notes/theory_of_machines_and_machanism/chapter4/self_lock.png)

无论径向轴颈和轴承之间是面接触还是线接触，最终都可以看成驱动力矩$M$、径向载荷$G$，法向反力$F_{N21}$和摩擦力$F_{f21}$作用下的平衡问题

$F_{R21}$与$G$应形成一个与驱动力矩相平衡的力偶，设两者间的距离为$\rho$

$$
M=F_{R21} \rho = G \rho
$$

由于法向反力对转动中心没有力矩，所以总反力的力矩即为摩擦力矩

$$
M=M_f=f_v G \rho
$$

联立解得

$$
\rho =f_v r
$$

对于一个具体的径向轴颈，受力平衡时总反力总是切于摩擦圆，方向阻止相对运动

>这里应该保证径向载荷是过圆心的
{: .prompt-warning }

设驱动力$G$,作用线距轴心的偏距为$e$

1. $e=\rho$时，轴颈匀速转动
2. $e>\rho$时，轴颈加速转动
3. $e<\rho$时，轴颈自锁

>驱动力偏距的来源实际上是把轴向载荷和驱动力矩合成变为了一个新的力，所以与前边推导过程的假设并不冲突
{: .prompt-tip }

### 三、计及摩擦时平面连杆机构的力分析

1. 计算出摩擦角和摩擦圆半径，并画出摩擦圆
2. 从二力构件着手分析
3. 对有已知力作用的构件作力分析
4. 对未知力所在构件进行力分析

## 4-4 机械的效率和自锁

### 一、机械效率

$$
P_d = P_r + P_f
$$

$$
\eta = \frac{P_r}{P_d}
$$

$$
\eta = 1 - \frac{P_f}{P_d} = 1 - \xi
$$

其中$\xi$称为机械损失系数

$$
\eta
=
\frac{\text{理想驱动力}}{\text{实际驱动力}}
=
\frac{\text{理想驱动力矩}}{\text{实际驱动力矩}}
$$

$$
\eta
=
\frac{\text{实际工作阻力}}{\text{理想工作阻力}}
=
\frac{\text{实际工作阻力矩}}{\text{理想工作阻力矩}}
$$

### 二、机械自锁

机械发生自锁的条件:

$$
\eta \leq 0
$$
