def set_para(num: int):
    def set_fun(func):
        def call_func(*args, **kwargs):
            print("here is inside of the decorator")
            if num < 10:
                print("Free version")
            elif num >= 10:
                print("Advanced version")
            else:
                print("you should not have seen this, something must be wrong!")
            return func()

        return call_func

    return set_fun


@set_para(100)
def test1():
    print("test 1")
    return "ok from test1"


@set_para(5)
def test2():
    print("test 2")
    return "ok from test2"


test1()

test2()
