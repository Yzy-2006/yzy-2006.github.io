---
title: STM32第0章 环境配置
description: STM32第0章笔记：Ubuntu 下的开发环境配置、编译、烧录与调试
author: 阎梓瑜
date: 2026-10-12 16:00:00 +0800
categories: [STM32]
tags: [STM32]
pin: false
math: true
mermaid: true
---

## 一、开发环境架构

```text
Ubuntu
├── STM32CubeMX                  配置 STM32 外设，生成 HAL + CMake 工程
├── Visual Studio Code           代码编辑、构建任务、断点调试
│   ├── C/C++                    代码补全与导航
│   ├── CMake Tools              CMake 集成
│   ├── Cortex-Debug             GDB 嵌入式调试
│   └── STM32CubeIDE for VS Code  可选的 ST 官方集成插件
├── CMake + Ninja                构建系统
├── arm-none-eabi-gcc            ARM 裸机交叉编译器
├── gdb-multiarch                GDB 调试器
└── SEGGER J-Link Software       SWD 连接、烧录与 GDB Server
        ↓
      J-Link V9
        ↓  SWD
     STM32F103C8T6
```

与课程中的 Keil 环境大致对应：

| 课程里的工具或操作 | Ubuntu 下的替代方式 |
| --- | --- |
| STM32CubeMX 配置 GPIO、UART、定时器等 | STM32CubeMX，基本一致 |
| Keil MDK-ARM 工程 | CubeMX 生成的 CMake 工程 |
| Keil 编辑和编译 | VS Code + CMake + ARM GCC |
| Keil Download | J-Link Commander（或 VS Code 烧录任务） |
| Keil Debug | Cortex-Debug + J-Link GDB Server |
| HAL 库函数 | 基本不变，仍使用相同 STM32F1 HAL API |

**注意**：以下配置中的目标芯片是 `STM32F103C8`。如果以后换芯片，需要相应修改芯片型号、引脚配置和调试参数。

## 二、检查 Ubuntu 与安装基本工具

检查系统：

```bash
lsb_release -a
uname -m
```

更新软件源并安装基础工具：

```bash
sudo apt update
sudo apt install -y \
    build-essential \
    cmake \
    ninja-build \
    git \
    gdb-multiarch \
    wget curl unzip \
    libusb-1.0-0
```

安装 STM32 交叉编译器：

```bash
sudo apt install -y gcc-arm-none-eabi
```

检查工具：

```bash
cmake --version
ninja --version
arm-none-eabi-gcc --version
arm-none-eabi-g++ --version
arm-none-eabi-objcopy --version
gdb-multiarch --version
```

本次实测 `arm-none-eabi-gcc` 为 **13.2.1**。`gcc` 与 `arm-none-eabi-gcc` 不同，后者是编译 STM32 Cortex-M 程序使用的交叉编译器。

## 三、安装 VS Code 与插件

