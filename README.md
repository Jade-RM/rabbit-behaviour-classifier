# Rabbit Behaviour Classifier

A prototype machine learning project to classify rabbit behaviour from video frames.

A workflow was developed to extract frames from videos of one or two rabbits either resting or doing activities.
Frames were then labelled according to observed behvaiour and a machine learning dataset was created from the labelled frames.
A classifier was trained to identify the rabbit's behaviours.

This is a simple classifier currently with only two observed states:

- Active
- Inactive

Dataset:

- 335 labelled images
- 186 Active
- 149 Inactive

Python and Python libraries were used to build this project.

The pilot prototype has been completed. The model has an accuracy of 100% using the current data and behavioural states of active/inactive.
This indicates issues with the data and/or classifications used. However, it also demonstrates that the prototype pipeline is functioning.