'''	Image Processing

	contrast stretching of greyscale images
	 - min-max mapping
	 - percentile mapping
	 - historgram equalisation

	by simon | github.com/mightbesimon
'''

from time_this import time_this


#########################  histograms  #########################

def histogram(image):
	flat = image.flatten().tolist()
	return [flat.count(q) for q in range(256)]

def cumulative_histogram(image):
	hist = histogram(image)
	return [sum(hist[:q+1]) for q in range(256)]


####################  contrast stretching  #####################

@time_this
def min_max_mapping(image):
	gain = 255 / (image.max()-image.min())
	bias = -image.min() * gain
	print(f'performing min-max mapping: gain={gain}, bias={bias}')
	return image*gain + bias

@time_this
def percentile_mapping(image, a=.05, b=.95):
	N = image.size
	C = cumulative_histogram(image)
	qa = min(C.index(val) for val in C if a*N<val)
	qb = max(C.index(val) for val in C if val<b*N)
	print(f'performing percentile mapping: qa={qa}, qb={qb}')
	mapped = [ [round(255/(qb-qa) * (px-qa)) for px in row] for row in image ]
	return [ [0 if px<0 else 255 if px>255 else px for px in row] for row in mapped ]

@time_this
def histogram_equalisation(image):
	pixel_min = int(image.min()*255)
	pixel_max = int(image.max()*255)
	C = cumulative_histogram(image)
	T = [round(255 * (C[q]-C[pixel_min]) / (C[pixel_max]-C[pixel_min])) for q in range(256)]
	return [ [T[px] for px in row] for row in image ]

