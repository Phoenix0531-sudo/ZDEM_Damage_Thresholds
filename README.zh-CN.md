# ZDEM Damage Thresholds

**ZDEM 微观监测的单轴损伤演化与破裂阈值分析**

[English](README.md) | [中文](README.zh-CN.md)

![CI](https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

面向 **ZDEM 单轴压缩** 微观监测数据的批处理分析：读取 `_id_1.dat`…`_id_5.dat` 类序列，合成体积应变，提取弹性参数与渐进破裂阈值（CC / CI / CD / UCS 风格），经 `plot2D/` 输出学术向应变–能量图。

## 为什么做这个

岩石力学写作需要可复现的阈值拾取与多联图。本仓库把流水线固化，替代一次性 notebook。

## 功能

- 按目录批量读微观监测文件  
- 弹性参数与损伤阈值提取  
- 出版向 2D 出图  
- 入口：`ZDEM_main_plot_damage_and_thresholds_from_dir.py`  

## 安装

```bash
git clone https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds.git
cd ZDEM_Damage_Thresholds
pip install -r requirements.txt
```

## 使用

1. 将监测文件放入实验目录  
2. 编辑入口脚本顶部全局配置（路径、出图选项）  
3. 运行：

```bash
python ZDEM_main_plot_damage_and_thresholds_from_dir.py
```

## 目录结构

```
ZDEM_main_plot_damage_and_thresholds_from_dir.py
plot2D/
tests/
```

## 相关 ZDEM 工具

| 仓库 | 作用 |
|------|------|
| [ZDEM_ParticleTracker](https://github.com/Phoenix0531-sudo/ZDEM_ParticleTracker) | 交互式颗粒追踪 + VisPy 真实半径渲染 |
| [ZDEM_Salt_Kinematics](https://github.com/Phoenix0531-sudo/ZDEM_Salt_Kinematics) | 盐体几何/运动学提取与出图 |
| [ZDEM_Area_Conservation](https://github.com/Phoenix0531-sudo/ZDEM_Area_Conservation) | 面积守恒 / 三角网格分析 |
| [ZDEM_Bond_Fracture](https://github.com/Phoenix0531-sudo/ZDEM_Bond_Fracture) | 粘结损伤序列 + 桌面/CLI |
| [ZDEM_Damage_Thresholds](https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds) | 损伤阈值与应变–能量图 |
| [ZDEM_DFN](https://github.com/Phoenix0531-sudo/ZDEM_DFN) | ZDEM 离散裂隙网络生成 |
| [ZDEM_Model_Editor](https://github.com/Phoenix0531-sudo/ZDEM_Model_Editor) | 模型文件可视化编辑 |
| [ZDEM_Archiver](https://github.com/Phoenix0531-sudo/ZDEM_Archiver) | 大体量模拟结果归档清理 |
| [ZDEM3D_WEB](https://github.com/Phoenix0531-sudo/ZDEM3D_WEB) | CAE 云端界面（Django + React + VTK.js） |
## 许可证

MIT。可在署名前提下商用。见 [LICENSE](LICENSE)。
