class TestDecorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("这里是类的call方法")
        return self.func()


@TestDecorator  # get_str() = TestDecorator(get_char)
def get_str():
    return "haha"


print(get_str())
