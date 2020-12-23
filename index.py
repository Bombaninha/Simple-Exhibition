import numpy as np

from Image import *
from Webcam import *
from Video import *

from config import *

ex = Image(ASSETS_PATH_IMAGE, "Output")
ex.show()

ex = Video(ASSETS_PATH_VIDEO, "Output")
ex.show()

ex = Webcam("Output", {
  "width": WIDTH_WEBCAM_VALUE,
  "height": HEIGHT_WEBCAM_VALUE,  
  "brightness": BRIGHTNESS_WEBCAM_VALUE    
})
ex.show()
'''
img = cv2.imread("assets/pug.jpg")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgGray)
cv2.imshow("Canny Image", imgGray)
cv2.imshow("Dialation Image", imgGray)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
'''