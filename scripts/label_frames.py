import pandas as pd
from pathlib import Path

FPS = 2

behaviours = pd.read_csv("data/behaviours.csv")

frame_labels = []

for _, row in behaviours.iterrows():

    video = row["video"]
    start = float(row["start"])
    end = float(row["end"])
    label = row["label"]

    video_folder = Path("extracted_frames") / video

    if not video_folder.exists():
        print(f"Missing folder: {video_folder}")
        continue

    for frame_file in sorted(
        video_folder.glob("*.jpg"),
        key=lambda f: int(f.stem.split("_")[1])
        ):

        frame_num = int(frame_file.stem.split("_")[1])

        frame_time = frame_num / FPS

        if start <= frame_time <= end:

            frame_labels.append({
                "video": video,
                "frame": frame_file.name,
                "time": frame_time,
                "label": label
            })

output = pd.DataFrame(frame_labels)

output.to_csv("frame_labels.csv", index=False)

print(f"Created {len(output)} labels")
print(output.head())