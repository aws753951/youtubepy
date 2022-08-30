from pytube import YouTube

from .steps import Step

class GetCaptions(Step):
    def process(self, inputs, data, utils):
        i = 0
        # 使用for loop 接住 generator取出的東西
        for item in data:
            if i == inputs["counts"]:
                break
            i += 1
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