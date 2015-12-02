import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm

import midpoint as line_drawing


def intersection_of_edge_with_scanline(scanline_y, edge):
	# line parameterized by
	# P(s) = start + (finish-start)*s    for s = [0, 1]
	# set y_intersect = scanline_y
	#
	# scanline_y = start_y + (finish_y-start_y)*s
	# s_intersect = (scanline_y - start_y)/(finish_y - start_y)
	(start_x, start_y) = edge[0]
	(end_x, end_y) = edge[1]
	if float(end_y-start_y) == 0:
		print 'setting to none'
		return None
	else:
		s_intersect = (scanline_y - start_y)/float(end_y-start_y)
		return s_intersect


def intersection_point_of_edge_with_scanline(scanline_y, edge):
	(start_x, start_y) = edge[0]
	(end_x, endy_y) = edge[1]
	s = intersection_of_edge_with_scanline(scanline_y, edge)
	return (start_x + (end_x-start_x)*s, start_y + (end_y-start_y)*s)



def scanline_polygon(edge_list, img, img_n):
	### THIS IS just to gaurantee that the start points have lower y
	for i in range(0, len(edge_list)):
		if edge_list[i][0][1] > edge_list[i][1][1]:
			edge_list[i] = (edge_list[i][1], edge_list[i][0])

	# sort the edge list by lowest y value
	edge_list.sort(key = lambda row: row[0][1])
	scanline_y = round(edge_list[0][0][1])

	# active edge list
	active_edge_list = []

	# go through each edge in the list
	for edge in edge_list:
		s = intersection_of_edge_with_scanline(scanline_y, edge)
		# if it intersects the scan line
		if 0 <= s <= 1:
			active_edge_list.append(edge)

	# now go over all the scan lines we need to
	max_y = max(edge_list, key = lambda elt: elt[1][1])[1][1]
	for scanline_y in range(int(edge_list[0][0][1]), max_y):
		# now go through the active edge lists
		intersection_points = []
		for active_edge in active_edge_list:
			s = intersection_of_edge_with_scanline(scanline_y, active_edge)
			# if edge is horizontal than just ignore it
			if s is None:
				continue
			(start_x, start_y) = active_edge[0]
			(end_x, end_y) = active_edge[1]
			intersection_pt = (start_x + (end_x-start_x)*s, start_y + (end_y-start_y)*s)
			intersection_points.append(intersection_pt)
		# sort the intersection points by lowest x value
		intersection_points.sort(key = lambda elt: elt[0])

		# now fill between pairs
		for i in range(0, len(intersection_points), 2):
			start = intersection_points[i]
			end = intersection_points[i+1]
			for x in range(int(start[0]), int(end[0])):
				img[img_n/2-scanline_y][x+img_n/2] = 1

		# move to the next scan line
		scanline_y = scanline_y + 1
		# add the necessary edges
		active_edge_list = []
		for edge in edge_list:
			# add if the starting y is before scanline_y
			# and if ending y is after scanline_y
			if edge[0][1] <= scanline_y and edge[1][1] > scanline_y:
				active_edge_list.append(edge)


	return edge_list

IMAGE_N = 200
IMAGE = np.zeros((IMAGE_N, IMAGE_N))



edges = [[(-50, -30),(0, 50)], [(0,50), (50, -30)], [(-50, -30),(0,10)], [(0,10), (50, -30)]]
# each edge is represented by a pair of endpoints

scanline_polygon(edges, IMAGE, IMAGE_N)

imgplot = plt.imshow(IMAGE, cmap = cm.Greys_r, interpolation="nearest")
plt.show()
