# PedestrainDetection
Pedestrian Detection using INRIA dataset and YOLO model with [Darknet](https://pjreddie.com/darknet/yolo/) framework.

I trained the model following the steps from [AlexeyAB](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects)

## Scripts
You can find the scripts that convert the annotations of the INRIA dataset into the labels required for Darknet.

You can find the converted labels in the INRIAPerson folder within the Train and Test folders respectively.

Also, you can graph your current AVG Loss with the ShowTraining script.

## Training
The files inria.data and inria.names should go in the /data folder of darknet.
Don't forget to create the train.txt and test.txt that inria.data calls.

Finally, start training using the following command:

<pre>$ ./darknet -i 0 detector train data/inria.data cfg/yolov3_inria.cfg darknet53.conv.74</pre>

Nevertheless, you can use the RunNonStop script, if you sometimes you training stops because of insufficient memory.

## Demos

Check some results with Caltech Pedestrian dataset (videos)

[Test1](https://vimeo.com/245870357)
[Test2](https://vimeo.com/245870532)
