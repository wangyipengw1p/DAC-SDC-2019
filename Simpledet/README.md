# Train your own data on [Simpledet](https://github.com/TuSimple/simpledet)
### Install
SimpleDet contains a lot of C++ operators not in MXNet offical repo, so one has to build MXNet from scratch. Please refer to [INSTALL.md](https://github.com/TuSimple/simpledet/blob/master/doc/INSTALL.md) more details
### Download the [DAC-SDC dataset](https://pitt.app.box.com/s/756141768nn92cj0dkfbg6dan17c4h4q0)
### Organize data
SimpleDet requires groundtruth annotation organized as following format, and provides tools for COCO-like dataset. 
```
[
    {
        "gt_class": (nBox, ),
        "gt_bbox": (nBox, 4),
        "flipped": bool,
        "h": int,
        "w": int,
        "image_url": str,
        "im_id": int,
        
        # this fields are generated on the fly during test
        "rec_id": int,
        "resize_h": int,
        "resize_w": int,
        ...
    },
    ...
]
```
For training DAC-SDC dataset, one can organize data in coco-like format, It's recommand to place data under $SIMPLEDET_DIR
```
data/
    coco/
        annotations/
            instances_DAC-SDC.json
            DAC-SDC                   # Not officially required
        images/
            DAC-SDC
```
The file name and path in DAC-SDC dataset is a disaster, so run [`move_imgs_anno.sh`](https://github.com/wangyipengw1p/DAC-SDC-2019/tree/master/Simpledet/move_imgs_anno.sh) to gather all imgs and xml desired folder and rename them like this

**compulsory to continue**
```
<classname>_<filename>
e.g.  boat1_000001.jpg  boat1_000001.xml
```
> Note that the filename of the DAC-SDC dataset even including Chinese bracket, which could not be recognized by some `bash`. So you may need to deal with this problem first. The simplest method is to select only last four charactor of the original filename, using python.

Then  open `data_to_coco.py` to change the path
```
<line 22>

#### To do : change the path for image and annotations ###
	img_path = ''	# e.g. data/coco/images/DAC-SDC/
	ann_path = ''
```

Since coco needs .json file while DAC provides xml format, so one should do the conversion using [`data_to_coco.py`](https://github.com/wangyipengw1p/DAC-SDC-2019/blob/master/Simpledet/data_to_coco.py), which require a input file recording the name of all imgs
```
<inputfile>

building1_000001
building1_000002
building1_000003
building1_000004
building1_000005
building1_000006
...
```
Copy [`get_file_name.sh`](https://github.com/wangyipengw1p/DAC-SDC-2019/tree/master/Simpledet/get_file_name.sh) to `data/coco/images/DAC-SDC` and run
```
sh get_file_name.sh
```
A `output.txt` will be generated, now move it to the same folder with [`data_to_coco.py`](https://github.com/wangyipengw1p/DAC-SDC-2019/tree/master/Simpledet/data_to_coco.py) and command 
```
python data_to_coco.py output.txt data/coco/annotations/instances_DAC-SDC.json
```
### Generate the roidb
```
cd $SIMPLEDET_DIR
python3 utils/generate_roidb.py --dataset coco --dataset-split DAC-SDC
```
Then the roidb will be generated to `data/cache`
### Deploy dependency and compile extension
```
cd $SIMPLEDET_DIR
git clone https://github.com/RogerChern/mxnext
```
### config the network
Choose the network in [config](https://github.com/TuSimple/simpledet/tree/master/config), and modify. Typically you should change

**compulsory**
```
gpus = [0, 1, 2, 3, 4, 5, 6, 7]     
# set according to your gpus, use 'nvidia-smi' to check, if you are using NVIDIA products
```
```
class DatasetParam:                 # change this origial image set to "coco_DAC-SDC"
        if is_train:
            image_set = ("coco_train2014", "coco_valminusminival2014", "coco_minival2014")
        else:
            image_set = ("coco_test-dev2017", )
```
```
from_scratch = False              
 # if you wang to traing from scratch, set this to TRUE. 
 # It's recommanded to train based on pre-trained coco model
```
```
# change the annotation path to "data/coco/annotations/instances_DAC-SDC.json"
class coco:                         
            annotation = "data/coco/annotations/instances_minival2014.json"
```
**selective**
```
ANYTHING you desire :)
```
### Train
```
python3 detection_train.py --config config/<config>.py
```
Now traing is Launched!

`nohup` will be useful if you're training on a server.

`mxnet` will run process to find the best algorithm to do the convolution, change the environment MXNET_CUDNN_AUTOTUNE_DEFAULT to 0 to disable.



