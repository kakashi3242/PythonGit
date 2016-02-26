import demjson
from builtins import print

json = '{"weatherinfo":{"city":"北京","cityid":"101010100","temp":"10","WD":"东南风","WS":"2级","SD":"26%","WSE":"2","time":"10:25","isRadar":"1","Radar":"JC_RADAR_AZ9010_JB","njd":"暂无实况","qy":"1012"}}'

text = demjson.decode(json)
print(text)



