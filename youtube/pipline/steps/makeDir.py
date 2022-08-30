import os
from .steps import Step
from youtube.settings import DOWNLOAD_DIR
from youtube.settings import VIDEOS_DIR
from youtube.settings import CAPTIONS_DIR


class MakeDir(Step):
    def process(self, inputs, data, utils):
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)