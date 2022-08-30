from pytube import YouTube

from .steps import Step

class GetCaptions(Step):
    def process(self, inputs, data, utils):
        # 使用for loop 接住 generator取出的東西
        # 在前一步驟已經定義該取得多少筆資料，這裡就不用重新再寫i = 0 & i += 1
        for item in data:
            url = f"https://www.youtube.com/watch?v={item}"
            if utils.checkFileExists(url):
                print(f'{item}.txt file exists.')
                continue
            try:
                source = YouTube(url)
                # 第一種方式要改原始碼 https://github.com/pytube/pytube/issues/1085
                caption = source.captions[inputs["lang"]].generate_srt_captions()

                # 第二種方式則不用改，但是xml標記型態
                # caption = source.captions[inputs["lang"]].xml_captions
            except KeyError:
                print(f'{item} has no subtiles')
                continue

            with open(utils.setCapPath(url), "w", encoding="utf-8") as f:
                f.write(caption)

        #這一份檔案僅處理取得字幕並儲存，下一個步驟要讀取每個檔案內的字幕，因此先回傳原url，方便提供檔案名字去找尋 
        # 在此沒用到，直接用字幕資料夾內的檔案讀取並寫入新的dictionary => os.listdir(資料夾)
        # 但之後的步驟仍為用到，因此繼續回傳
        return data;