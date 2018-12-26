#coding=utf-8
import pytest


# 不带参数时默认 scope="function"
@pytest.fixture()
def login():
    print('\n')
    print("输入账号，密码先登录")

def test_s1(login):
    print("用例 1：登录之后其它动作 111")

def test_s2():
    print("用例 2：不传login")

def test_s3(login):
    print("用例 3：登录之后其它动作 333")


if __name__ == "__main__":
    pytest.main(["-s", "testfix.py"])