class Msg:
    def __init__(self, title, message="Empty Message", content={}):
        self.title = title
        self.message = message
        self.content = content

    def __str__(self):
        return "{}\n{}\nContent: {}".format(self.title, self.message, self.content)
