# 数据读取
class DataLoader:

    def __init__(self, path):
        self.path = path


    def load(self):

        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as f:

            text = f.read()


        documents = text.split("\n")

        return documents