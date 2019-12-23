#!/bin/sh

for folder in `ls ~/data_training` 
do
cd ~/data_training/$folder
for file in `ls *0001.jpg` 
do
cp ~/data_training/$folder/$file ~/darknet/train_yolov2_0512_test/JPEGImages/${folder}${file}
done
for file in `ls *0001.xml` 
do
cp ~/data_training/$folder/$file ~/darknet/train_yolov2_0512_test/Annotations/${folder}${file}
done

done