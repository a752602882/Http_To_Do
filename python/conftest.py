import  pytest
# 不带参数时默认 scope="function"
@pytest.fixture()
def login():
    print('\n')
    print("输入账号，密码先登录")