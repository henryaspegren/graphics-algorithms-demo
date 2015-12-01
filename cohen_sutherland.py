import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm

import midpoint as line_drawing


# xl = left x coordinate of rectangle
# xr = right x coordinate of rectangle
# yt = top y coordinate of rectange
# yb = bottom y coordinate of rectange
def cohen_sutherland(xl, xr, yt, yb, start_pt, end_pt, img, img_n):
	(sx, sy) = start_pt
	(ex, ey) = end_pt
	m = (ey-sy)/float(ex-sx)
	# Q1 = ABCD
	q_start = (sx < xl, sx > xr, sy < yb, sy > yt)
	# Q2 = ABCD
	q_end = (ex < xl, ex > xr, ey < yb, ey > yt)
	if (not q_start[0] and not q_start[1] and not q_start[2] and not q_start[3]) and  \
		(not q_end[0] and not q_end[1] and not q_end[2] and not q_end[3]):
		# accept
		line_drawing.midpoint_line_drawing(sx, sy, ex, ey, img, img_n)
	elif (q_start[0] and q_end[0]) or (q_start[1] and q_end[1]) or (q_start[2] and q_end[2]) or \
		(q_start[3] and q_end[3]):
		# reject
		return None
	### CASES
	# START POINT
	elif q_start[0]:
		# clip against left boundary
		sx_new = xl
		sy_new = sy + (sx_new-sx)*m
		return cohen_sutherland(xl, xr, yt, yb, (sx_new, sy_new), end_pt, img, img_n)
	elif q_start[1]:
		# clip against right boundary
		sx_new = xr
		sy_new = sy + (sx_new-sx)*m
		return cohen_sutherland(xl, xr, yt, yb, (sx_new, sy_new), end_pt, img, img_n)
	elif q_start[2]:
		# clip against bottom boundary
		sy_new = yb
		sx_new = sx + (1/m)*(sy_new-sy)
		return cohen_sutherland(xl, xr, yt, yb, (sx_new, sy_new), end_pt, img, img_n)
	elif q_start[3]:
		# clip aggainst top boundary
		sy_new = yt
		sx_new = sx + (1/m)*(sy_new-sy)
		return cohen_sutherland(xl, xr, yt, yb, (sx_new, sy_new), end_pt, img, img_n)
	# END POINT
	elif q_end[0]:
		# clip against left boundary
		ex_new = xl
		ey_new = ey + (ex_new-ex)*m
		return cohen_sutherland(xl, xr, yt, yb, start_pt, (ex_new, ey_new), img, img_n)
	elif q_end[1]:
		# clip against right boundary
		ex_new = xr
		ey_new = ey + (ex_new-ex)*m
		return cohen_sutherland(xl, xr, yt, yb, start_pt, (ex_new, ey_new), img, img_n)
	elif q_end[2]:
		# clip against bottom boundary
		ey_new = yb
		ex_new = ex + (1/m)*(ey_new-ey)
		return cohen_sutherland(xl, xr, yt, yb, start_pt, (ex_new, ey_new), img, img_n)
	elif q_end[3]:
		# clip aggainst top boundary
		ey_new = yt
		ex_new = ex + (1/m)*(ey_new-ey)
		return cohen_sutherland(xl, xr, yt, yb, start_pt, (ex_new, ey_new), img, img_n)
	else:
		raise 'Error'

IMAGE_N = 200
IMAGE = np.zeros((IMAGE_N, IMAGE_N))

cohen_sutherland(-25, 25, 25, -25, (-50, -90), (90, 90), IMAGE, IMAGE_N)
line_drawing.midpoint_line_drawing(-25, -25, 25.1, -25.1, IMAGE, IMAGE_N)
line_drawing.midpoint_line_drawing(-25, 25, -24.95, -25, IMAGE, IMAGE_N)
line_drawing.midpoint_line_drawing(25, 25, -25, 25,IMAGE,IMAGE_N)
line_drawing.midpoint_line_drawing(25, 25, 25.05, -25.05, IMAGE,IMAGE_N)

imgplot = plt.imshow(IMAGE, cmap = cm.Greys_r, interpolation="nearest")
plt.show()




