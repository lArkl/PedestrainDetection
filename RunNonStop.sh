#!/bin/bash
cont=1
./darknet -i 0 detector train data/inria.data cfg/yolov3_inria.cfg darknet53.conv.74 |tee output.txt
while true; do
echo "fallo N $cont"
cont=$[$cont+1]
./darknet -i 0 detector train data/inria.data cfg/yolov3_inria.cfg backup/yolov3_inria.backup |tee -a output.txt
done
