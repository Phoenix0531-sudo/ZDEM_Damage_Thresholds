# ZDEM Damage Thresholds

**Uniaxial damage evolution & crack thresholds from ZDEM micro-monitoring**

[English](README.md) | [中文](README.zh-CN.md)

![CI](https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Batch-oriented analysis for **ZDEM uniaxial compression** micro-monitoring dumps: read `_id_1.dat` … `_id_5.dat` style series, synthesize volumetric strain, extract elastic parameters and progressive cracking thresholds (CC / CI / CD / UCS style markers), and render academic strain–energy figures via `plot2D/`.

## Why this exists

Rock-mechanics papers need reproducible threshold picks and multi-panel figures. This repo codifies the pipeline instead of one-off notebooks.

## Features

- Directory-driven batch over micro-monitoring files
- Elastic parameter + progressive damage threshold extraction
- Publication-oriented 2D plotting (`plot2D`)
- Entry script: `ZDEM_main_plot_damage_and_thresholds_from_dir.py`

## Install

```bash
git clone https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds.git
cd ZDEM_Damage_Thresholds
pip install -r requirements.txt
```

## Usage

1. Put ZDEM micro-monitoring files in an experiment directory.
2. Edit the global config block at the top of `ZDEM_main_plot_damage_and_thresholds_from_dir.py` (paths, plot options).
3. Run:

```bash
python ZDEM_main_plot_damage_and_thresholds_from_dir.py
```

## Project layout

```
ZDEM_main_plot_damage_and_thresholds_from_dir.py
plot2D/                 # file_io, zdem_core, zdem_plot
tests/
```

## Related ZDEM tools

| Repo | Role |
|------|------|
| [ZDEM_ParticleTracker](https://github.com/Phoenix0531-sudo/ZDEM_ParticleTracker) | Interactive particle tracking + VisPy true-radius render |
| [ZDEM_Salt_Kinematics](https://github.com/Phoenix0531-sudo/ZDEM_Salt_Kinematics) | Salt geometry / kinematics extraction & plots |
| [ZDEM_Area_Conservation](https://github.com/Phoenix0531-sudo/ZDEM_Area_Conservation) | Area-conservation / triangulation analysis |
| [ZDEM_Bond_Fracture](https://github.com/Phoenix0531-sudo/ZDEM_Bond_Fracture) | Bond damage series + desktop / CLI |
| [ZDEM_Damage_Thresholds](https://github.com/Phoenix0531-sudo/ZDEM_Damage_Thresholds) | Damage thresholds & strain–energy plots |
| [ZDEM_DFN](https://github.com/Phoenix0531-sudo/ZDEM_DFN) | Discrete fracture network generator for ZDEM |
| [ZDEM_Model_Editor](https://github.com/Phoenix0531-sudo/ZDEM_Model_Editor) | Model file visual editor |
| [ZDEM_Archiver](https://github.com/Phoenix0531-sudo/ZDEM_Archiver) | Purge / archive bulky simulation dumps |
| [ZDEM3D_WEB](https://github.com/Phoenix0531-sudo/ZDEM3D_WEB) | CAE cloud UI (Django + React + VTK.js) |
## License

MIT. Free for commercial use with attribution. See [LICENSE](LICENSE).
