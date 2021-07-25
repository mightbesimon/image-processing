# convert from greyscale to binary

def thresholding(image, threshold):
	return np.array(image<threshold, dtype=np.unint8)

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