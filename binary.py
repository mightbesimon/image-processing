# convert from greyscale to binary

import numpy as np

from time_this import time_this

@time_this
def thresholding(image, threshold):
	return np.array(image<threshold, dtype=np.unint8)

@time_this
def pointillism(image):
	copy = np.random.rand(*image.shape)
	copy = np.array(copy<image, dtype=np.uint8)
	return copy


# morphological operations

def erosion(image):
	...

def dilation(image):
	...

def opening(image):
	...

def closing(image):
	...