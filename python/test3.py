#coding=utf-8
import pytest
# 功能函数
def multiply(a,b):
    return a * b

class Test3(object):


    # =====fixtures========
    def setup(self):
        print ("\n")
        print ("setup================>")

    def teardown(self,module):
        print ("teardown=============>")

    def setup_class(self,function):
        print ("setup_class------>")

    def teardown_class(self,function):
        print ("teardown_class--->")

    def set_method(self,method):
        print ("setup_method------>")

    def teardown_method(self, method):
        print ("teardown_method-->>")


    # =====测试用例========
    def test_numbers_3_4(self):
        print ('test_numbers_3_4')
        assert multiply(3,4) == 12


    def test_strings_a_3(self):
        print ('test_strings_a_3')
        assert multiply('a',3) == 'aaa'

if __name__ == '__main__':
        pytest.main(["-s"," test_fixtures.py"])