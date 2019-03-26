def test_closure(k: int, b: int):
    def mk_closure(x: int):
        print(k * x + b)

    return mk_closure


closure_1 = test_closure(1, 2)
closure_1(0)
closure_1(1)
closure_1(2)

closure_2 = test_closure(11,22)
closure_2(0)
closure_2(1)
closure_2(2)
