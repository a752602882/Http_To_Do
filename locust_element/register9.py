from locust import TaskSet, task, HttpLocust
from locust.clients import HttpSession

'''
Locust会自动跟踪HTTP请求的状态并统计，如果不想使用默认的安全形式，可以配合with语句及catch_response参数捕捉原始响应。
可以使用name参数对不同URL的请求进行分类。
第一个参数不再是完整的URL，比如请求http://www.baidu.com/，只需要提供参数/即可，http://www.baidu.com是通过Locust类的host特性提供的，或者通过locust命令行的-H参数提供。
'''


class test_register(TaskSet):

    @task(1)
    def test_A(self):
        s = HttpSession('http://www.baidu.com')
        with s.get('/', catch_response = True, name = "test1") as res:
            if res.status_code ==200:
                print(res.status_code)
                res.failure('Failed!')
            else:
                res.success()
    @task(2)
    def test_B(self):
        s = HttpSession('http://www.baidu.com')
        with s.get('/', catch_response = True, name = "test2") as res:
            if res.status_code ==200:
                print(res.status_code)
                res.failure('Failed!')
            else:
                res.success()


    @task(1)
    def test_C(self):
        s = HttpSession('http://www.baidu.com')
        with s.get('/', catch_response = True, name = "test2") as res:
            if res.status_code ==200:
                res.failure('HiHi Failed!')
            else:
                res.success()


class WebsiteUser(HttpLocust):
        '''
        Locust实例被挑选执行的权重，数值越大，执行频率越
        weight = 1
       '''
        task_set = test_register
        min_wait = 5000
        max_wait = 9000


        #locust -f   locust_element/register9.py --host=http://192.168.31.104:1027