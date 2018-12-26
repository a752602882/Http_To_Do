from locust import TaskSet, task, HttpLocust
'''
 权重复杂嵌套
'''
class test_register(TaskSet):


    def test_register(self):
        pass

    def test_getcode(self):
        pass


    class A(TaskSet):

         def A_M1(self):
             pass

         def A_M2(self):
             # interrupt 有跳出A_M2方法，执行其他方法，要不让此线程会一直执行A_M1 和A_M2
             self.interrupt()

         tasks = {
             A_M1:1,
             A_M2:2
         }

    def logOut(self):
        pass

    tasks = {
        test_register:1,
        test_getcode:2,
        A:3
    }

class locust1(HttpLocust):

    task_set = test_register

    #locust -f   locust_element/register4.py --host=http://192.168.31.104:1027
    #locust -f locust_element/register4.py UserOne UserTwo