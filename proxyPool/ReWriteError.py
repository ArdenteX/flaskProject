class ReWriteSpiderError(Exception):
    def __init__(self, name):
        self.name = name
        Exception.__init__(self)

    def __str__(self):
        return repr(f"this class {self.name} does not has 'gets' method")


class PoolEmptyError(Exception):
    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('The proxy source is exhausted')


class SourceDepletionError(Exception):
    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('The proxies are decreasing but no new proxy be put in pool')

