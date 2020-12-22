from Exibition import *

class Video(Exibition):
    def __init__(self, path, title):
        self.setPath(path)
        self.setTitle(title)

    def show(self):
        captureVideo = cv2.VideoCapture(self.getPath())
        
        while True:
            success, image = captureVideo.read()
            cv2.imshow(self.title, image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break