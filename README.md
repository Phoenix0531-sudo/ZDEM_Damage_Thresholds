# ZDEM Damage Thresholds

**Rock damage evolution and crack-threshold style analysis for ZDEM energy curves.**

[English](README.md) | [中文](README.zh-CN.md)

[![CI](https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds/actions/workflows/ci.yml/badge.svg)](https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Focus on **threshold-centric** views: damage index vs normalized energy / strain-energy style plots under `plot2D/`. Complements Bond Fracture (series/spatial damage) with curve-based criteria used in lab reports.

## Preview

![ZDEM Damage Thresholds](docs/screenshots/preview.png)

## Layout

```
plot2D/     # threshold and energy figure scripts
tests/ docs/
```

## Install / run

```bash
git clone https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds.git
cd ZDEM_Damage_Thresholds
pip install -r requirements.txt
# run plot/analysis entries under plot2D/ as documented in scripts
pytest tests/
```

## License

MIT. See [LICENSE](LICENSE).
