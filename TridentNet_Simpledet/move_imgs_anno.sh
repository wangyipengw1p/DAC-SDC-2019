#!/bin/sh

# To do : modify the path
DACSDCPATH=/home/<usr>/data_training  # original data path
SIMPLEDETDATA=<simpledet-dir>/data/coco

# Note that the folder name is the class name
for folder in `ls $DACSDCPATH` 
do
	for file in `ls $DACSDCPATH/$folder/*.jpg`
	do
		cp $file $SIMPLEDETDATA/images/DAC-SDC/${folder}_${file}
	done
	for file in `ls $DACSDCPATH/$folder/*.xml`
	do
		cp $file $SIMPLEDETDATA/annotations/DAC-SDC/${folder}_${file}
	done

done