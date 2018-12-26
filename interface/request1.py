import requests

json={
    "page": 1,
    "limit": 50
}
head = {
    'Authorization':'eyJhbGciOiJIUzUxMiJ9.eyJjcmVhdGVfdGltZSI6MTU0MzMwNDY2NTk4OCwidXNlcl9pZCI6IjEiLCJleHAiOjE1NDMzOTEwNjUsImF1dGhvcml0aWVzIjpbXSwidXNlcm5hbWUiOiJhZG1pbiJ9.t-XxIkgfKneikiR7xklJaOXB4vTLqX5I9DcEj6E9gVOM6F1Verz4pLAFbGOPz5apMskohaWI3h9xuPtyBsNIYQ',
    'Content-Type':'application/json'
}
response=requests.post(url='http://192.168.31.104:1027/core/wellrecords/list',headers=head,json=json)
print(type(response))
print(type(response.text))
print(type(response.json()))
A=response.json()
print(A)
print(A['status'])