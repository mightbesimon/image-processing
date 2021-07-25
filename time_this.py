'''	COMPSCI 373 (2021) - University of Auckland
	ASSIGNMENT ONE - QR Code Detection
	Simon Shan  441147157

	Decorator that times functions
	prints [function name,  time took, total elapsed time]
'''

from time import time


class time_this():

	elapsed_time = []

	def __init__(self, function):
		self.function = function
		self.name     = function.__name__

	def __call__(self, *args, **kwargs):
		start  = time()
		result = self.function(*args, **kwargs)
		finish = time()

		self.elapsed_time.append(finish-start)

		print(f'function: {self.name}{" "*(20-len(self.name))} took: {finish-start:.4f}s       total elapsed time: {sum(self.elapsed_time):.4f}s')
		return result
