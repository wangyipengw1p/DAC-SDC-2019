# Train your own data on [Simpledet](https://github.com/TuSimple/simpledet)
### Install
SimpleDet contains a lot of C++ operators not in MXNet offical repo, so one has to build MXNet from scratch. Please refer to [INSTALL.md](https://github.com/TuSimple/simpledet/blob/master/doc/INSTALL.md) more details
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
For training DAC-SDC dataset, one can organize data in coco-like format, It's recommand to place data under \<simpledet-dir\>
```
data/
    coco/
        annotations/
            instances_DAC-SDC.json
            DAC-SDC                   # Not officially required
        images/
            DAC-SDC
```
The file name and path in DAC-SDC dataset is a disaster, even including Chinese bracket. So run `move_imgs_anno.sh` to gather all imgs and xml desired folder and rename them like this

**compulsory to continue**
```
<classname>_<filename>
e.g.  boat1_000001.jpg  boat1_000001.xml
```

Since coco needs .json file while DAC provides xml format, so one should do the conversion using `data_to_coco.py`, which require a input file recording the name of all imgs
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
Copy `get_file_name.sh` to `data/coco/images/DAC-SDC` and run
```
sh get_file_name.sh
```
A `output.txt` will be generated, now move it to the same folder with `data_to_coco.py` and command (remember to change the path)
```
python data_to_coco.py output.txt data/coco/annotations/instances_DAC-SDC.json
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
 # usually on DAC-SDC, we are traing from scratch, so set this to TRUE
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
