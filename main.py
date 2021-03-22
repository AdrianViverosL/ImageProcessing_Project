import cv2, os
import numpy as np
import imutils

os.system('clear')

#img = cv2.imread('image.jpeg')
#cv2.imshow('image', img)
def region_of_interest(frame):
    try:
        height, width= frame.shape
    except ValueError:
        height, width= frame.shape[:-1]

    mask = np.zeros_like(frame)
    #Cover not desired area
    polygon = np.array([[(0, height * 1/3), (width, height * 1/3),
                        (width, height),(0,height),]], np.int32)
    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(frame, mask)
    return masked_image

cap = cv2.VideoCapture('/Users/adsvl/Downloads/IMG_3646.mp4')

#Check if file was opened successfully
if(cap.isOpened() == False):
    print('Error opening video footage')

while(cap.isOpened()):
    #Get frame by frame of the Video
    ret, frame = cap.read()

    #Resize the frame
    frame = imutils.resize(frame, width=480)
    
    #Converting to Gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Converting to HSV space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Region of intenrest
    roi_frame = region_of_interest(hsv)
    if ret == True:
        #cv2.imshow('Frame', frame)
        #cv2.imshow('gray', gray)
        #cv2.imshow('HSV Space', hsv)
        cv2.imshow('ROI', roi_frame)

        #Press Q on Keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release() #Once the video frames have ended, close the video
#cv2.waitKey(0)
cv2.destroyAllWindows() #Destroy all the windows


