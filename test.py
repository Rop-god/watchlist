import requests
import json



resp=requests.get('http://127.0.0.1:5000/login',params={'username':'admin','password':'<PASSWORD>'})
print(resp.content)