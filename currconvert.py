import urllib.parse
import requests
import json
access_key = 'ac2821989d38e738232c39faa829e462'
url = 'http://data.fixer.io/api/latest?access_key='
frm = 'AUD'
tok = 'BDT'
amount = '1'
#print(url+access_key+'&from='+frm+'&to='+tok+'&amount='+amount)
query = url+access_key+'&format=1'
response = requests.get(query).json() #resoponse is a dict now
#print(response['rates']['AUD'])
AUD = response['rates']['AUD']
BDT = response['rates']['BDT']
rate = BDT/AUD
print(rate)
#allcur = json.loads(response)
#for key, value in response.items():
#    print(key,value,'\n')
