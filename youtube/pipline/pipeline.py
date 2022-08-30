class Pipeline:

    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        # 一開始建立資料夾時初始data
        data = None
        for step in self.steps:
            data = step.process(inputs, data, utils)