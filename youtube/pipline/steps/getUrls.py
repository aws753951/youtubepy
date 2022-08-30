import scrapetube
from .steps import Step


class GetUrls(Step):
    
    def process(self, inputs, data, utils):
        videos = scrapetube.get_channel(inputs["channelID"])
        lists = []
        i = 0
        for video in videos:
            i+=1
            if i == inputs["counts"]:
                break
            lists.append(video['videoId'])
        return lists