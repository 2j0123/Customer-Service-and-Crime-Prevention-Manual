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
SWINV2 = ROOT / "swinv2_model" / "checkpoint-2516"

DETECTION_MODEL_LIST = [
    "yolo_custom_model.pt",
    "yolo_face_detection.pt"
]