from locust import TaskSet, task, HttpLocust
'''
 权重复杂嵌套
'''
class test_register(TaskSet):


    # locust = [locust1]指向每个TaskSet所属的loucst用户实例
    # parent = 指向每个TaskSet所属的父类TaskSet，用在TaskSet有嵌套的情况，如果调用parent的TaskSet是最顶层的，则返回它所属的locust用户实例。

    # interrupt()   顶层的TaskSet（即被绑定到某个Locust类的task_set的第一层TaskSet）不能调用这个方法。reschedule置为True时，
    # 从被嵌套任务出来马上选择新任务执行，如果置为False，从被嵌套任务出来后，随机等待min_wait和max_wait之间的一段时间，再选择新任务执行。

    '''
    schedule_task(task_callable, args=None, kwargs=None, first=False)
    将一个可调用的对象task_callable添加进Locust对象（注意是针对某个Locust实例，而不是所有的Locust实例）的任务选择队列，
    其中args和kwargs是传递给可调用对象的参数，如果first置为True，则将其加到队首。
    '''

    def test_register(self):
        pass

    def test_getcode(self):
        pass


class locust1(HttpLocust):

    #client =指向TaskSet所属的父HttpLocust类的client属性，self.client与self.locust.client效果是一样的。如果TaskSet所属的父类是个Locust类，则没有这个client属性


    task_set = test_register


    #locust -f   locust_element/register4.py --host=http://192.168.31.104:1027
    #locust -f locust_element/register4.py UserOne UserTwo