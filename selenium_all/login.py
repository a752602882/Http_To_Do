from  selenium import  webdriver
from selenium_all.common.base import Base
import pytest


loc1 =('id','account')
loc2 =('name','password')
loc3 =('xpath','//*[@id="submit"]')
loc4 =('classname','user-name')


class Test_Login(object):

    driver = webdriver.Chrome()
    zen = Base(driver)
    url ='http://120.79.63.137:9000/zentao/user-login.html'

    login_user= ()


    def setup(self):
        self.driver.get(self.url)

    def teardown(self):
        print('清空cookies ,退出登录状态')
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def teardown_class(self):
        print('用例完成后退出,关闭浏览器')
        self.driver.quit()

    def test_login_1(self):
        self.zen.sendKeys(loc1,'fengli')
        self.zen.sendKeys(loc2,'5423110')
        self.zen.click(loc3)
        result = self.zen.get_text(loc4)
        print('登录结果，获取到登录名：%s'%result)
        assert  result =='冯力'

    def test_login_2(self):
        self.zen.sendKeys(loc1,'admin')
        self.zen.sendKeys(loc2,'111')
        self.zen.click(loc3)
        result = self.zen.get_text(loc4)
        print('登录结果，获取到登录名：%s'%result)
        assert  result =='冯力'


if __name__ == '__main__':
    pytest.main(['-v','login.py'])