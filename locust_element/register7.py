from locust import TaskSet, task, HttpLocust
'''
 ResponseContextManger使用方法
'''
class test_register(TaskSet):

    @task
    def test_register(self):
        with self.client.get("https://www.baidu.com",catch_response =True) as response:
            if response.status_code ==200:
                response.failure('Failed!')
            else:
                response.success()
    #这里success()和failure(str)的调用会体现在结果的统计上
    #response.failure('Failed!') 失败信息会在【Failures】页面显示出来

class locust1(HttpLocust):



    task_set = test_register
    min_wait = 1000
    max_wait = 1000


    #locust -f   locust_element/register7.py --host=http://192.168.31.104:1027
    #locust -f locust_element/register4.py UserOne UserTwo