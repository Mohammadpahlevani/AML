# import library
import numpy as np
import os
import cv2
from skimage.metrics import structural_similarity as ssim

# load picture & convert it to grayscale
folder = "C:\\Desktop\\Face_Recognition\\pictures"
pictures = [cv2.cvtColor(cv2.imread(os.path.join(folder, name)), cv2.COLOR_BGR2GRAY) for name in os.listdir(folder)]

# threshold
ssim_thr = 0.75

# capture picture
cap_pic = cv2.VideoCapture(0)
img, pic = cap_pic.read()
gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

# calculate SSIM
s_list = []
for pict in pictures:
    ssim_m = ssim(gray, pict)
    s_list.append(ssim_m)

# check SSIM threshold
if any(ssim_li > ssim_thr for ssim_li in s_list):
    print("Hello")
else:
    print("Can't login")
    
# release & destroy
cap_pic.release()
cv2.destroyAllWindows()