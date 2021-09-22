import cv2
import numpy
img = cv2.imread("image.png")
print(img.shape)
cv2.imshow("anh truoc",img)
cv2.waitKey()

#cat goc phan tu trai tren cua anh

imgcrop = img[0:272, 0:320]
cv2.imshow("anh sau cat",imgcrop)
cv2.waitKey()

#resize anh: dai, rong con 1/2

resize = cv2.resize(img,(272,320))
cv2.imshow("resized",resize)
cv2.waitKey()

#gaussian blur anh

gb = cv2.GaussianBlur(img,ksize = (5,5), sigmaX = 0)

cv2.imshow("Gaussian Smoothing",numpy.hstack((img, gb)))
cv2.waitKey()


#tim edge anh

	#convert thanh anh xam
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#timgoc
edges = cv2.Canny(gray_image, threshold1 = 100, threshold2 = 200)
cv2.imshow("edge",edges)
cv2.waitKey()

