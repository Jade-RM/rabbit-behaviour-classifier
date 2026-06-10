from pathlib import Path

import numpy as np
from PIL import Image

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X = []
y = []

for label in ["Active", "Inactive"]:

    folder = Path("dataset") / label

    for image_file in folder.glob("*.jpg"):

        img = Image.open(image_file)

        # shrink images to something manageable
        img = img.resize((64, 64))

        # convert to numpy array
        arr = np.array(img)

        # flatten into a long vector
        arr = arr.flatten()

        X.append(arr)
        y.append(label)

X = np.array(X)

print(f"Loaded {len(X)} images")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print(f"Training images: {len(X_train)}")
print(f"Test images: {len(X_test)}")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nResults:\n")

print(classification_report(y_test, predictions))