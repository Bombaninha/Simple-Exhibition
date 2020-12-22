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