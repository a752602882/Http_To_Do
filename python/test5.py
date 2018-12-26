#coding=utf-8
import pytest




def test_s1(login):
    print("用例 1：登录之后其它动作 111")

def test_s2():
    print("用例 2：不传login")
    assert  2==3

def test_s3(login):
    print("用例 3：登录之后其它动作 333")
    assert  3==3

if __name__ == "__main__":
    #pytest.main(["-s", "testfix.py"])
    pytest.main("pytest -s -q --alluredir report")
