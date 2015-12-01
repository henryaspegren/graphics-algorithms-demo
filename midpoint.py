import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm


def draw_octant_1(x_start, y_start, x_end, y_end, img, img_n):
	# k(x, y) = ax + by + c
	# k < 0 -> above the line
	# k > 0 -> below the line
	a = float((y_end-y_start))
	b = float(-(x_end-x_start))
	c = float(x_end*y_start - x_start*y_end)

	x = round(x_start)
	y = round((-a*x - c)/b)

	# get the first decision point
	d = a*(x+1) + b*(y+0.5) + c
	while(x <= round(x_end)):
		img[img_n/2-y][x+img_n/2] = 1

		# if above the line go E
		# d' = (a(x+2)+ b(y+0.5) + c)
		#    = (a(x+1)+ a + b(y+0.5) + c)
		#	 = d + a 
		if d < 0:
			d = d + a
		# if below the line go NE
		# d' = (a(x+2)+ b(y+1.5) + c)
		#    = (a(x+1)+ a + b(y+0.5) + b + c)
		#	 = d + a + b
		else:
			d = d + a + b
			y = y + 1
		# increment x every time
		x = x + 1

def draw_octant_2(x_start, y_start, x_end, y_end, img, img_n):
	a = float((y_end-y_start))
	b = float(-(x_end-x_start))
	c = float(x_end*y_start - x_start*y_end)

	x = round(x_start)
	y = round((-a*x - c)/b)

	# get the first decision point
	d = a*(x+0.5) + b*(y+1) + c
	while(y <= round(y_end)):
		img[img_n/2-y][x+img_n/2] = 1

		# d = (a(x+0.5) + b(y+1) + c)

		# if above the line go NE
		# d' = (a(x+1.5)+ b(y+2) + c)
		#    = (a(x+0.5)+ a + b(y+1) + b + c)
		#	 = d + a + b
		if d < 0:
			d = d + a + b
			x = x + 1
		# if below the line go N
		# d' = (a(x+0.5)+ b(y+2) + c)
		#    = (a(x+0.5)+ b(y+1) + b + c)
		#	 = d + b
		else:
			d = d + b
		# increment y every time
		y = y + 1


def draw_octant_8(x_start, y_start, x_end, y_end, img, img_n):
	a = float((y_end-y_start))
	b = float(-(x_end-x_start))
	c = float(x_end*y_start - x_start*y_end)
	x = round(x_start)
	y = round((-a*x - c)/b)

	# get the first decision point
	d = a*(x+1) + b*(y-0.5) + c
	while(x <= round(x_end)):
		img[img_n/2-y][x+img_n/2] = 1

		# d = (a(x+1) + b(y-0.5) + c)

		# if above the line go SE
		# d' = (a(x+2)+ b(y-1.5) + c)
		#    = (a(x+1)+ a + b(y-0.5) - b + c)
		#	 = d + a - b
		if d < 0:
			d = d + a - b
			y = y - 1
		# if above the line go E
		# d' = (a(x+2)+ b(y-0.5) + c)
		#    = (a(x+1)+ a + b(y-0.5) + c)
		#	 = d + a			
		else:
			d = d + a
		# increment x
		x = x + 1


def draw_octant_7(x_start, y_start, x_end, y_end, img, img_n):
	a = float((y_end-y_start))
	b = float(-(x_end-x_start))
	c = float(x_end*y_start - x_start*y_end)
	m = -a/b
	x = round(x_start)
	y = round((-a*x - c)/b)
	# get first decision point
	d = a*(x+0.5) + b*(y-1) + c
	while(y >= round(y_end)):
		img[img_n/2-y][x+img_n/2] = 1

		# d = (a(x+0.5) + b(y-1) + c)

		# if above the line go E
		# d' = (a(x+0.5)+ b(y-2) + c)
		#    = (a(x+0.5)+ b(y-1) - b + c)
		#	 = d - b
		if d < 0:
			d = d - b
		# if below the line go SE
		# d' = (a(x+1.5)+ b(y-2) + c)
		#    = (a(x+0.5)+ a + b(y-1) - b + c)
		#	 = d + a - b			
		else:
			d = d + a - b
			x = x + 1
		# decrement y
		y = y - 1