从 [VS Code Linux 官方页面](https://code.visualstudio.com/docs/setup/linux) 下载适用于 Ubuntu 的 `.deb` 包，安装示例：

```bash
cd ~/下载
sudo apt install ./code_*.deb
code --version
```

> 如果下载目录是 `~/Downloads`，请调整路径。已经安装 VS Code 则无需重复安装。

VS Code 安装推荐扩展：

```bash
code --install-extension ms-vscode.cpptools
code --install-extension ms-vscode.cmake-tools
code --install-extension marus25.cortex-debug
```

还可以安装 ST 官方的 **STM32CubeIDE for Visual Studio Code** 扩展；本记录中的一键烧录和调试使用 **VS Code Tasks + Cortex-Debug** 实现，不依赖官方插件。

## 四、安装 STM32CubeMX 与 STM32F1 HAL 固件包

1. 从 [STM32CubeMX 官网](https://www.st.com/en/development-tools/stm32cubemx.html) 下载 **Linux 版 STM32CubeMX**，不是 STM32CubeMX2。
2. 解压下载的 ZIP；给 Linux 安装程序添加可执行权限，运行安装程序（实际文件名以下载包为准）。
3. 启动 CubeMX，使用 `ACCESS TO MCU SELECTOR` 进入芯片选择界面。
4. 搜索并选择 `STM32F103C8T6`。
5. 第一次生成工程时，如果提示下载 `STM32Cube FW_F1`，选择 **Yes**，安装 STM32F1 HAL/CMSIS 固件包。本次弹窗提示版本为 `V1.8.7`。

安装程序的命令示例（先根据实际压缩包名调整）：

```bash
cd ~/下载
unzip en.stm32cubemx-lin-*.zip
chmod +x SetupSTM32CubeMX-*.linux
./SetupSTM32CubeMX-*.linux
```

### 1. 创建第一个 LED_Blink 工程

在 CubeMX 中进行如下配置：

| 配置位置 | 配置内容 |
| --- | --- |
| MCU Selector | `STM32F103C8T6` |
| System Core → SYS → Debug | `Serial Wire`，保留 PA13/PA14 的 SWD 功能 |
| Pinout → PC13 | `GPIO_Output` |
| GPIO output level | `High`（常见 Blue Pill 板载 LED 为低电平点亮） |
| GPIO mode | 可以使用适合板载 LED 电路的 `Output Open Drain` 或 `Push-Pull` |
| Clock Configuration | 第一次实验可先用默认 HSI 配置 |
| Project Manager → Project Name | `LED_Blink` |
| Project Manager → Toolchain / IDE | `CMake`，使用 GCC 工具链 |

然后点击 **GENERATE CODE**。本次工程路径：

```text
~/projects/STM32/LED_Blink/
├── Core/
│   ├── Inc/
│   └── Src/main.c
├── Drivers/
│   ├── CMSIS/
│   └── STM32F1xx_HAL_Driver/
├── cmake/
├── CMakeLists.txt
└── LED_Blink.ioc
```

> CubeMX 重新生成代码可能覆盖不在 `USER CODE` 区域内的修改，用户逻辑尽量写在 `USER CODE BEGIN ... END` 标记范围内。

### 2. 编写 HAL LED 闪烁代码

在 `Core/Src/main.c` 的 `while (1)` 循环中，保留 CubeMX 自动生成的 USER CODE 标记，并加入：

```c
/* USER CODE BEGIN WHILE */
while (1)
{
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
    HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);
    HAL_Delay(500);
}
/* USER CODE END 3 */
```

这里 `HAL_GPIO_TogglePin` 翻转 PC13，`HAL_Delay(500)` 延时约 500 ms；若板载 LED 确实连接到 PC13，应当每 0.5 秒翻转一次亮灭状态。

## 五、使用 CMake + Ninja 编译工程

进入工程根目录：

```bash
cd ~/projects/STM32/LED_Blink
```

首次配置 CMake：

```bash
cmake -S . -B build -G Ninja \
    -DCMAKE_BUILD_TYPE=Debug \
    -DCMAKE_TOOLCHAIN_FILE=cmake/gcc-arm-none-eabi.cmake
```

编译：

```bash
cmake --build build
```

本次实际编译输出：

```text
[19/19] Linking C executable LED_Blink.elf
Memory region         Used Size  Region Size  %age Used
             RAM:        1584 B        20 KB      7.73%
           FLASH:        4884 B        64 KB      7.45%
```

这证明项目**编译和链接成功**。生成的文件通常在：

```text
~/projects/STM32/LED_Blink/build/LED_Blink.elf
```

如果重新编译时显示：

```text
ninja: no work to do.
```

说明源文件没有变化，通常不是错误。

> 不同 CubeMX 版本生成的 CMake 工具链文件路径可能有差别；如果找不到 `cmake/gcc-arm-none-eabi.cmake`，应查看工程实际目录和 `CMakePresets.json`，不要机械照搬路径。

## 六、安装 SEGGER J-Link 并接线

### 1. 安装 J-Link 软件

在 [SEGGER J-Link 官方下载页](https://www.segger.com/downloads/jlink/) 下载 Linux x86_64 的 `.deb` 安装包。本次使用 `JLink_Linux_V980_x86_64.deb`：

```bash
cd ~/下载
sudo apt install ./JLink_Linux_V980_x86_64.deb
```

若出现提示：

```text
N: ... 无法被用户 '_apt' 访问，已脱离沙盒并提权为根用户来进行下载
```

但同时出现 `正在设置 jlink (9.80.0)` 和 `Updating udev rules ... OK`，通常表示**安装已完成**，末尾是本地文件读取权限提示。

检查程序：

```bash
command -v JLinkExe
command -v JLinkGDBServerCLExe
JLinkExe
```

### 2. 本次 J-Link V9 与 Blue Pill 接线

本次使用的 **FanX Tek J-Link V9** 下载器丝印与 Blue Pill 接口对应：

| J-Link V9 | STM32F103C8T6 | 作用 |
| --- | --- | --- |
| `DIO` | `SWIO`（PA13） | SWD 数据 |
| `CLK` | `SWCK`（PA14） | SWD 时钟 |
| `GD` | `GND` | 公共地 |
| `3V` | `3V3` | **仅在确认它是 3.3V 供电输出、且电流足够时使用** |
| `5V` | 不连接 | 避免误接 5V |

**安全提醒**：

- 最保守的首次测试方式是开发板通过自身 USB 单独供电，J-Link 先连接 DIO、CLK、GND；调试器若需要额外 VTref，则按该型号的说明连接正确的电压参考输入。
- 本次实测采用了 3.3V 四线供电接法，但**其他 J-Link 型号的 VTref 可能只是电压检测输入，并不能供电**；不要仅根据引脚名称类推。
- 使用调试器 3.3V 给板子供电前，需确认电压和最大供电电流；不要同时随意并联开发板 USB 供电与调试器 3.3V 输出。
- 接线操作应断电进行，确认正负极与信号线后再通电。

### 3. 验证 SWD 连接

在终端运行：

```bash
JLinkExe -device STM32F103C8 -if SWD -speed 1000
```

进入 `J-Link>` 后输入：

```text
connect
```

本次实际输出包括：

```text
Connecting to J-Link ...O.K.
VTref=3.295V
DAP initialized successfully.
Found SW-DP with ID 0x1BA01477
Found Cortex-M3 r1p1, Little endian.
Cortex-M3 identified.
```

其中 `VTref=3.295V` 证明检测到了合适的目标板电压；`Cortex-M3 identified.` 表示 **SWD 已成功连接目标内核**。

## 七、第一次手动烧录与运行

保持在 `J-Link>` 提示符，输入：

```text
loadfile /home/yanziyu/projects/STM32/LED_Blink/build/LED_Blink.elf
r
g
exit
```

含义：

| 命令 | 作用 |
| --- | --- |
| `loadfile` | 下载并校验 ELF 到 STM32 Flash |
| `r` | 复位目标芯片 |
| `g` | 继续运行 |
| `exit` | 退出 J-Link Commander |

实际烧录日志包含：

```text
Downloading file [.../build/LED_Blink.elf]...
J-Link: Flash download: Bank 0 @ 0x08000000: 1 range affected (5120 bytes)
J-Link: Flash download: Program & Verify speed: 31 KB/s
O.K.
```

烧录后观察到蓝色板载 LED 闪烁，说明目标程序运行正常。原来未烧录时蓝灯也可能闪烁，因为板上可能已有出厂测试程序；若要确认运行的是**新程序**，可以修改 `HAL_Delay(500)` 为 `HAL_Delay(100)`，重新编译并烧录，观察频率变化。

## 八、VS Code 一键编译与烧录

### 1. 手动创建 VS Code 任务

在工程根目录创建：

```text
.vscode/tasks.json
.vscode/launch.json
scripts/flash.jlink
```

`scripts/flash.jlink`：

```text
loadfile /home/yanziyu/projects/STM32/LED_Blink/build/LED_Blink.elf
r
g
exit
```

`.vscode/tasks.json`：

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "STM32: Build",
      "type": "shell",
      "command": "cmake",
      "args": ["--build", "${workspaceFolder}/build"],
      "options": { "cwd": "${workspaceFolder}" },
      "problemMatcher": []
    },
    {
      "label": "STM32: Build + Flash (J-Link)",
      "type": "shell",
      "command": "JLinkExe",
      "args": [
        "-device", "STM32F103C8",
        "-if", "SWD",
        "-speed", "1000",
        "-AutoConnect", "1",
        "-ExitOnError", "1",
        "-NoGui", "1",
        "-CommandFile", "${workspaceFolder}/scripts/flash.jlink"
      ],
      "dependsOn": ["STM32: Build"],
      "dependsOrder": "sequence",
      "group": { "kind": "build", "isDefault": true },
      "options": { "cwd": "${workspaceFolder}" },
      "problemMatcher": []
    }
  ]
}
```

在 VS Code 中按 **`Ctrl + Shift + B`**，就会按顺序执行：

```text
CMake Build → JLinkExe 读取 flash.jlink → 下载 ELF → 复位 → 运行 → 退出
```

本次成功日志包括：

```text
J-Link Command File read successfully.
J-Link>loadfile /home/yanziyu/projects/STM32/LED_Blink/build/LED_Blink.elf
Comparing flash [100%] Done.
J-Link: Flash download: Bank 0 @ 0x08000000: Skipped. Contents already match
O.K.
J-Link>r
J-Link>g
J-Link>exit
Script processing completed.
```

`Skipped. Contents already match` 表示芯片 Flash 与 ELF 一致，J-Link 无须重复写入，**不是烧录失败**。

## 九、VS Code F5 断点调试

确保安装了 **Cortex-Debug** 扩展，以及 `gdb-multiarch` 和 J-Link GDB Server。

在 `.vscode/launch.json` 中写入：

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "STM32F103 Debug (J-Link)",
      "type": "cortex-debug",
      "request": "launch",
      "cwd": "${workspaceFolder}",
      "executable": "${workspaceFolder}/build/LED_Blink.elf",
      "servertype": "jlink",
      "device": "STM32F103C8",
      "interface": "swd",
      "serverpath": "/opt/SEGGER/JLink/JLinkGDBServerCLExe",
      "gdbPath": "/usr/bin/gdb-multiarch",
      "toolchainPrefix": "arm-none-eabi",
      "serverArgs": ["-speed", "1000"],
      "runToEntryPoint": "main",
      "preLaunchTask": "STM32: Build"
    }
  ]
}
```

