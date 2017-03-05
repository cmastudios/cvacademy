import cv2

def imshow(name, image):
	cv2.imwrite(name + "_imshow.png", image)