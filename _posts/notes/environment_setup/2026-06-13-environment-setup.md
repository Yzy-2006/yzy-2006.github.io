---
title: 环境配置小妙招
description: 环境配置小妙招
author: 阎梓瑜
date: 2026-06-13 16:00:00 +0800
categories: [笔记,环境配置]
tags: [环境配置,CMake]
pin: false
math: true
mermaid: true
---

## 1.使用源码编译安装第三方库

### 1.1 安装位置

**个人长期使用的库**通常安装在`$HOME/.local`，也可以**按库按版本隔离安装**，安装在`$HOME/local/<library>/<version>

### 1.2 如何指定安装位置

**1.使用源码外构建**

```bash
cmake -S library-source -B library-build \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=$HOME/local/mylib/1.0.0
```

其中`library-source`为源码目录，`library-build`为构建目录

**2.编译**

```bash
cmake --build library-build -j
```

**3.安装**

```bash
cmake --install library-build
```

### 1.3 后续的CMake如何找到这个库

配置当前工程时添加

```bash
cmake -S . -B build \
    -DCMAKE_PREFIX_PATH="$HOME/local/eigen/3.4.0;$HOME/local/opencv/4.12.0;$HOME/local/vtk/9.4.2"
```

然后在 `CMakeLists.txt `中

```cmake
find_package(MyLib REQUIRED)

target_link_libraries(my_program
    PRIVATE
        MyLib::MyLib
)
```

如果使用`find_package`找不到库

```
cmake -S . -B build \
    -DMyLib_DIR="$HOME/local/mylib/1.0.0/lib/cmake/MyLib"
```