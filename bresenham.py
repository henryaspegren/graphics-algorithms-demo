import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm

def bresenham_algo(x_start, y_start, x_end, y_end, img, img_n):
	m = (float(y_end)-float(y_start))/(float(x_end)-float(x_start))
	print('Slope is %f' %m)
	# Octant 1
	if(0 <= m <= 1):
		"""
		Here we ensure that each COLUMN has exactly one pixel
		"""
		print('In octant 1')
		# get the closest x val
		x = round(x_start)
		# now back out what its corresponding y value is
		yi = y_start+ m*(x-x_start)
		# round it
		y = round(yi)
		# yf is the fractional component
		# y is the integer part
		yf = yi - y
		# keep stepping throuhg the x values until we get to the end
		# which we have to round (get closest pixel)
		while x<=round(x_end):
			# make the origin in the middle
			img[img_n/2-y][x+img_n/2] = 1
			# slide through the x values
			x = x + 1
			# update the fractional value
			yf = yf + m
			# if this bumps us up to the next pixel
			if yf > 0.5:
				y = y + 1
				yf = yf - 1
	# Octant 2
	if m > 1:
		"""
		Here we ensure that each ROW has exactly one pixel
		"""
		print('In octant 2')
		y = round(y_start)
		# using 1/m because situation is reflected around y = x 
		xi = x_start+(1/m)*(y-y_start)
		x = round(xi)
		xf = xi - x
		# now slide through the y values until we get to the end
		while y <= round(y_end):
			img[img_n/2-y][x+img_n/2] = 1
			# slide through the y values
			y = y + 1
			# update the fractional component
			# note that we are adding 1/m here because the slope is x_1 - x_0 / y_1 - y_0
			xf = xf + 1/m
			# if over threshold
			if xf > 0.5:
				x = x + 1
				xf = xf - 1
	# Octant 8
	if -1 <= m < 0:
		""" 
		Here we ensure that each COLUMN has exactly one pixel
		"""
		print('In octant 8')
		x = round(x_start)
		yi = y_start+ m*(x-x_start)
		y = round(yi)
		yf = yi - y
		# keep stepping throuhg the x values until we get to the end
		# which we have to round (get closest pixel)
		while x<=round(x_end):
			img[img_n/2-y][x+img_n/2] = 1
			print('Now coloring %f %f' %(x, y))
			x = x + 1
			yf = yf + m
			# if this bumps us up to the next pixel
			# since going downward we take negative -0.5 as cutoff
			# and y values are decreasing
			if yf < -0.5:
				y = y - 1 # we subtract 1 since we move downward 
				yf = yf + 1 
	# Octant 7
	if m < -1:
		""" 
		Here we make sure that each ROW contains one pixel
		"""
		print('In Octant 7')
		# get the closest y value
		y = round(y_start)
		xi = x_start + (1/m)*(y-y_start)
		x = round(xi)
		xf = xi - x
		# NOTE: >= b/c y is decreasing
		while y >= round(y_end):
			img[img_n/2-y][x+img_n/2] = 1
			# Here we subtract because y values are decreasing
			y = y - 1
			xf = xf + -(1/m) #NOTE this is negative because x values are increasing
			# use the threshold of 0.5
			if xf > 0.5:
				x = x + 1
				xf = xf - 1

	"""
	All other cases are omitted because they can just be transformed into one of these four by switching the 
	end points [and using the exact same procedure] 
	"""
	return None

"""
Demonstration of each quadrant
"""


IMAGE_N = 50
IMAGE = np.zeros((IMAGE_N, IMAGE_N))

# Quadrant 1
bresenham_algo(0, 0, 20.3, 9.9, IMAGE, IMAGE_N)

# Quadrant 2
bresenham_algo(0, 0, 10.9, 24.1, IMAGE, IMAGE_N)

# Quadrant 8
bresenham_algo(0, 0, 20.4, -15.6, IMAGE, IMAGE_N)

# Quadrant 7
bresenham_algo(0, 0, 10.1, -20.6, IMAGE, IMAGE_N)



imgplot = plt.imshow(IMAGE, cmap = cm.Greys_r, interpolation="nearest")
plt.show()