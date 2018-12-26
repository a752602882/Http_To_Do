
class Test1():




    def func(self,x):
     return  x+1

    def test_answer(self):
        assert self.func(3)==5

    def test1(self):
        assert  1==1

    @classmethod
    def setup_class(cls):
        print("setup_class：每个类开始前都会执行")

    @classmethod
    def teardown_class(cls):
        print("teardown_class：每个类结束后都会执行")
