import bs4
import requests

url = 'https://api.afl.com.au/statspro/playersStats/rounds/CD_R202101419'#?teamId=CD_T30,CD_T100'

h = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'x-media-mis-token': '2762ff8803aee902a0be72daba182566'
     }

r = requests.get(url, headers=h, verify=False)
print(r.text)