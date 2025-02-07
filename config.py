from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())


# Model config


IMG_FOLDER = ROOT / "images"

YOLO_CUSTOM = ROOT / "models" / "yolo_custom_model.pt"
YOLO_FACE = ROOT / "models" / "yolo_face_detection.pt"
YOLO_5EMO = ROOT / "models" / "yolo_5emotion.pt"
SWINV2 = ROOT / "swinv2_model" / "checkpoint-2516"
SWINV2_BOXED = ROOT / "swinv2_model" / "5emo_boxed"

SELECT_GIT_PATH = ROOT / "select_git.py"

DETECTION_MODEL_LIST = [
    "yolo_custom_model.pt",
    "yolo_face_detection.pt"
]