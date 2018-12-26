from locust import TaskSet, task, HttpLocust


class test_register(TaskSet):




    #Authorization是不断变化的，注意查询

    def test_register(self):


        data = {
            "mobile":15208460574,
            "password":123456,
            "code":1345
        }

        url='http://39.104.103.201:8080/api/member/register/submit'


        response= self.client.post(url,data=data)
        res=response.json()
        assert res['status']==False

    def test_getcode(self):
        url = 'http://39.104.103.201:8080/api/common/smsCode'
        params ={
            "mobile":"18380253907",
            "type":'register'
        }

        response= self.client.get(url,params=params)
        res=response.json()
        assert res['status']==True

    '''
    有替代注释器的作用
    test_getcode 执行频率 test_register的两倍
    '''
    tasks = {
        test_register:1,
        test_getcode:2
    }



class WebsiteUser(HttpLocust):
        '''
        Locust实例被挑选执行的权重，数值越大，执行频率越
        weight = 1
       '''
        task_set = test_register
        min_wait = 5000
        max_wait = 9000


        #locust -f   locust_element/register1.py --host=http://192.168.31.104:1027