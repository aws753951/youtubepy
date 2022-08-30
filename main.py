from youtube.pipline.steps.getCaptions import GetCaptions
from youtube.pipline.steps.makeDir import MakeDir
from youtube.pipline.pipeline import Pipeline
from youtube.pipline.steps.getUrls import GetUrls
from youtube.utils import Utils

# 李永樂
# CHANNELID = "UCSs4A6HYKmHA2MG_0z-F0xw"
# 英文頻道
CHANNELID = "UCYvCbycHNeNiVOSvPhRy9lQ"



def main():
    inputs = {
        "channelID": CHANNELID,
        # 若是要中文，去captions調成xml標記型態
        "lang": "a.en",
        # 取前幾部就好
        "counts": 5,
        "downloadUrl": True,
    }

    steps = [
        MakeDir(),
        GetUrls(),
        GetCaptions(),
    ]

    utils = Utils()
    piInstance = Pipeline(steps)
    # utils作為helper func
    # 在每一次執行run時(for loop中的 process)，可用可不用，但不適合放入inputs內
    # 傳入的為實例，之後可以直接拿裡面的method運行
    piInstance.run(inputs, utils)


# 檢查是不是程式進入點，如是，該檔案身上的__name__屬性就會變成__main__
if __name__ == "__main__":
    main()


