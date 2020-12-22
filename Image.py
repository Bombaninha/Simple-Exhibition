from Exibition import *

class Image(Exibition):
    def __init__(self, path, title):
        self.setPath(path)
        self.setTitle(title)

    def show(self):
        image = cv2.imread(self.getPath())
        cv2.imshow(self.getTitle(), image)
        cv2.waitKey(0)