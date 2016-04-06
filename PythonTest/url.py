
import urllib.request


url = 'http://tieba.baidu.com/p/4143459082'
page = '3'
url_final = url + '/?pn=' + page
print(url_final)

request = urllib.request.Request(url_final)
response = urllib.request.urlopen(request)

result = response.read()
print(result)













