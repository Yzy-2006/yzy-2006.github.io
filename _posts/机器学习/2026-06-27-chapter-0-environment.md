---
title: 机器学习 第0章 配置环境
description: 机器学习第0章笔记
author: 阎梓瑜
date: 2026-06-27 16:30:00 +0800
categories: [机器学习, 开发环境]
tags: [机器学习]
pin: false
math: true
mermaid: true
---


## 进入项目目录

```bash
cd /home/yanziyu/Hands-on-ML
```

该命令用于切换到 `Hands-on-ML` 项目目录。

后续创建环境、启动 Jupyter、运行代码时，终端的当前工作目录就是该项目目录。

---

## 创建 Conda 环境

```bash
conda create -n machine_learning -c conda-forge python=3.11 pip \
  jupyterlab notebook ipykernel \
  numpy pandas matplotlib scipy scikit-learn scikit-image \
  tqdm xgboost pydotplus six graphviz -y
```

该命令用于创建一个名为 `machine_learning` 的 Conda 环境，并安装机器学习常用依赖。

其中：

```bash
conda create
```

表示创建新的 Conda 环境。

```bash
-n machine_learning
```

表示环境名称为 `machine_learning`。

```bash
-c conda-forge
```

表示从 `conda-forge` 频道安装软件包。

```bash
python=3.11
```

表示环境中使用 Python 3.11。

```bash
pip
```

表示安装 pip，方便后续安装 PyPI 上的软件包。

```bash
-y
```

表示自动确认安装过程，不再手动输入 `y`。

反斜杠 `\` 表示命令换行，方便阅读。多行命令本质上仍然是一条完整命令。

---

## 激活 Conda 环境

```bash
conda activate machine_learning
```

激活后，终端前面一般会显示：

```bash
(machine_learning) yanziyu@Legion:~/Hands-on-ML$
```

这说明当前终端正在使用 `machine_learning` 环境。

此时执行：

```bash
python
pip
jupyter lab
```

都会优先使用该环境中的版本。

退出环境可以使用：

```bash
conda deactivate
```

---

## 已安装的主要软件包

### Jupyter 相关

```bash
jupyterlab notebook ipykernel
```

作用分别是：

```text
jupyterlab：现代版 Jupyter 网页开发环境
notebook：传统版 Jupyter Notebook
ipykernel：让当前 Python 环境可以作为 Jupyter 内核运行
```

---

### 数据分析与科学计算

```bash
numpy pandas matplotlib scipy
```

作用分别是：

```text
numpy：数组、矩阵和数值计算
pandas：表格数据处理，例如 DataFrame、CSV 读取等
matplotlib：绘图和数据可视化
scipy：科学计算，例如优化、统计、信号处理等
```

---

### 机器学习相关

```bash
scikit-learn scikit-image xgboost
```

作用分别是：

```text
scikit-learn：经典机器学习库，包括回归、分类、聚类、降维、模型评估等
scikit-image：图像处理库
xgboost：梯度提升树模型库，常用于分类和回归任务
```

---

### 辅助工具

```bash
tqdm pydotplus six graphviz
```

作用分别是：

```text
tqdm：显示循环进度条
pydotplus：生成 Graphviz 图结构，常用于可视化决策树
six：兼容 Python 2 和 Python 3 的工具库
graphviz：图可视化工具，常用于决策树、流程图等可视化
```

---

## 检查 NVIDIA 显卡驱动

如果电脑有 NVIDIA 显卡，可以先检查驱动是否正常：

```bash
nvidia-smi
```

如果能正常显示显卡信息，说明 NVIDIA 驱动已经正常工作。

例如输出中出现：

```text
Driver Version: 595.71.05
CUDA Version: 13.2
NVIDIA GeForce RTX 5080
```

说明：

```text
系统已经识别到 NVIDIA 显卡
NVIDIA 驱动正在正常运行
当前驱动最高支持 CUDA 13.2
```

注意：

```text
nvidia-smi 中显示的 CUDA Version 表示驱动最高支持的 CUDA 版本，
不代表系统中一定安装了完整的 CUDA Toolkit。
```

安装 PyTorch 时，通常不需要手动安装完整 CUDA Toolkit，只要驱动版本足够新即可。

---

## 安装 PyTorch GPU 版本

如果之前安装过 CPU 版 PyTorch，可以先卸载：

```bash
pip uninstall torch torchvision torchaudio -y
```

然后安装 CUDA 版本，例如 CUDA 12.8 版本：

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

其中：

```bash
torch
```

是 PyTorch 核心库，用于张量计算、自动求导、神经网络搭建和模型训练。

```bash
torchvision
```

是 PyTorch 的计算机视觉扩展库，常用于图像数据集、图像预处理和视觉模型。

```bash
torchaudio
```

是 PyTorch 的音频处理扩展库，常用于音频读取、语音处理和声谱图生成。

```bash
--index-url https://download.pytorch.org/whl/cu128
```

表示从 PyTorch 官方 CUDA 12.8 版本软件源下载。

如果安装的是 CPU 版本，则命令通常是：

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

其中 `cpu` 表示只安装 CPU 版本，不使用 NVIDIA 显卡。

---

## 验证 PyTorch 是否可以调用显卡

安装完成后，可以运行：

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'No CUDA')"
```

如果输出类似：

```text
2.x.x+cu128
True
NVIDIA GeForce RTX 5080
```

说明 PyTorch 已经可以调用 NVIDIA 显卡。

如果输出中出现：

```text
False
```

说明当前 PyTorch 没有成功使用 CUDA。

常见原因包括：

```text
安装成了 CPU 版 PyTorch
NVIDIA 驱动没有正常安装
当前 Python 环境不是预期的 Conda 环境
```

可以进一步检查：

