from pytube import YouTube
# 李永樂
url = "https://www.youtube.com/watch?v=x_pq4Dzj97o"
# # 英文
# url = "https://www.youtube.com/watch?v=vfBz6t5CcrE"
source = YouTube(url)
# caption codes format is something like this ['en', 'ar', 'fr']
# caption = source.captions['zh-Hant'].generate_srt_captions()
caption = source.captions['zh-Hant'].xml_captions
print(caption)


