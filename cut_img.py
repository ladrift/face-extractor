# -*- coding: utf-8 -*-
# $File: face_extract.py

import cv2
import numpy as np
def edge_space(points):
    x1, y1 = points[0].x, points[0].y
    x2, y2 = 0, 0
    for p in points:
        if p.x < x1:
            x1 = p.x
        if p.x > x2:
            x2 = p.x
        if p.y < y1:
            y1 = p.y
        if p.y > y2:
            y2 = p.y

    return x1, x2, y1, y2

def is_on_right(phead, ptail, x, y):
    x1, y1 = phead.x - ptail.x, phead.y - ptail.y
    x2, y2 = x - phead.x, y - phead.y
    return x1*y2 - x2*y1 < 0

def block_out(img, edge_points):
    height, width, channels = img.shape
    points_num = len(edge_points)
    for i in xrange(points_num):
        ptail = edge_points[i]
        if i < points_num - 1:
            phead = edge_points[i+1]
        else:
            phead = edge_points[0]
        cv2.line(img, (int(ptail.x), int(ptail.y)), (int(phead.x), int(phead.y)), (0,0,255), 5)
        cv2.line(img, (int(ptail.x), int(ptail.y)), (int(ptail.x), int(ptail.y)), (255,0,0), 5)
        cv2.line(img, (int(phead.x), int(phead.y)), (int(phead.x), int(phead.y)), (0,255,0), 5)
        for x in xrange(width):
            for y in xrange(height):
                if is_on_right(phead, ptail, x, y):
                    # set pixel to be transparent
                    img.itemset((y, x, 3), 0)
                    #img.itemset((y, x, 2), 255)
        #cv2.imshow('abc', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
    return img


def cut_and_save(img_path, edge_points):
    img = cv2.imread(img_path, -1)
    img_alpha = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    img_alpha = block_out(img_alpha, edge_points)
    left, right, bottom, top= edge_space(edge_points)
    print left, right, bottom, top
    face_square = img_alpha[bottom:top, left:right]
    cv2.imwrite(img_path.split('.')[0] + 'face.png', face_square)
#    cv2.imshow('abc', img_alpha)
#    cv2.imwrite('wtf_edge_line.png', img_alpha)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
