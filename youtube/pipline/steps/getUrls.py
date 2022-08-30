import scrapetube
from .steps import Step


class GetUrls(Step):
    
    def process(self, inputs, data, utils):
        videos = scrapetube.get_channel(inputs["channelID"])
        i = 0
        for video in videos:
            if i == inputs["counts"]:
                break
            i += 1
            # generator ，等等下個程式要接的時候記得用for loop取出
            yield video['videoId']

            if inputs["downloadUrl"]:
                self.writeUrlToFile(video, utils.setUrlPath(inputs["channelID"]))

    @staticmethod
    def writeUrlToFile(video, filePath):
        # 使用"a"讓寫入"同個"檔案時不覆蓋
        # 寫入檔案要跨行，記得加"\n"
        with open (filePath, "a", encoding="utf-8") as f:
            f.write(video['videoId'] + "\n")
