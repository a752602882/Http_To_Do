import requests

#data = {
#    "mobile":15208460574,
#    "password":123456,
#    "code":1345
#}

#url='http://39.104.103.201:8080/api/member/register/submit'


# response= requests.post(url,data=data)
# res=response.json()

url = 'http://39.104.103.201:8080/api/common/smsCode'
params ={
    "mobile":"18380253907",
    "type":'register'
}
response= requests.get(url,params=params)
res=response.json()
assert res['status']==True

print(type(response))
print(type(response.text))
print(type(response.json()))
A=response.json()
print(A)
print(A['status'])