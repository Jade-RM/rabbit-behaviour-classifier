# Rabbit Behaviour Classifier

A prototype machine learning project to classify rabbit behaviour from video frames.

A workflow was developed to extract frames from videos of one or two rabbits either resting or doing activities.
Frames were then labelled according to observed behvaiour and a machine learning dataset was created from the labelled frames.
A classifier was trained to identify the rabbit's behaviours.

The first classifier only classified two observed states:

- Active
- Inactive

Dataset:

- 335 labelled images
- 186 Active
- 149 Inactive

The second version classified three observed states:

- Eating
- Exploring
- Resting

Dataset:

- 129 Eating
- 57 Exploring
- 149 Resting

Python and Python libraries were used to build this project.

The pilot prototype has been completed. The model has an accuracy of 100% using the current data and behavioural states.
This indicates issues with the data and/or classifications used. However, it also demonstrates that the prototype pipeline is functioning.

In the next step, a class of Grooming was added to the dataset, and the frames were reclassified to include this class. The accuracy of the model has decreased due to this, but it is still at an acceptable level. I will now continue using this model without further modifications, and collect more data.

More data was collected in the next step, with 10 videos altogether. The model is able to better recognise the behaviours and the accuracy is quite high after being trained on the new data.

While random frame splitting showed an apparently high level of accuracy (>90%), this was reduced substantially when the model was evaluated on a previously unseen video using the script train_by_video, indicating that environmental factors may have led to false accuracy levels. More data is required to acheive a true high level of accuracy.