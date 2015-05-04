#coding=utf-8
#!/usr/bin/python

import os

def checkFolderExists(folder_path):
	path_exist=os.path.exists(folder_path)
	if path_exist:
	    pass
	else:
	    os.mkdir(folder_path)
