import requests
from lxml import etree
import re
import pickle

url = 'http://www.360doc.com/content/09/0830/21/145264_5413512.shtml'
response = requests.get(url)

html = etree.HTML(response.text)
areaList = html.xpath('//*[@id="artContent"]/div[2]/text()')
areaStr = "".join(areaList)
p = re.compile(r'(\d*?)\s')
result = re.findall(p,areaStr)
print(result[:20])
with open('firstSixNumber.db','wb') as f:
    pickle.dump(result,f)

