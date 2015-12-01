import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm

import midpoint as line_drawing

IMAGE_N = 50
IMAGE_A = np.zeros((IMAGE_N, IMAGE_N))


def draw_bezier(p0, p1, p2, p3, tolerance, img, img_n): 
	# unpack points
	(p0x, p0y) = p0
	(p1x, p1y) = p1
	(p2x, p2y) = p2
	(p3x, p3y) = p3

	# check to see if we can approximate with a flat line
	if is_flat(p0, p3, tolerance):
		line_drawing.midpoint_line_drawing(p0x, p0y, )