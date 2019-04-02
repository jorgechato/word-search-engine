class Search:
    found = False
    count = 0

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def set_count(self, c):
        self.count = c
        self.found = True if self.count > 0 else False
