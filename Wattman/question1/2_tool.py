import json
import os
import cv2
import numpy as np

file_dir = os.getcwd()
file_path = open(file_dir+'/boxes.json')
box = json.load(file_path)
left_top = box['boxes'][1]['rectangle']['left_top']
right_bottom = box['boxes'][1]['rectangle']['right_bottom']
# 计算box_b的宽度和高度
weight = right_bottom[0]-left_top[0]
height = right_bottom[1]-left_top[1]

#读取最开始读入的图片
src = cv2.imread('img_1.png')
#读取待嵌入的图片
img = cv2.imread('img_2.png')
resized_img = cv2.resize(img, (weight, height))

#嵌入图片
if left_top[1] > src.shape[0] | left_top[1]+height > src.shape[0]:
    print("高度超出范围！")
elif left_top[0] > src.shape[1]| left_top[0]+weight > src.shape[1]:
    print("宽度超出范围！")
else:
    src[left_top[1]:left_top[1]+height, left_top[0]:left_top[0]+weight] = resized_img

# cv2.imshow('out.jpg', src)
# cv2.waitKey(0)
cv2.imwrite('out.jpg', src)