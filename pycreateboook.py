#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import os.path
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

rootdir = 'C:\Users\Flowerowl\Desktop\django'

def walkFolder(rootdir):
	for parent,dirnames,filenames in os.walk(rootdir): 
		for filename in filenames:  
			path = os.path.join(parent, filename)
			spath = '\\'.join(os.path.join(parent, filename).split('\\')[4:])
			convert(path, spath)

def convert(path, spath):
	f = open(path,'r')
	context = f.read()
	f.close()
	fp = open('djangobook.txt','a')
	spath = '=============================='+spath
	fp.write('\r\n'+spath)
	fp.write('\r\n'+context)
	fp.close()

walkFolder(rootdir)