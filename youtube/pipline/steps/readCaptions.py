import os
from .steps import Step
from youtube.settings import CAPTIONS_DIR

class ReadCaptions(Step):
    def process(self, inputs, data, utils):
        # 上個步驟的data沒用到，主要是因為這層使用os.listdir讀取檔案(有儲存字幕檔)
        data = {}
        # os.listdir(資料夾) => 從該資料夾內取得所有東西(包含副檔名的檔案)
        for file in os.listdir(CAPTIONS_DIR):
            caption={}
            with open (utils.setCapPath(file.split(".txt")[0]), "r") as f:
                time = ""
                for line in f:
                    # 針對有\n結尾的，利用.strip()清除
                    line = line.strip()
                    if "-->" in line:
                        time = line
                        continue
                    if time:
                        caption[line] = time
                        time = ""
            # 由於是字典型態，就不會按照順序給
            data[file] = caption
        return data