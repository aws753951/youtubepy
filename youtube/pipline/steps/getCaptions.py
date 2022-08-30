from pytube import YouTube

from .steps import Step

class GetCaptions(Step):
    def process(self, inputs, data, utils):
        i = 0
        for item in data:
            i+=1
            if i == inputs["counts"]:
                break
            try:
                url = f"https://www.youtube.com/watch?v={item}"
                source = YouTube(url)
                # caption codes format is something like this ['en', 'ar', 'fr']
                # 第一種方式要改原始碼 https://github.com/pytube/pytube/issues/1085
                caption = source.captions[inputs["lang"]].generate_srt_captions()

                # 第二種方式則不用改，但是xml標記型態
                # caption = source.captions[inputs["lang"]].xml_captions



            except KeyError:
                print(f'{item} has no subtiles')
                continue

            #saving the the captions to a flat file
            with open(utils.setPath(url), "w", encoding="utf-8") as f:
                f.write(caption)