> `serverpath` 和 `gdbPath` 要以你电脑实际安装位置为准。如果路径不同，先使用 `command -v` 查找。启动 F5 前，确保之前的 `JLinkExe` 已经退出，避免 USB 调试器被占用。

在 `Core/Src/main.c` 的 GPIO 翻转语句旁点击行号左侧添加断点，然后按 **F5**。常用快捷键：

| 快捷键 | 作用 |
| --- | --- |
| `F5` | 启动 / 继续调试 |
| `F10` | 单步跳过（Step Over） |
| `F11` | 单步进入（Step Into） |
| `Shift + F11` | 单步跳出 |
| `Shift + F5` | 结束调试 |

本次启动调试时看到：

```text
0x0800034e in HAL_GetTick () at stm32f1xx_hal.c:307
Program stopped, probably due to a reset and/or halt issued by debugger
Resetting target
Temporary breakpoint 2, main () at Core/Src/main.c:74
74    HAL_Init();
```

这是**正常启动流程**：调试器复位并暂停目标，随后根据 `runToEntryPoint: "main"` 设置临时断点，最终停在 `main()` 开头。继续按 F5 即可运行到手动设置的断点。

## 十、将重复配置封装为通用模板

一次性安装的工具（CubeMX、ARM GCC、CMake、VS Code、J-Link）**后续无须重复安装**。每个新工程仍要在 CubeMX 中配置芯片和外设，但 `.vscode` / 脚本可复用。

