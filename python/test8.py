#coding=utf-8
import pytest

@pytest.fixture()
def open():
    print('\n')
    print("执行setup的方法=========》")

    ## yield相当于唤醒tearDown操作
    yield
    print("执行 teardown!")
    print("最后关闭浏览器")


'''
 如果第一个用例异常了，不影响其他的用例执行
'''
def test_s1(open):
    print("用例 1")
    raise NameError # 模拟异常

def test_s2(open):
    print("用例 2")

def test_s3(open):
    print("用例 3")


if __name__ == "__main__":
    pytest.main(["-s", "test8.py"])