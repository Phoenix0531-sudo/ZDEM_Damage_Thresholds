"""Smoke tests — keep green on empty / thin packages."""
from pathlib import Path
import importlib
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def test_repo_has_readme():
    assert (ROOT / 'README.md').exists()


def test_license_present():
    assert any((ROOT / n).exists() for n in ('LICENSE', 'LICENSE.md', 'LICENSE.txt'))


PACKAGES = ['plot2D']


def test_packages_importable():
    for name in PACKAGES:
        importlib.import_module(name)


def test_entry_compiles():
    src = ROOT / 'ZDEM_main_plot_damage_and_thresholds_from_dir.py'
    assert src.exists()
    compile(src.read_text(encoding='utf-8', errors='replace'), str(src), 'exec')