```bash
python -c "import torch; print(torch.__version__)"
```

如果版本号中含有：

```text
+cpu
```

说明当前安装的是 CPU 版 PyTorch，需要卸载后重新安装 CUDA 版。

---

## 注册 Jupyter Kernel

在 Conda 环境中执行：

```bash
conda activate machine_learning

python -m ipykernel install --user --name machine_learning --display-name "Python (machine_learning)"
```

该命令用于把当前 Conda 环境注册到 Jupyter 中。

其中：

```bash
python -m ipykernel
```

表示使用当前环境的 Python 运行 `ipykernel` 模块。

```bash
install
```

表示安装或注册一个 Jupyter kernel 配置。

```bash
--user
```

表示只为当前用户注册该 kernel，不需要管理员权限。

```bash
--name machine_learning
```

表示 Jupyter 内部使用的 kernel 名称。

```bash
--display-name "Python (machine_learning)"
```

表示在 JupyterLab、Jupyter Notebook 或 VS Code Notebook 中显示的名称。

注册完成后，可以在 Jupyter 中选择：

```text
Python (machine_learning)
```

作为 Notebook 的运行环境。

---

## 查看已经注册的 Jupyter Kernel

```bash
jupyter kernelspec list
```

如果看到类似：

```text
machine_learning    /home/yanziyu/.local/share/jupyter/kernels/machine_learning
```

说明注册成功。

如果以后想删除这个 kernel，可以使用：

```bash
jupyter kernelspec uninstall machine_learning
```

注意：该命令只会删除 Jupyter 中的 kernel 入口，不会删除 Conda 环境本身。

如果要删除 Conda 环境，需要使用：

```bash
conda remove -n machine_learning --all
```

---

## 启动 JupyterLab

在项目目录下执行：

```bash
cd /home/yanziyu/Hands-on-ML
conda activate machine_learning
jupyter lab
```

然后浏览器会打开 JupyterLab 页面。

在新建 Notebook 或打开已有 `.ipynb` 文件时，选择：

```text
Python (machine_learning)
```

作为运行内核。

---

## 在 VS Code 中配置 Conda 环境

首先打开项目目录：

```bash
cd /home/yanziyu/Hands-on-ML
code .
```

然后在 VS Code 中安装插件：

```text
Python
Jupyter
```

插件发布者一般为 Microsoft。

---

## 选择 Python 解释器

在 VS Code 中按：

```text
Ctrl + Shift + P
```

输入并选择：

```text
Python: Select Interpreter
```

然后选择类似：

```text
Python 3.11.x ('machine_learning': conda)
```

或者选择路径类似：

```text
/home/yanziyu/anaconda3/envs/machine_learning/bin/python
```

如果列表中找不到 `machine_learning`，可以先在终端中查看 Python 路径：

```bash
conda activate machine_learning
which python
```

然后将输出路径手动填入 VS Code 的解释器选择中。

---

## 在 VS Code 中选择 Notebook Kernel

打开 `.ipynb` 文件后，点击右上角的 Kernel 选择器。

选择：

```text
Python (machine_learning)
```

或者类似：

```text
machine_learning
```

这样 VS Code 中的 Notebook 就会使用 `machine_learning` 环境运行代码。

---

## 验证 VS Code 是否使用正确环境

在 VS Code 中新建 Python 文件或 Notebook，运行：

```python
import sys
print(sys.executable)
```

如果输出类似：

```text
/home/yanziyu/anaconda3/envs/machine_learning/bin/python
```

说明 VS Code 当前使用的是 `machine_learning` 环境。

如果安装了 CUDA 版 PyTorch，可以进一步验证：

```python
import torch

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
```

如果输出中包含：

```text
True
NVIDIA GeForce RTX 5080
```

说明 VS Code 中的 Python 环境也可以正常调用显卡。

---

## 推荐完整配置流程

```bash
cd /home/yanziyu/Hands-on-ML

conda create -n machine_learning -c conda-forge python=3.11 pip \
  jupyterlab notebook ipykernel \
  numpy pandas matplotlib scipy scikit-learn scikit-image \
  tqdm xgboost pydotplus six graphviz -y

conda activate machine_learning

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

python -m ipykernel install --user --name machine_learning --display-name "Python (machine_learning)"

jupyter lab
```

VS Code 中需要额外完成：

```text
安装 Python 和 Jupyter 插件
通过 Python: Select Interpreter 选择 machine_learning 环境
打开 .ipynb 文件后选择 Python (machine_learning) Kernel
```

---

## 常用检查命令

### 查看当前 Python 路径

```bash
which python
```

或在 Python 中：

```python
import sys
print(sys.executable)
```

---

### 查看当前 Conda 环境

```bash
conda info --envs
```

当前激活的环境前面会有 `*` 标记。

---

### 查看 PyTorch 是否支持 CUDA

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

---

### 查看显卡状态

```bash
nvidia-smi
```

---

### 查看 Jupyter Kernel

```bash
jupyter kernelspec list
```

---

## 总结

整个环境配置流程可以概括为：

```text
进入 Hands-on-ML 项目目录
创建 machine_learning Conda 环境
安装机器学习、数据分析、Jupyter 等常用库
根据 NVIDIA 显卡情况安装 CUDA 版 PyTorch
将 Conda 环境注册为 Jupyter Kernel
在 JupyterLab 或 VS Code 中选择该环境运行 Notebook
```

核心命令是：

```bash
conda activate machine_learning
python -m ipykernel install --user --name machine_learning --display-name "Python (machine_learning)"
```

核心检查方式是：

```python
import sys
print(sys.executable)
```

只要输出路径位于：

```text
/home/yanziyu/anaconda3/envs/machine_learning/
```

就说明当前 Python、Jupyter 或 VS Code 使用的是正确的 Conda 环境。