之前已整理好 `STM32_VSCode_Template.zip`，文件结构：

```text
STM32_VSCode_Template/
├── .vscode/
│   ├── tasks.json
│   └── launch.json
├── scripts/
│   ├── build.sh
│   └── flash.sh
├── install.sh
└── README.md
```

建议将 ZIP 解压到：

```text
~/projects/STM32/STM32_VSCode_Template/
```

### 1. 新建 UART_Test 等项目时

1. 使用 CubeMX 创建 `UART_Test` 工程，选择 CMake + GCC，生成代码。
2. 执行安装模板脚本：

   ```bash
   bash ~/projects/STM32/STM32_VSCode_Template/install.sh \
       ~/projects/STM32/UART_Test
   ```

3. 打开新项目：

   ```bash
   code ~/projects/STM32/UART_Test
   ```

4. `Ctrl + Shift + B`：首次自动配置 CMake、编译并烧录。
5. `F5`：自动编译并开始断点调试。

模板的 `build.sh` 会寻找工程生成的 ELF，并在 `build/` 下复制为统一的 **`firmware.elf`**；`flash.sh` 与 `launch.json` 固定引用该文件，因此不用每次把 `LED_Blink.elf` 改成 `UART_Test.elf`。

**模板适用边界**：设计用于 STM32F103C8、J-Link、单个 ELF 目标的 CubeMX/CMake 入门工程；更换芯片时需修改 `device` 参数，并复查引脚、供电及调试设置。`install.sh` 不会覆盖已有同名配置文件。由于最初 `LED_Blink` 的手工配置已经验证通过，而通用模板在新项目上的运行尚未单独实测，建议首次应用模板时进行一次完整编译和烧录验证。

