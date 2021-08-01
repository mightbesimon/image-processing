from matplotlib import pyplot as plt
from matplotlib.widgets import Button, TextBox

from commands import commands


MRGN = .025		# margin
SPRT = .75		# separator
BNHT = .05		# button height


class Interface:

	def __init__(self):
		self.setup()
		self.load_image()
		# plt.show()
		input()

	def setup(self):
		plt.ion()		# interactive mode on
		plt.figure('Image Processing - Interface')
		# plt.subplots_adjust(left=0, right=SPRT, top=1, bottom=0)
		plt.subplots_adjust(left=0, right=SPRT, top=.9, bottom=0)
		plt.axis('off')

		self.image = None
		self.axes  = plt.gca()
		self.buttons = []

		pos = .925
		# axes = plt.axes((SPRT+MRGN, pos, 1-SPRT-2*MRGN, BNHT))
		axes = plt.axes((MRGN, pos, SPRT, BNHT))
		self.filename_box_load = TextBox(axes, '', initial='images/snowtree.png')
		self.filename_box_load.on_submit(self.load_image)

		pos = .925
		for command, function in commands.items():
			function = self.wrap(function)
			axes = plt.axes((SPRT+MRGN, pos, 1-SPRT-2*MRGN, BNHT))	# bottom-left x,y	width, height
			button = Button(axes, command)
			button.on_clicked(function)
			self.buttons.append(button)
			pos -= BNHT + 0

		# pos = .925
		# # axes = plt.axes((SPRT+MRGN, pos, 1-SPRT-2*MRGN, BNHT))
		# axes = plt.axes((MRGN, pos, SPRT, BNHT))
		# self.filename_box_load = TextBox(axes, '', initial='images/snowtree.png')
		# self.filename_box_load.on_submit(self.load_image)
		# # pos -= BNHT
		# function = self.wrap(commands['load'])
		# axes = plt.axes((SPRT+MRGN, pos, 1-SPRT-2*MRGN, BNHT))	# bottom-left x,y	width, height
		# button = Button(axes, 'load')
		# button.on_clicked(function)
		# self.buttons.append(button)

	def wrap(self, function):
		def wrapper(mouse_event):
			self.image = function(self.image)
			self.update_image()
			print('executed')

		return wrapper

	def load_image(self, filename='images/11.png'):
		commands['load'](self, filename)

	def update_image(self):
		self.axes.imshow(self.image, cmap='gray')


if __name__ == '__main__':
	Interface()
