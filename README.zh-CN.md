# ZDEM Damage Thresholds

**岩石损伤演化与裂纹阈值分析（ZDEM）**

[English](README.md) | [中文](README.zh-CN.md)

![CI](https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

岩石损伤演化与裂纹阈值分析（ZDEM）。

> 作者：[Phoenix0531-sudo](https://github.com/Phoenix0531-sudo) · 欢迎学习、二次开发与**商业使用**，请保留本仓库署名与许可证声明。

## 技术栈

Python

## 功能特性

- 损伤演化曲线
- 裂纹阈值识别
- 目录批处理绘图

## 快速开始

```bash
git clone https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds.git
cd ZDEM_Damage_Thresholds
```

```bash
pip install -r requirements.txt
python ZDEM_main_plot_damage_and_thresholds_from_dir.py
```

更完整的英文说明见 [README.md](README.md)。

## 仓库结构（摘要）

```
ZDEM_Damage_Thresholds/
├─ .github/
├─ docs/
├─ plot2D/
├─ CHANGELOG.md
├─ Dockerfile
├─ LICENSE
├─ README.md
├─ README.zh-CN.md
├─ requirements.txt
├─ setup.py
├─ ZDEM_main_plot_damage_and_thresholds_from_dir.py
```

## 测试

```bash
pip install pytest
pytest -q
```

仓库内 `tests/` 至少包含 smoke 测试；有完整测试套件时以 CI 为准。

## CI

GitHub Actions（`push` / `pull_request`）会：

- 安装依赖（requirements / pyproject）
- 运行 `pytest`（**硬失败**）
- 尽力做语法/结构检查

## 许可证

[MIT](LICENSE) — 可自由使用、修改、分发与**商用**，需保留版权与许可声明（提及本仓库 / 作者即可）。

## 关于

维护者：[Phoenix0531-sudo](https://github.com/Phoenix0531-sudo)
