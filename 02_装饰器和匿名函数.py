def set_func1(func):
    print("decorator--1")

    def call_func1():
        print("-------------Here is inside call func1-----------")
        func()

    return call_func1


def set_func2(func):
    print("decorator--2")

    def call_func2():
        print("-------------Here is inside call func2-----------")
        func()

    return call_func2


@set_func2
@set_func1
def test():
    print("----------1-----------")


test()
print("+" * 20)
