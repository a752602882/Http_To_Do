from locust import TaskSet, task, HttpLocust


class test_register(TaskSet):
    #任务之间也有权重关系
    @task(1)
    def test_register(self):
        pass
    @task(2)
    def test_getcode(self):
        pass

    '''
    有替代注释器的作用
    test_getcode 执行频率 test_register的两倍
    '''
    tasks = {
        test_register:1,
        test_getcode:2
    }

'''
 蝗虫locust2执行频率是locust1的一倍
'''

class locust1(HttpLocust):
    weight = 1
    task_set = test_register

class locust2(HttpLocust):
    weight = 2
    task_set = test_register

    #locust -f   locust_element/register2.py --host=http://192.168.31.104:1027
    #locust -f locust_element/register2.py UserOne UserTwo