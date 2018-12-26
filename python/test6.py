#coding=utf-8
import pytest

@pytest.fixture(scope='module')
def open():
    print('\n')
    print("打开Baidu浏览器=========》")

'''
2个方法都调用了open,但是调用了一次
在test-s2方法调用之前
'''
def test_s1():
    print("用例 1")

def test_s2(open):
    print("用例 2")

def test_s3(open):
    print("用例 3")


if __name__ == "__main__":
    pytest.main(["-s", "test6.py"])