def midpoint_line_drawing(x_start, y_start, x_end, y_end, img, img_n):
	a = float((y_end-y_start))
	b = float(-(x_end-x_start))
	c = float(x_end*y_start - x_start*y_end)
	m = -a/b
	# Octant 1 
	if (0 <= m <= 1):
		print('Calling Octant 1')
		draw_octant_1(x_start, y_start, x_end, y_end, img, img_n)
		# we just reverse the end points for all cases. this is to cover the other 
		# quadrants
		draw_octant_1(x_end, y_end, x_start, y_start, img, img_n)
	# Octant 2
	if m > 1:
		print('Calling Octant 2')
		draw_octant_2(x_start, y_start, x_end, y_end, img, img_n)
		draw_octant_2(x_end, y_end, x_start, y_start, img, img_n)
	# Octant 8
	if -1 <= m < 0:
		print('Calling Octant 8')
		draw_octant_8(x_start, y_start, x_end, y_end, img, img_n)
		draw_octant_8(x_end, y_end, x_start, y_start, img, img_n)

	# Octant 7
	if m < -1:
		print('Calling Octant 7')
		draw_octant_7(x_start, y_start, x_end, y_end, img, img_n)
		draw_octant_7(x_end, y_end, x_start, y_start, img, img_n)


def draw_circle_at_origin(r, img, img_n):
	# circle is parameterized by x^2 + y^2 = r^2
	# d = x^2 + y^2 - r^2
	# d > 0 outside circle
	# d < 0 inside
	# d = 0 on circle

	# start at (0, r)
	y = round(r)
	x = 0
	d = (x+1)**2 + (y-0.5)**2 - r**2

	# cutoff at round(sqrt(2)/2 * r)
	x_cutoff = round((2**(0.5)/2)*r)
	while(x <= x_cutoff):
		img[img_n/2-y][x+img_n/2] = 1 			# OCTANT 2
		img[img_n/2-y][(-x)+img_n/2] = 1 		# OCTANT 3
		img[img_n/2-(-y)][(-x)+img_n/2] = 1 	# OCTANT 6
		img[img_n/2-(-y)][x+img_n/2] = 1 		# OCTANT 7
		img[img_n/2-x][y+img_n/2] = 1 			# OCTANT 1
		img[img_n/2-(-x)][y+img_n/2] = 1 		# OCTANT 4
		img[img_n/2-(-x)][(-y)+img_n/2] = 1 	# OCTANT 5
		img[img_n/2-x][(-y)+img_n/2] = 1 		# OCTANT 8

		# d = (x+1)^2 + (y-0.5)^2 - r^2
		#	= x^2 + 2x + 1 + y^2 - y + 0.25 - r^2

		# if outside circle -> move SE
		if d > 0:
			# d' = (x+2)^2 + (y-1.5)^2 - r^2
			#    = x^2 + 4x + 4 + y^2 - 3y + 2.25 - r^2
			#	 = d + 2x + 3 -2y - 2
			d = d + 2*x + 3 - 2*y - 2
			y = y - 1
		# if inside the circle -> move E
		else:
			# d' = (x+2)^2 + (y-0.5)^2 - r^2
			#    = x^2 + 4x + 4 + y^2 - y + 0.25 - r^2
			#	 = d + 2x + 3
			d = d + 2*x + 3
		x = x + 1
	return 

"""
IMAGE_N = 50
IMAGE_A = np.zeros((IMAGE_N, IMAGE_N))

# Quadrant 1
midpoint_line_drawing(0, 0, 20.3, 9.9, IMAGE_A, IMAGE_N)

# Quadrant 2
midpoint_line_drawing(0, 0, 10.9, 24.1, IMAGE_A, IMAGE_N)

# Quadrant 8
midpoint_line_drawing(0, 0, 20.4, -15.6, IMAGE_A, IMAGE_N)

# Quadrant 7
midpoint_line_drawing(0, 0, 10.1, -20.6, IMAGE_A, IMAGE_N)


imgplot = plt.imshow(IMAGE_A, cmap = cm.Greys_r, interpolation="nearest")
plt.show()

IMAGE_B = np.zeros((IMAGE_N, IMAGE_N))
draw_circle_at_origin(20, IMAGE_B, IMAGE_N)


imgplot = plt.imshow(IMAGE_B, cmap = cm.Greys_r, interpolation="nearest")
plt.show()
"""


