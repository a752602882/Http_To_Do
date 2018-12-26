#coding=utf-8
import smtplib

import pytest


@pytest.fixture(scope="module")
def smtp_connection(request):
    smtp_connection=smtplib.SMTP("smtp.gmail.com",578,timeout=5)

    def fin():
        print("teardown smtp_connsmtp_connection.close")
        smtp_connection.close()
        request.addfinalizer(fin)
        return smtp_connection #

'''
     .yield 呾 addfinalizer 方法都是在测试完成后呼叨相应的代码。但
    是 addfinalizer 不同的是：
     他可以注册多个终结函数。
     返些终结方法总是会被执行，无论在乊前的 setup code 有没有
    抛出错误。返个方法对于正确关闭所有的 fixture 创建的资源非常便利，
    即使其一在创建戒获取时失败
'''
def test_s1(smtp_connection):
    print("用例 1")
    raise NameError # 模拟异常

def test_s2(smtp_connection):
    print("用例 2")

def test_s3(smtp_connection):
    print("用例 3")


if __name__ == "__main__":
    pytest.main(["-s", "test10.py"])