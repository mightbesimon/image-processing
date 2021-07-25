def mean(image):
	copy = image[2:] + image[1:-1] + image[:-2]
	copy = copy[:,2:] + copy[:,1:-1] + copy[:,:-2]
	return np.pad(copy/9, 1)

def mean_5(image):
	copy = image[4:] + image[3:-1] + image[2:-2] + image[1:-3] + image[:-4]
	copy = copy[:,4:] + copy[:,3:-1] + copy[:,2:-2] + copy[:,1:-3] + copy[:,:-4]
	return np.pad(copy/25, 2)

def gaussian(image):
	...