from pathlib import Path

import numpy as np
from PIL import Image

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X_train = []
y_train = []

X_test = []
y_test = []

TEST_VIDEO = "rabbit_behaviour_10"

for label in ["Eating", "Exploring", "Grooming", "Resting"]:

    folder = Path("dataset") / label

    for image_file in folder.glob("*.jpg"):

        img = Image.open(image_file)
        img = img.resize((64, 64))

        arr = np.array(img).flatten()

        filename = image_file.name

        if filename.startswith(TEST_VIDEO):

            X_test.append(arr)
            y_test.append(label)

        else:

            X_train.append(arr)
            y_train.append(label)

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