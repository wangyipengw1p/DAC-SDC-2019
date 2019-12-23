# -*- coding: utf-8 -*-
"""
    This script allows you to transfer your own data from your own data format to coco format.

    Attention: This is not the official format, it does not require licenses and other redundant info, but can generate
    coco-like dataset which can be accepted by Simpledet.

    TODO: You should reimplement the code line 22, this file only describe the format of dataset
    and the way to save it.
"""

import json
import sys
from xml.dom.minidom import parse

def main():
	if len(sys.argv) < 3:
		print("Usage: python data_to_coco.py infile outfile")
		exit(1)
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	#### To do : change the path for image and annotations ###
	img_path = ''	# e.g. data/coco/images/DAC-SDC/
	ann_path = ''	
    # The whole coco dataset
	dataset = {
		'licenses': [],
		'info': {},
		'categories': [],   # Required
		'images': [],       # Required
		'annotations': []   # Required
	}

    #  class_map maps the class, which would be added into dataset['categories']
	class_map = {

		"boat1"			:	1	,
		"boat2"			:	2	,
		"boat3"			:	3	,
		"boat4"			:	4	,
		"boat5"			:	5	,
		"boat6"			:	6	,
		"boat7"			:	7	,
		"boat8"			:	8	,
		"building1"		:	9	,
		"building2"		:	10	,
		"building3"		:	11	,
		"car1"			:	12	,
		"car10"			:	13	,
		"car11"			:	14	,
		"car12"			:	15	,
		"car13"			:	16	,
		"car14"			:	17	,
		"car15"			:	18	,
		"car16"			:	19	,
		"car17"			:	20	,
		"car18"			:	21	,
		"car19"			:	22	,
		"car2"			:	23	,
		"car20"			:	24	,
		"car21"			:	25	,
		"car22"			:	26	,
		"car23"			:	27	,
		"car24"			:	28	,
		"car3"			:	29	,
		"car4"			:	30	,
		"car5"			:	31	,
		"car6"			:	32	,
		"car8"			:	33	,
		"car9"			:	34	,
		"drone1"		:	35	,
		"drone2"		:	36	,
		"drone3"		:	37	,
		"drone4"		:	38	,
		"group2"		:	39	,
		"group3"		:	40	,
		"horseride1"	:	41	,
		"paraglider1"	:	42	,
		"person1"		:	43	,
		"person10"		:	44	,
		"person11"		:	45	,
		"person12"		:	46	,
		"person13"		:	47	,
		"person14"		:	48	,
		"person15"		:	49	,
		"person16"		:	50	,
		"person17"		:	51	,
		"person18"		:	52	,
		"person19"		:	53	,
		"person2"		:	54	,
		"person20"		:	55	,
		"person21"		:	56	,
		"person22"		:	57	,
		"person23"		:	58	,
		"person24"		:	59	,
		"person25"		:	60	,
		"person26"		:	61	,
		"person27"		:	62	,
		"person28"		:	63	,
		"person29"		:	64	,
		"person3"		:	65	,
		"person4"		:	66	,
		"person5"		:	67	,
		"person6"		:	68	,
		"person7"		:	69	,
		"person8"		:	70	,
		"person9"		:	71	,
		"riding1"		:	72	,
		"riding10"		:	73	,
		"riding11"		:	74	,
		"riding12"		:	75	,
		"riding13"		:	76	,
		"riding14"		:	77	,
		"riding15"		:	78	,
		"riding16"		:	79	,
		"riding17"		:	80	,
		"riding2"		:	81	,
		"riding3"		:	82	,
		"riding4"		:	83	,
		"riding5"		:	84	,
		"riding6"		:	85	,
		"riding7"		:	86	,
		"riding8"		:	87	,
		"riding9"		:	88	,
		"truck1"		:	89	,
		"truck2"		:	90	,
		"wakeboard1"	:	91	,
		"wakeboard2"	:	92	,
		"wakeboard3"	:	93	,
		"wakeboard4"	:	94	,
		"whale1"		:	95	

    }
	for class_name, class_id in class_map.items():
		dataset['categories'].append({
			'id': class_id,
			'name': class_name,
			'supercategory': 'supercategory_name'
		})

    #  Load your own data
	i = 0
	with open(input_file, 'r') as in_file:
		for line in in_file:
			i = i + 1
			line = line[:-1]
			imgp =  line + '.jpg'
			anno = ann_path + line + '.xml'
			imgid = line.split('_')[0]
    #  Dataset images info, normally you should implement an iter here to append the info

			dataset['images'].append({
				'coco_url': '',
				'date_captured': '',
				'file_name': imgp,    # Required (str)    image file name
				'flickr_url': '',
				'id': int(i),        # Required (int)    id of image
				'license': '',
				'width': int(640),     # Required (int)    width of image
				'height': int(360)     # Required (int)    height of image
			})

    #  Dataset annotation info, normally you should implement an iter here to append the info
			with open(anno, 'r') as readfile:
				for line in readfile:
					if 'xmax' in line:
						xmax = filter(str.isdigit, line)
					if 'xmin' in line:
						xmin = filter(str.isdigit, line)
					if 'ymax' in line:
						ymax = filter(str.isdigit, line)
					if 'ymin' in line:
						ymin = filter(str.isdigit, line)
			
			barea = ( int(xmax) - int(xmin)) * (int(ymax) - int(ymin))
			dataset["annotations"].append({
				'area': int(barea),          # Required (int)    image area
				'bbox': [int(xmax), int(xmin), int(ymax), int(ymin)],    
				'category_id': int(class_map[imgid]),   # Required (int)    class id of this bbox
				'id': int(1),            # Required (int)    bbox id in this image
				'image_id': int(i),      # Required (int)    image id of this bbox
				'iscrowd': 0,           # Optional, required only if you want to train for semantic segmentation
				'segmentation': []      # Optional, required only if you want to train for semantic segmentation
			})

	with open(output_file, 'w') as ofile:
		json.dump(dataset, ofile, sort_keys=True, indent=2)


if __name__ == '__main__':
    main()
 
