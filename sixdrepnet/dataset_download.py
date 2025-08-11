import kagglehub
from pathlib import Path

custom_dir = Path(r"C:\Users\bilal\OneDrive - National University of Ireland, Galway\dataset")

# Download latest version
path = kagglehub.dataset_download("kmader/biwi-kinect-head-pose-database",
                                  path=custom_dir)

print("Path to dataset files:", path)
kagglehub.dataset_download