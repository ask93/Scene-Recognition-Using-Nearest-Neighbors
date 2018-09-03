
import sys
from os import listdir, mkdir
from os.path import exists, isdir, join
import numpy as np
from skimage import transform
from PIL import Image
import gist
import cv2
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

def find_accuracy():
	f = open("filemap.txt", "r")
	fl = f.readlines()
	matched_array = []
	for x in fl:
		g = x.strip().split(' ')
		matched_array.append(g)
	print matched_array
	numpy_array = np.array(matched_array)
	total_size =  numpy_array.shape[0] * numpy_array.shape[1]
	print len(np.where(numpy_array[:,0] != numpy_array[:, 1])[0])
	error = len(np.where(numpy_array[:,0] != numpy_array[:, 1])[0]) + len(np.where(numpy_array[:,0] != numpy_array[:, 2])[0]) + len(np.where(numpy_array[:,0] != numpy_array[:, 3])[0]) + len(np.where(numpy_array[:,0] != numpy_array[:, 4])[0])\
	 + len(np.where(numpy_array[:,0] != numpy_array[:, 5])[0]) + len(np.where(numpy_array[:,0] != numpy_array[:, 6])[0])
	print 1 - (1.0 * error/total_size)


find_accuracy()

def display():
	f = open("indexmap.txt", "r")
	fl = f.readlines()
	name_array = []
	for x in fl:
		g = x.strip().split(' ')
		name_array.append(g)

	print len(name_array)
	fileindex = np.random.randint(len(name_array))

	# fileindex = 7

	argv = sys.argv
	x = [400, 10, 470,930, 10, 470, 930]
	y = [300, 10, 10, 10, 480, 480, 480]

	input_dir = argv[1]
	j = 0
	k = 10
	for i in name_array[fileindex]:
		print join(input_dir, i) 
		img = cv2.imread(join(input_dir, i) ,1)
		cv2.namedWindow(i)
		cv2.moveWindow(i, x[j], y[j]);
		cv2.imshow(i,img)
		j += 1

	cv2.waitKey(0)

display()


# input_dir = argv[1]
# for i in name_array[fileindex]:
# 	print join(input_dir, i) 
# 	plt.figure()
# 	img = mpimg.imread(join(argv[1], i))
# 	plt.imshow(img)
# 	plt.show()



# fileindex = np.random.randint(len(input_array))
# name = join(input_dir, input_array[fileindex])
# img = cv2.imread(name,1)
# cv2.imshow('image',img)
# print join(input_dir, input_array[fileindex])
# for i in name_array[fileindex]:
# 	print join(input_dir, i)
# 	# name = join(input_dir, i)
# 	# img = cv2.imread(name,1)
# 	# cv2.imshow('image',img)


# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()