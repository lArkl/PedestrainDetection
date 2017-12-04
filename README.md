# PedestrainDetection
Pedestrian Detection using INRIA dataset and YOLO model with [Darknet](https://pjreddie.com/darknet/yolo/) framework.

I trained the model following the steps from [AlexeyAB](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects)

## Scripts
You can find the scripts that convert the annotations of the INRIA dataset into the labels required for Darknet.

You can find the converted labels in the INRIAPerson folder within the Train and Test folders respectively. 

## Training
The files inria.data and inria.names should go in the /data folder of darknet.
Don't forget to create the train.txt and test.txt that inria.data calls.

Finally, start training using the following command:

<pre>$ ./darknet detector train data/inria.data cfg/yolo-inria.cfg darknet19_448.conv.23</pre>
