# -*- coding: utf-8 -*-
# $File: covex_hull.py

import math
from print_assist import print_result

def is_turn_left(p1, p2, p3):
    x1, y1 = p2.x - p1.x, p2.y - p1.y
    x2, y2 = p3.x - p2.x, p3.y - p2.y
    return x1*y2 - x2*y1 > 0

def line(lined_points, other_points):
   # print_result('lined points', lined_points)
    if len(other_points) == 0:
        #print_result('After return: lined points', lined_points)
        return lined_points
    else:
        if is_turn_left(lined_points[-2], lined_points[-1], other_points[0]):
            lined_points.append(other_points.pop(0))
            return line(lined_points, other_points)
        else:
            lined_points.pop()
            if len(lined_points) == 1:
                lined_points.append(other_points.pop(0))
                return line(lined_points, other_points)
            else:
                return line(lined_points, other_points)


def get_bottom_point(points):
    bottom_point = points[0]
    for p in points:
        if p.y < bottom_point.y:
            bottom_point = p
    return bottom_point

def get_edge_points(points):
    edge_points = []
    for i in range(2): # append first two points
        edge_points.append(points.pop(0))

    edge_points = line(edge_points, points)

    return edge_points

def covex_hull(points_stack):
    bottom_point = get_bottom_point(points_stack)
    print bottom_point
    for p in points_stack:
        angle = math.atan2(p.y - bottom_point.y, p.x - bottom_point.x)
        p.angle = angle
    sorted_points = sorted(points_stack, key=lambda x: x.angle)
    return get_edge_points(sorted_points)
