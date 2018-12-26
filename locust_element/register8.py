from locust import TaskSet, task, HttpLocust

'''
 参数化统计【Failures】页面
'''
class test_register(TaskSet):

    @task
    def test_register(self):
       '''
       消息统计合并
       '''
       #  name参数对不同URL的请求进行分类。在图表中进行区分
       self.client.get('https://www.baidu.com/id=2012',name = "test")
       self.client.get('https://www.baidu.com/id=2013',name = "test1")
       self.client.get('https://www.baidu.com/id=2014',name = "test")
       self.client.get('https://www.baidu.com/id=2015',name = "test1")


class locust1(HttpLocust):



    task_set = test_register


    #locust -f   locust_element/register8.py --host=http://192.168.31.104:1027
    #locust -f locust_element/register4.py UserOne UserTwo