## 十一、常见问题与处理

| 现象 | 原因与处理 |
| --- | --- |
| CubeMX 报 `mcusAds.json` 下载失败 | MCU 信息下载异常，可能是网络/服务器/代理问题；先尝试进入 MCU Selector，必要时检查 `Help → Updater Settings`。 |
| CubeMX 提示缺少 `STM32Cube FW_F1` | 点击 `Yes` 安装对应 HAL 固件包，或在 `INSTALL / REMOVE` 中下载。 |
| 安装 J-Link 时提示 `_apt` 权限不足 | 仅在安装流程正常完成的情况下可视为本地文件读取的非致命提示。 |
| `No probes connected via USB` | J-Link 软件可运行，但硬件尚未连接/识别；检查 USB、权限、设备。 |
| `VTref=3.295V` | 说明 J-Link 检测到约 3.3V 目标电压；尚需 `connect` 确认 SWD 内核连接。 |
| `Cortex-M3 identified.` | SWD 成功识别 Cortex-M3 内核。 |
| `ninja: no work to do.` | 没有需要重新编译的文件，正常。 |
| `Flash ... Skipped. Contents already match` | Flash 与 ELF 一致，无需重新烧录，正常。 |
| 批处理只出现 `Script processing completed`，但没有 `loadfile` | 检查 `scripts/flash.jlink` 是否实际包含命令并已经保存，可用 `cat -n scripts/flash.jlink` 查看。 |
| 调试停在 `HAL_GetTick()`，之后停在 `main()` | 复位及 `runToEntryPoint` 临时断点行为，正常。 |
| `JLinkGDBServerCLExe not found` | 检查 `launch.json` 中 `serverpath`。 |
| `gdb-multiarch` 不存在 | `sudo apt install gdb-multiarch`。 |
| J-Link 被占用、连接失败 | 结束其它 JLinkExe、GDB Server 或调试会话，再尝试连接。 |

## 十二、最终使用速查

### 1. 首次在新电脑安装（一次性）

```text
安装 Ubuntu 工具 → ARM GCC → VS Code → CubeMX → J-Link Software
                ↓
创建 CubeMX CMake 工程 → 编译 → SWD 连接 → 烧录 → F5 调试
```

### 2. 后续每个新实验

```text
CubeMX 创建/配置 .ioc → 生成 CMake 工程 → 安装通用模板
                    ↓
             VS Code 编写 HAL 代码
                    ↓
        Ctrl + Shift + B 编译并烧录
                    或
              F5 在线断点调试
```

### 3. 本次验证过的工程与命令

```bash
cd ~/projects/STM32/LED_Blink
cmake --build build
JLinkExe -device STM32F103C8 -if SWD -speed 1000
```

推荐在继续学习 GPIO 输入、UART、PWM、ADC、I2C、SPI 和 CAN 之前，保留 `LED_Blink` 工程不动，作为已验证的环境基准工程。

---

## 参考资料

- [STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html)
- [ARM GNU Toolchain](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads)
- [VS Code](https://code.visualstudio.com/)
- [SEGGER J-Link](https://www.segger.com/downloads/jlink/)
- [Cortex-Debug](https://github.com/Marus/cortex-debug)
