# torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, sampler=None, num_workers=0, collate_fn=<function default_collate>, pin_memory=False, drop_last=False)
#batch_size是你批处理数目，shuffle是否每个epoch都打乱，workers是载入数据的线程数（请查看中文文档对每个参数的解释）

#[original_iamges.tensor,label.tensor]

import torch.utils.data 
import torch
#from tochvision import transforms
import os
import numpy as np


 

import glob
from PIL import Image




class DAC_SDC(torch.utils.data.Dataset):
	def __init__(self, name_txt, rootpath, train=True):
		self.rootpath = rootpath			
		self.train = train
		with open(name_txt, 'r') as file:
			self.names = file.readlines()
		self.class_map = {

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

	def __getitem__(self, idx): 
      
		img_path = self.root+'/Images/'+self.names[idx]+'.jpg'
		anno_path = self.root+'/Annotations/'+self.names[idx]+'.xml'
		imgclass = [0]*95
		imgclass[self.class_map[self.names[idx].split('-')[0]] - 1] = 1
		img = np.array(Image.open(img_path))
		img = torch.from_numpy(img).float() 
		if self.train:
			#bbox = [0, 0, 0, 0]			#There's only one bounding box per image, in DAC-SDC dataset, so it's simpler
			#with open(anno_path, 'r') as annof:
			#	
			#	for line in annof:
			#		if '<xmax>' in line:
			#			bbox[0] = filter(str.isdigit, line)
			#		elif '<xmin>' in line:
			#			bbox[1] = filter(str.isdigit, line)
			#		elif '<ymax>' in line:
			#			bbox[2] = filter(str.isdigit, line)
			#		elif '<ymin>' in line:
			#			bbox[3] = filter(str.isdigit, line)
			return img,imgclass
		return img
 
	def __len__(self):
		return len(self.names)
