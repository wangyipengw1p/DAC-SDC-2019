#!/bin/sh
# Yipeng  2019.5.11
#Put this shell under the folder where exists the pictures only
#rename the output.txt and put it where you want

file=`ls *.jpg`
echo > output.txt
for item in $file
do
echo ${item%.*}  >> output.txt #name
# ${file##*.}  for extension
done