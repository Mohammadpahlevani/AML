# import library
import cv2

# capture picture
cap_pic = cv2.VideoCapture(0)

# display & save picture
for count in range(1, 61):
    img, pic = cap_pic.read()
    if img:
        cv2.imshow('Taking picture', pic)
        name = f"pictures/pic{count}.jpg"
        cv2.imwrite(name, pic)

    # Add a small delay between capturing frames
    cv2.waitKey(100)

# release & destroy
cap_pic.release()
cv2.destroyAllWindows()