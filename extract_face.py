#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: face_extract.py

API_KEY = '40482f8f45dfdcd870057b331b140c78'
API_SECRET = 'w8pay74xRG0yuVeSxUSov4c6d_csH5JB'

from facepp import API, File
api = API(API_KEY, API_SECRET)

from print_assist import print_result
from covex_hull import covex_hull
from cut_img import cut_and_save
import time
import sys

time1 = time.time()

def get_face_id(detection):
    return detection['face'][0]['face_id']

def get_size(detection):
    return detection['img_width'], detection['img_height']

def get_landmark(landmark_result):
    return landmark_result['result'][0]['landmark']

class Point:
    def __init__(self, x, y, angle=0.0):
        self.x = x
        self.y = y
        self.angle = angle
    def __repr__(self):
        return "<Point:(%f, %f), Angle: %f>" % (self.x, self.y, self.angle)

def get_points_stack(landmarks):
    global width, height
    stack = []
    for p in landmarks.values():
        x = p['x'] * width / 100
        y = p['y'] * height / 100
        stack.append(Point(x, y))
    return stack

img_path = sys.argv[1]
#detection = api.detection.detect(url='http://www.huabian.com/uploadfile/2014/0821/20140821092236949.jpg')
detection = api.detection.detect(img = File(img_path))
face_id = get_face_id(detection)
width, height = get_size(detection)
landmark_result = api.detection.landmark(face_id=face_id)
landmarks = get_landmark(landmark_result)

# Debug
print_result('anglebaby', detection)
print '------------------------------'
print_result('landmarks', landmarks)

points_stack = get_points_stack(landmarks)
print_result('points of landmarks', points_stack)

edge_points = covex_hull(points_stack)
print_result('edge points', edge_points)

cut_and_save(img_path, edge_points)

print 'Used time :', time.time() - time1
