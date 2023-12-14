"""
LICENSE:
===============

    Copyright (c) 2018 Marita Fitzgerald and the Creative Science Foundation. All rights reserved.

    Based on;
    https://github.com/lzane/Fingers-Detection-using-OpenCV-and-Python
    http://creat-tabu.blogspot.com/2013/08/opencv-python-hand-gesture-recognition.html
    https://github.com/mahaveerverma/hand-gesture-recognition-opencv
    https://github.com/Sadaival/Hand-Gestures

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    DEPENDENCIES:
    ===============
    install using pip commands:
    pip install opencv-python
    pip install numpy

    INSTRUCTIONS
    ============
    1. Run the program and ensure your hand is not in the blue capture area
    2. Press "b" to capture the background
    3. Put your hand in the blue capture area and press "t" to gain gesture capture
    4. To reset the background, remove your hand from the blue capture area and press "r"
    5. To exit press "Esc"

    NOTES
    =====
    Please note, works best with a high contrast background

"""

import cv2
import numpy as np
import copy
import sys
from codeepy import CodeePy

# parameters
cap_region_x_begin = 0.5  # start point/total width
cap_region_y_end = 0.8  # start point/total width
threshold = 60  # BINARY threshold
blurValue = 41  # GaussianBlur parameter
bgSubThreshold = 50
learningRate = 0

# variables
isBgCaptured = 0  # bool, whether the background captured
triggerSwitch = False  # if true, keyboard simulator works


def get_com_port():
    return 'COM12'


def print_threshold(thr):
    print("! Changed threshold to " + str(thr))


def remove_bg(frame):
    fgmask = bgModel.apply(frame, learningRate=learningRate)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res


# Camera
camera = cv2.VideoCapture(0)
camera.set(10, 200)
cv2.namedWindow('trackbar')
cv2.createTrackbar('trh1', 'trackbar', threshold, 100, print_threshold)

# Codee
codee = CodeePy(get_com_port())

while camera.isOpened():
    ret, frame = camera.read()
    threshold = cv2.getTrackbarPos('trh1', 'trackbar')
    frame = cv2.bilateralFilter(frame, 5, 50, 100)  # smoothing filter
    frame = cv2.flip(frame, 1)  # flip the frame horizontally
    cv2.rectangle(frame, (int(cap_region_x_begin * frame.shape[1]), 0),
                  (frame.shape[1], int(cap_region_y_end * frame.shape[0])), (255, 0, 0), 2)
    cv2.imshow('original', frame)

    #  Main operation
    if isBgCaptured == 1:  # this part wont run until background captured
        img = remove_bg(frame)
        img = img[0:int(cap_region_y_end * frame.shape[0]),
              int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]  # clip the ROI
        cv2.imshow('mask', img)

        # convert the image into binary image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (blurValue, blurValue), 0)
        cv2.imshow('blur', blur)
        ret, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)
        cv2.imshow('ori', thresh)

        # get the contours
        thresh1 = copy.deepcopy(thresh)
        contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        length = len(contours)
        maxArea = -1
        if length > 0:
            for i in range(length):  # find the biggest contour (according to area)
                temp = contours[i]
                area = cv2.contourArea(temp)
                if area > maxArea:
                    maxArea = area
                    ci = i

            res = contours[ci]
            # make a convex hull around the hand (red line)
            hull = cv2.convexHull(res)
            drawing = np.zeros(img.shape, np.uint8)
            cv2.drawContours(drawing, [res], 0, (0, 255, 0), 2)
            cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3)

            if triggerSwitch is True:
                # define area of hull and area of hand
                areahull = cv2.contourArea(hull)
                areacnt = cv2.contourArea(res)
                # find the percentage of area not covered by hand in convex hull
                arearatio = ((areahull - areacnt) / areacnt) * 100
                print(arearatio)
                if arearatio < 11:
                    print("rock")
                    codee.display_image("rock")
                elif  arearatio < 25:
                    print("paper")
                    codee.display_image("paper")
                else:
                    print("scissors")
                    codee.display_image("sissors")
        cv2.imshow('output', drawing)

    # Keyboard OP
    k = cv2.waitKey(10)
    if k == 27:  # press ESC to exit
        cv2.destroyAllWindows()
        for i in range(1, 5):
            cv2.waitKey(1)
        sys.exit()
    elif k == ord('b'):  # press 'b' to capture the background
        bgModel = cv2.createBackgroundSubtractorMOG2(0, bgSubThreshold)
        isBgCaptured = 1
        print('!!!Background Captured!!!')
    elif k == ord('r'):  # press 'r' to reset the background
        bgModel = None
        triggerSwitch = False
        isBgCaptured = 0
        print('!!!Reset BackGround!!!')
    elif k == ord('t'):  # press 't' to trigger gesture capture
        triggerSwitch = True
        print('!!!Trigger On!!!')
