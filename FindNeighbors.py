import sys
from os import listdir, mkdir
from os.path import exists, isdir, join
import numpy as np
from skimage import transform
from PIL import Image
import gist
import cv2
from sklearn.neighbors import NearestNeighbors

argv = sys.argv
argc = len(argv)

if (argc < 2):
	print "Not enough arguments. Second argument should be path to the image folder sample/spatial..."
	quit(1)


input_dir = argv[1]

imsize = (128, 128)
arrays = np.array(np.random.randint(2,4, (1,960)))

random_index = np.random.randint(2680)
features = {}
names = []
filemap = []
ind = []
filenames = listdir(input_dir)
print filenames
for filename in filenames:
	# print filename

	

	names.append(filename)
	filepath = join(input_dir, filename)

	try:
		pilimg = Image.open(filepath)
	except:
		continue

	img = np.asarray(pilimg)
	# img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	img_resized = transform.resize(img, imsize, preserve_range=True).astype(np.uint8)
	desc = gist.extract(img_resized)
	arrays = np.vstack((arrays, desc))

	class_name = filename.split('_')[0]
	# print "class_name", class_name


	if "coast" in filename:
		val = 1
	elif "forest" in filename:
		val = 2
	elif "highway" in filename: 
		val = 3
	elif "insidecity" in filename: 
		val = 4
	elif "highway" in filename: 
		val = 5
	elif "mountain" in filename: 
		val = 6
	elif "opencountry" in filename: 
		val = 7
	elif "street" in filename: 
		val = 8
	elif "tallbuilding" in filename: 
		val = 9

	
	ind.append(filename)
	filemap.append(val)

	print len(filemap)
	print len(ind)
	# ind.append(val)

	if (class_name in features):
		features[class_name] = np.vstack((features[class_name], desc))
	else:
		features[class_name] = np.atleast_2d(desc)

# print features['myImage.jpg'].shape
print arrays.shape
arrays = arrays[1:, :]

nbrs = NearestNeighbors(n_neighbors=7, algorithm='kd_tree').fit(arrays)
distances, indices = nbrs.kneighbors(arrays)
for i in indices[random_index]:
	print filemap[i], ind[i]

f2 = open("filemap.txt", "w+")
f3 = open("indexmap.txt", "w+")
for i in indices:
	for j in i:
		f2.write(str(filemap[j]) + " ")
		f3.write(str(ind[j]) + " ")
	f2.write("\n")
	f3.write("\n")

# for i in indices:
# 	for j in i:
# 		print ind[j]
# distances, indices = nbrs.kneighbors(arrays)
# for i in indices:
# 	for j in i:
# 		print ind[j]

# 	print "\n\n"

# print names
# print indices
# # for class_name, desc_mat in features.items():
# 	np.save(join(output_dir, class_name+'.npy'), desc_mat)
