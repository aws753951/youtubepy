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
    # 取得字幕檔的位置
    def setCapPath(self, url):
        return os.path.join(CAPTIONS_DIR, self.getID(url)+".txt")

    # 檢查是否存在字幕黨
    def checkFileExists(self, url):
        path = self.setCapPath(url)
        # 位元運算(bitwise operator)的 &，另一種為邏輯運算(logical operator)的 and
        # os.path.getsize(檔案位置)，辨別是否容量大小大於0
        return os.path.exists(path) and os.path.getsize(path) > 0

    # 取得url list檔的位置(存在download根目錄)
    # 有需要更改該檔案，再去setting新增檔案名並import進來
    @staticmethod
    def setUrlPath(channelID):
        return os.path.join(DOWNLOAD_DIR, channelID+".txt")

    