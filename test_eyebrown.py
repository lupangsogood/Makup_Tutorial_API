import cv2
import numpy as np
import dlib
import PIL
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

detector  = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

im_bg = cv2.imread('../FILE_OUTPUT_color_207_40_57.jpg')
im_fg = cv2.imread('eyebrowL.png')


cv2.imshow('Original',img)
cv2.waitKey(0)
## For Specs


imOrg = img.copy()
gray = cv2.cvtColor(imOrg,cv2.COLOR_BGR2GRAY)
rects = detector(gray,1)
for (i,rect) in enumerate(rects):
    shape = predictor(gray,rect)

    #ค่าความกว้างของหน้า และ ความสูงของหน้า
    HALF_FACE_RATIO = (0.695)
    halfFace = shape.part(16).x * HALF_FACE_RATIO
    FACE_HEIGHT_RATIO = (1.0 / 5)
    heightFace = shape.part(8).y * FACE_HEIGHT_RATIO

    #ค่าจุดกลางของหน้าเอาไว้จุดแก้มอีกหนึ่งข้าง
    mid = shape.part(33).x-20
    x = shape.part(17).x
    y = shape.part(19).y-10
    w = shape.part(21).x+10
    h = shape.part(19).y+30
    cv2.rectangle(imOrg,(x,y),(w,h),(255,86,30),3)
