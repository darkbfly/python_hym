import requests

url = 'https://springboot-weather-push-gftlgclvaw.cn-hangzhou.fcapp.run/test?userId=oU7jH5v0vVeCcM_8heBzvGDKfq7Y'
test = requests.get(url=url)
print(test.text)