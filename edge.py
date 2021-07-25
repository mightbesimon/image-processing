'''	Image Processing

	sharpening of greyscale images
	 - sobel kernels
	 - edge detection
	 - sharpening

	by simon | github.com/mightbesimon

	[!] * * *   PLEASE NOTE   * * * [!]
	In this code, sobel and mean kernel operations may look weird.
	They are optimised for speed.
	For example, instead of [1 0 -1] * [a b c] = [1*a, 0*b, -1*c],
	it is simply a - c in my representation
	adapted for numpy ndarrays
'''

# custom decorator for timing functions
from time_this import time_this


#######################  edge detection  #######################

'''	[ 1  2  1]             [ 1]
	[ 0  0  0] = [1 2 1] x [ 0] x (1/4)
	[-1  0 -2]             [-1]
	    ^                 ^
  9 calculations    3 calculations
'''
@time_this
def sobel_horizontal(image):
	# * [1 0 -1]^T operation
	copy = image[:-2, :] - image[2:, :]
	# * [1 2 1] operation
	copy = copy[:, :-2] + 2*copy[:, 1:-1] + copy[:, 2:]
	# * (1/4) and padded
	return np.pad(copy/4, 1)

'''	[1  0 -1]               [1]
	[2  0 -2] = [1  0 -1] x [2] x (1/4)
	[1  0 -1]               [1]
	    ^                 ^
  9 calculations    3 calculations
'''
@time_this
def sobel_vertical(image):
	# [1  0 -1] operation
	copy = image[:, :-2] - image[:, 2:]
	# * [1 2 1]^T operation
	copy = copy[:-2, :] + 2*copy[1:-1, :] + copy[2:, :]
	# * (1/4) and padded
	return np.pad(copy/4, 1)

@time_this
def combine(image1, image2):
	# formula gm = sqrt( gx(x,y)^2 + gx(x,y)^2 )
	return (image1**2 + image2**2) ** 0.5

@time_this
def combine_fast(image1, image2):
	# using the appromimate formula gm = |gx(x,y)| + |gy(x,y)|
	return abs(image1) + abs(image2)

def get_edges(image):
	edges_h = sobel_horizontal(image)
	edges_v = sobel_vertical  (image)
	return  combine(edges_h, edges_v)
	

##########################  sharpen  ###########################

def sharpen(image):
	edges = get_edges(image)
	return  combine(image, edges)
