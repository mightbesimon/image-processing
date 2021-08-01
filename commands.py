import file
import contrast
import smooth
import edge
import binary

commands = {
	'load':file.load,
	'save':file.save,
	# 'log' :operations.log,

	'histogram' : contrast.histogram,
	'cumulative': contrast.cumulative_histogram,
	'min-max'   : contrast.min_max_mapping,
	'percentile': contrast.percentile_mapping,
	'hist-eq'   : contrast.histogram_equalisation,

	'mean'    : smooth.mean,
	'gaussian': smooth.gaussian,

	'sobelh' : edge.sobel_horizontal,
	'sobelv' : edge.sobel_vertical,
	# 'combine': edge.combine,
	'edge'   : edge.edge_image,
	'sharpen': edge.sharpen,

	'thresholding': binary.thresholding,
	'pointillism' : binary.pointillism,
	'erosion'     : binary.erosion,
	'dilation'    : binary.dilation,
	'opening'     : binary.opening,
	'closing'     : binary.closing,
}