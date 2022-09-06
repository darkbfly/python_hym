import requests

url = 'https://springboot-weather-push-gftlgclvaw.cn-hangzhou.fcapp.run/History'
test = requests.get(url=url)
print(test.text)