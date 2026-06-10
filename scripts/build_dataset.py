import pandas as pd
import shutil
from pathlib import Path

labels = pd.read_csv("frame_labels.csv")

Path("dataset/Active").mkdir(parents=True, exist_ok=True)
Path("dataset/Inactive").mkdir(parents=True, exist_ok=True)

for _, row in labels.iterrows():

    source = (
        Path("extracted_frames")
        / row["video"]
        / row["frame"]
    )

    destination = (
        Path("dataset")
        / row["label"]
        / f"{row['video']}_{row['frame']}"
    )

    shutil.copy(source, destination)

print("Dataset created.")