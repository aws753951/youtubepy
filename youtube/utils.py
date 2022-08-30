import os
from .settings import DOWNLOAD_DIR
from .settings import VIDEOS_DIR
from .settings import CAPTIONS_DIR

class Utils:
    # 沒有要使用self
    @staticmethod
    def getID(url):
        return url.split("watch?v=")[-1]

    # 使用到getID的func，得用self了
    def setPath(self, url):
        return os.path.join(CAPTIONS_DIR, self.getID(url)+".txt")
