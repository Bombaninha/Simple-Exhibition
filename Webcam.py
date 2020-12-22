from Exibition import *

from config import *

class Webcam(Exibition):
    def __init__(self, title, configurations):
        self.setTitle(title)
        self.setConfigurations(configurations)
    
    def getConfigurations(self):
        return self.configurations

    def setConfigurations(self, configurations):
        self.configurations = configurations

    def show(self):
        setup = {
            "width": (WIDTH_WEBCAM_ID, WIDTH_WEBCAM_VALUE),
            "height": (HEIGHT_WEBCAM_ID, HEIGHT_WEBCAM_VALUE),
            "brightness": (BRIGHTNESS_WEBCAM_ID, BRIGHTNESS_WEBCAM_VALUE)
        }

        captureVideo = cv2.VideoCapture(DEFAULT_WEBCAM)

        for configuration in self.getConfigurations():
            captureVideo.set(setup[configuration][0], setup[configuration][1])
            captureVideo.set(setup[configuration][0], setup[configuration][1])
            captureVideo.set(setup[configuration][0], setup[configuration][1])

        while True:
            success, image = captureVideo.read()
            cv2.imshow(self.getTitle(), image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break