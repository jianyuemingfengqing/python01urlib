# _*_ coding: utf-8
# @Time: 2023/3/28 16:02
# @Author: ljy
# @File: 02 百度翻译
# @project: urlib

import urllib.request
import urllib.parse

# 接口
# url = 'https://fanyi.baidu.com/sug'# 普通翻译
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'  # 详细翻译
# 反爬虫
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
    'Cookie': ' BIDUPSID=CAFD62FF86598D7E9B0352AA06D9E908; PSTM=1679574647; BD_UPN=12314753; BAIDUID=DCE015904BA8F4D142187D3888449619:FG=1; BDUSS=WM5YUMzY2xlLU1-MUlMdkNwVmgwYWVnRUF2dVh6Z0pLLUNiYXNqVkV1bkl1VVJrRVFBQUFBJCQAAAAAAAAAAAEAAAAZJok-18-zx8Sn0~IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMgsHWTILB1kS; BDUSS_BFESS=WM5YUMzY2xlLU1-MUlMdkNwVmgwYWVnRUF2dVh6Z0pLLUNiYXNqVkV1bkl1VVJrRVFBQUFBJCQAAAAAAAAAAAEAAAAZJok-18-zx8Sn0~IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMgsHWTILB1kS; ab_sr=1.0.1_MWFjYzg2MGZhOGU2MWZlMjQyOTYzZDE1OTVmZmNkOTM5NThmNWFiOTE4YjkxNWI4MWYwZjhhYzIwZTI3M2VmMzYwM2I3NmUyOGVlMGUwMDMwNWUwOTJiM2UwODY5YmMwNzYyMjAzMzRiODAyYjk3MmQ3YzBmMTkxYjkzYTdkYjc4YTU0ZTFhZjEwNjAyNzU3OTkwMmFhMTQxMDE1MGVjNzdkYzM0OGExZmI5MzhjNWVlNmFlMDU5MjQxOTUzZmM1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=DCE015904BA8F4D142187D3888449619:FG=1; BA_HECTOR=8l2g8k8h2h200g048kaha1a61i1uegk1m; ZFY=08Il4jXY4YzylNIygwI:B9ra77rfpe:AyP975jeMEb:BlE:C; B64_BOT=1; delPer=0; BD_CK_SAM=1; PSINO=1; H_PS_PSSID=38185_36542_38412_38106_38348_38438_38398_37862_38468_38172_38289_38236_36803_37938_38383_38040_26350_22160_38281_37881; sugstore=1; H_PS_645EC=9487f8CJogpAp9yPfWxHpmMNqdGdWPpveeDtydOxv%2FWHG8dMIWYLSEKHQMI; baikeVisitId=d14bd979-ce8d-47d4-b484-fd076cab67d6'
}
# 请求参数
# data = {
#     'kw' : 'dog'
# }
data = {
    'rom': 'en',
    'to': 'zh',
    'query': 'dog',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '871501.634748',
    'token': '088fd0facd7867b97d1d1488ac685404',
    'domain': 'common'
}
#   编码
data = urllib.parse.urlencode(data).encode('utf-8')
# 请求
request = urllib.request.Request(url, data, headers)
# 发送并接收
response = urllib.request.urlopen(request)
# 读取数据
content = response.read().decode('utf-8')
# print(content)
import json

obj = json.loads(content)  # 转为json数据
print(obj)
