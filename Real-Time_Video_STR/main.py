import easyocr
import matplotlib.pyplot as plt
import cv2
import time
import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFont
import pyttsx3

reader= easyocr.Reader(['en'], gpu=True) #specifies reading in english, and reads on GPU for speed
vid= cv2.VideoCapture(0) #captures the video, 0 indicates it's a webcam feed
skip_frame = True #frame skipping to ensure OCR doesn't hold back detector

#Text to speech
audio = pyttsx3.init()
audio.setProperty('rate', 150)
audio.setProperty('volume', 0.9)

while(True):
    a= time.time()
    ret, img= vid.read()

    gray= cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #converts image to grayscale
    result= reader.readtext(gray)
    text= ""

    for res in result:
        text+= res[1] + " "
    cv2.putText(img, text, (50,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2) #puts the text predicted on screen in specific coordinates and colour


    ##FFPS
    b= time.time() #end time
    fps= 1/(b-a) #how long does it take to process image
    cv2.line(img, (20,25), (127,25), [85,45,225], 30) #draws image

    for (bbox, tx, prob) in result:
        # unpack the bounding box
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))
        cv2.rectangle(img, tl, br, (0, 255, 0), 3) #draws bounding box
        cv2.putText(img, f'FPS: {int(fps)}', (11,35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, lineType=cv2.LINE_AA)
        cv2.imshow("result", img)




    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    print(fps)
    print(text)
    audio.say(text)
    audio.runAndWait()





