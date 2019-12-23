import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets=[('2019', 'DAC-SDC')]
###########################
classes = ["boat1",
"boat2",
"boat3",
"boat4",
"boat5",
"boat6",
"boat7",
"boat8",
"building1",
"building2",
"building3",
"car1",
"car10",
"car11",
"car12",
"car13",
"car14",
"car15",
"car16",
"car17",
"car18",
"car19",
"car2",
"car20",
"car21",
"car22",
"car23",
"car24",
"car3",
"car4",
"car5",
"car6",
"car8",
"car9",
"drone1",
"drone2",
"drone3",
"drone4",
"group2",
"group3",
"horseride1",
"paraglider1",
"person1",
"person10",
"person11",
"person12",
"person13",
"person14",
"person15",
"person16",
"person17",
"person18",
"person19",
"person2",
"person20",
"person21",
"person22",
"person23",
"person24",
"person25",
"person26",
"person27",
"person28",
"person29",
"person3",
"person4",
"person5",
"person6",
"person7",
"person8",
"person9",
"riding1",
"riding10",
"riding11",
"riding12",
"riding13",
"riding14",
"riding15",
"riding16",
"riding17",
"riding2",
"riding3",
"riding4",
"riding5",
"riding6",
"riding7",
"riding8",
"riding9",
"truck1",
"truck2",
"wakeboard1",
"wakeboard2",
"wakeboard3",
"wakeboard4",
"whale1"]



def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(year, image_id):
    in_file = open('Annotations/%s.xml'%( image_id))
    out_file = open('labels/%s.txt'%(image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = 0     #obj.find('difficult').text#######################
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

for year, image_set in sets:
    if not os.path.exists('labels/'):
        os.makedirs('labels/')
    image_ids = open('ImageSets/Main/train.txt').read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/JPEGImages/%s.jpg\n'%(wd,image_id))
        convert_annotation(year, image_id)
    list_file.close()

################
os.system("cat 2019_DAC-SDC.txt > train.txt")
os.system("cat 2019_DAC-SDC.txt > train.all.txt")

