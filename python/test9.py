#coding=utf-8
import smtplib

import pytest


@pytest.fixture(scope="module")
def smtp():
    with smtplib.SMTP("smtp.gmail.com") as smtp:
        yield smtp # provide the fixture val


'''
 如果第一个用例异常了，不影响其他的用例执行
'''
def test_s1(smtp):
    print("用例 1")
    raise NameError # 模拟异常

def test_s2(smtp):
    print("用例 2")

def test_s3(smtp):
    print("用例 3")


if __name__ == "__main__":
    pytest.main(["-s", "test9.py"])