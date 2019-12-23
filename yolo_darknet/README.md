# Run the solution

### build
> Note that this version of darknet is optimised from [original version](https://github.com/pjreddie/darknet) concerning performance and test mode.
```
$ git clone https://github.com/wangyipengw1p/DAC-SDC-2019.git
$ cd yolo-darknet/darknet_DAC
```
##### With CUDA

Change the Makefile
```
GPU=1
CUDNN=1
```

##### With OpenCV
Change the Makefile
```
OPENCV=1
```

```
$ make
```
If you have any errors, like the absence of `libopenblas.so`,`libtengine.so`. Try google for solution.

If everything seems to have compiled correctly, try running it!
```
./darknet
```
You should get
```
usage: ./darknet <function>
```

If you compiled using CUDA but want to do CPU computation for whatever reason you can use -nogpu to use the CPU instead:
```
./darknet -nogpu imagenet test cfg/alexnet.cfg alexnet.weights
```

### Run the solution
[Download the weight file](https://drive.google.com/open?id=1TKYFm1hXg8sItwvD7rAiw-66Of_Dik6C) to `test` folder.

Generate a text file which contains the path of all input images. Check the tools for help.

Then simply run

```
$ cd test
$ ../darknet test DAC-SDC.data yolov2-DAC.cfg yolo-final[0601].weights <path-to-text-file>
```

## Want to train yourself?
First, arrange data as indicated in `train` folder, with images in `JPEGImages` and annotations in `Annotations`.

Generate a text file which contains the path of all input images. Check the tools for help. Rename it to `train.txt` and copy to `ImageSets/Main`.

Then run
```
python3 label.py
```

Modify `yolov2-DAC.cfg` for training parameters
> Note that `filters` shoud be `3 * (classes + 5)`

Then start train by 
```
$ ./darknet detector train DAC-SDC.data yolov2-DAC.cfg [yolo-final[0601].weights] [-clear]
```
> `.weights` is optional incase you want to continue from where you left off.

If you are getting errors with `.weights` indicated, consider add `-clear`, which will clear the statistics but will not touch original weights.

