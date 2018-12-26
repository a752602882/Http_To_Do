import json

from locust import HttpLocust, TaskSet, task
#测试百斯特数据
class test_url(TaskSet):

    #Authorization是不断变化的，注意查询
    @task()
    def test_reigster(self):
        json={
            "page": 1,
            "limit": 50
        }

        head = {
            'Authorization':'eyJhbGciOiJIUzUxMiJ9.eyJjcmVhdGVfdGltZSI6MTU0MzMwNDY2NTk4OCwidXNlcl9pZCI6IjEiLCJleHAiOjE1NDMzOTEwNjUsImF1dGhvcml0aWVzIjpbXSwidXNlcm5hbWUiOiJhZG1pbiJ9.t-XxIkgfKneikiR7xklJaOXB4vTLqX5I9DcEj6E9gVOM6F1Verz4pLAFbGOPz5apMskohaWI3h9xuPtyBsNIYQ',
            'Content-Type':'application/json'
        }
        url ='/core/wellrecords/list'
        response= self.client.post(url,headers=head,json=json)
        res=response.json()
        assert res['status']==True



class WebsiteUser(HttpLocust):
    task_set = test_url
    min_wait = 5000
    max_wait = 9000


    #locust -f   locust_element/http1_locust.py --host=http://192.168.31.104:1027