


from matplotlib import pyplot as plt
import numpy as np


# @time_this
def image_read(filename):
	image = plt.imread(filename)

	# already greyscale -> return as is
	if image.ndim==2:
		return image
	# greyscale and alpha -> remove alpha
	if image.shape[2]==2:
		return image[...,1]
	# rgb or rgba -> convert to greyscale
	return rgb_to_greyscale(image[...,:3])

def rgb_to_greyscale(rgb_triplets):
	return rgb_triplets @ (.299, .587, .114)

# @time_this
def image_write(filename, pixels):
	plt.imsave(filename, pixels, cmap='gray')

def to255(image):
	# return np.array(image*255, dtype=np.uint8)
	return np.array(image*255, dtype=np.int32)


def load(interface, filename):
	interface.image = image_read(filename)
	interface.update_image()
	print(f'[image loaded] {filename}')

def save(filename):
	...


# class img:
# 	counter = 1
# 	current = None

# def load(filename):
# 	# global current
# 	image = image_read(filename)
# 	image_write('workspace/current.png', image)
# 	img.current = image

# def save(filename=None):
# 	# global counter, current
# 	if not filename:
# 		filename = f'workspace/{img.counter}.png'
# 		img.counter += 1
# 	image_write(filename, img.current)

# global counter, current
# img.counter = 1
# img.current = None

# plt.figure('workspace')
# plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
# plt.axis('off')

# plt.imshow(image_read('834.png'), cmap='gray')
# a = input('>>> ')
# plt.show()
# a = input('>>> ')