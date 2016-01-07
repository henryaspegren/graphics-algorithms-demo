import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm

import midpoint as line_drawing


def draw_bezier(p0, p1, p2, p3, tolerance, img, img_n): 
	# unpack points
	(p0x, p0y) = p0
	(p1x, p1y) = p1
	(p2x, p2y) = p2
	(p3x, p3y) = p3

	# check to see if we can approximate with a flat line
	if is_flat(p0, p3, p1, tolerance) and is_flat(p0, p3, p2, tolerance):
		line_drawing.midpoint_line_drawing(p0x, p0y, p3x, p3y, img, img_n)
	else:
		# split into two bezier curves
		#
		# DO DERIVATION FOR THESE
		# Basically need three conditions:
		#	First q3 = P(1/2) = r(3)
		#	first_half(2t) = P(t) for t = [0, 0.5]
		#  	second_half(2t + 0.5) = P(t) for t = [0.5, 1]
		q0 = p0
		q1 = ((0.5*p0x+0.5*p1x), (0.5*p0y+0.5*p1y))
		q2 = ((0.25*p0x + 0.5*p1x + 0.25*p2x), (0.25*p0y + 0.5*p1y + 0.25*p2y))
		q3 = ((0.125*p0x + 0.375*p1x + 0.375*p2x + 0.125*p3x), (0.125*p0y + 0.375*p1y + 0.375*p2y + 0.125*p3y))
		draw_bezier(q0, q1, q2, q3, tolerance, img, img_n)
		r0 = q3
		r1 = ((0.25*p1x + 0.5*p2x + 0.25*p3x), (0.25*p1y + 0.5*p2y + 0.25*p3y))
		r2 = ((0.5*p2x + 0.5*p3x), (0.5*p2y + 0.5*p3y))
		r3 = p3
		draw_bezier(r0, r1, r2, r3, tolerance, img, img_n)


def is_flat(a, b, c, t):
	"""
		returns true if the distance between the line AB and the point C
		is less than t and returns false otherwise
	"""
	(ax, ay) = a
	(bx, by) = b
	(cx, cy) = c
	# A line is parameterized by 
	# P(s) = (1-s)*a + s*b 
	# P(s)_x = (1-s)ax + s*bx
	# P(s)_y = (1-s)ay + s*by
	# for s = [0, 1]
	# WANT: the closest point on line(ab) to point c

	# Now we have to derive the condition for the closest point on line
	# closest when
	# AB dot CP(s) = 0  where CP(s) is the line from P(s) to C
	# 
	# AB = B - A
	# AB_x = bx - ax
	# AB_y = by - ay
	#
	# plugging in for CP(s) = P(s) - C
	# CP(s)_x = (1-s)ax + s*bx - cx
	# CP(s)_y = (1-s)ay + s*by - cy
	#
	# Now set the dot product equal to zero
	# for x:
	# (1-s)(ax)(bx) + s(bx)(bx) - cx(bx) - (1-s)(ax)(ax) - s(bx)(ax) + ax(cx) = 0
	# (1-s)(ax)(bx) + s(bx)(bx) - (1-s)(ax)(ax) - s(bx)(ax) = (cx-ax)(bx)
	# FINSIH DERIVATION

	s_min = ((bx-ax)*(cx-ax)+(by-ay)*(cy-ay))/float((bx-ax)**2 + (by-ay)**2)
	min_x = (1-s_min)*ax + s_min*bx
	min_y = (1-s_min)*ay + s_min*by
	min_dist = ((cx-min_x)**2 + (cy-min_y)**2)**(0.5)

	if min_dist <= t:
		return True
	else:
		return False


IMAGE_N = 200
IMAGE = np.zeros((IMAGE_N, IMAGE_N))

draw_bezier((-50, -50), (-15, 10), (10, 20), (50, -10), 1, IMAGE, IMAGE_N)
imgplot = plt.imshow(IMAGE, cmap = cm.Greys_r, interpolation="nearest")
plt.show()

