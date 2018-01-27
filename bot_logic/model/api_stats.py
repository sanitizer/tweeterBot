class Stats:

    def __init__(self):
        self.limit = -1
        self.remaining = -1

    def __str__(self):
        return "limit: {} remaining: {}".format(self.limit, self.remaining)
