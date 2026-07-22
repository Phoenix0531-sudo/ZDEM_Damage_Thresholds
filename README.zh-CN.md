# ZDEM Damage Thresholds

**岩石损伤演化与裂纹阈值分析（ZDEM）。**

[English](README.md) | [中文](README.zh-CN.md)

[![CI](https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds/actions/workflows/ci.yml/badge.svg)](https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

岩石损伤演化与裂纹阈值分析（ZDEM）。

应变能向图件与阈值。


## 功能

- 🪨 损伤演化分析
- 📉 阈值 / 能量图（`plot2D/`）
- ✅ CI + 测试

## 快速开始

### 安装

```bash
git clone https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds.git
cd ZDEM_Damage_Thresholds
pip install -r requirements.txt
```

### 使用

```bash
# 按文档运行 plot2D/ 下分析入口
pytest tests/
```

## 项目结构

```
plot2D/
tests/  docs/
```

## 相关 ZDEM 工具

| 仓库 | 作用 |
|------|------|
| [ZDEM_ParticleTracker](https://github.com/Phoenix0531-sudo/ZDEM_ParticleTracker) | 交互颗粒追踪 + VisPy 真实半径渲染 |
| [ZDEM_Salt_Kinematics](https://github.com/Phoenix0531-sudo/ZDEM_Salt_Kinematics) | 盐构造几何 / 运动学提取与出图 |
| [ZDEM_Area_Conservation](https://github.com/Phoenix0531-sudo/ZDEM_Area_Conservation) | 面积守恒 / 三角剖分分析 |
| [ZDEM_Bond_Fracture](https://github.com/Phoenix0531-sudo/ZDEM_Bond_Fracture) | 粘结损伤序列 + 桌面 / CLI |
| [ZDEM_Damage_Thresholds](https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds) | 损伤阈值与应变能图 |
| [ZDEM_DFN](https://github.com/Phoenix0531-sudo/ZDEM_DFN) | ZDEM 离散裂隙网络生成 |
| [ZDEM_Model_Editor](https://github.com/Phoenix0531-sudo/ZDEM_Model_Editor) | 模型文件可视化编辑 |
| [ZDEM_Archiver](https://github.com/Phoenix0531-sudo/ZDEM_Archiver) | 大体积模拟结果归档 / 清理 |
| [ZDEM3D_WEB](https://github.com/Phoenix0531-sudo/ZDEM3D_WEB) | CAE 云端界面（Django + React + VTK.js） |

## 说明

与 Bond Fracture 互补，更侧重阈值视角。

## 许可证

MIT。在注明出处的前提下可商业使用（以 LICENSE 为准）。详见 [LICENSE](LICENSE)。
