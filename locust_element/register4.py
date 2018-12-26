from locust import TaskSet, task, HttpLocust
'''
 权重复杂嵌套
'''
class test_register(TaskSet):
    #任务之间也有权重关系
    @task(1)
    def test_register(self):
        pass
    @task(2)
    def test_getcode(self):
        pass

    @task(2)
    class A(TaskSet):
         @task(4)
         def A_M1(self):
             pass
         @task(3)
         def A_M2(self):
             # interrupt 有跳出A_M2方法，执行其他方法，要不让此线程会一直执行A_M1 和A_M2
             self.interrupt()
    @task(1)
    def logOut(self):
        pass

class locust1(HttpLocust):
    task_set = test_register

    #locust -f   locust_element/register4.py --host=http://192.168.31.104:1027
    #locust -f locust_element/register4.py UserOne UserTwo