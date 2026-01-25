import yaml
from pathlib import Path

_STYLES_PATH = Path(__file__).parent / "styles.yaml"

def load_styles():
    # 加载styles.yaml文件
    with open(_STYLES_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)