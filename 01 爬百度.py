import urllib.request
import urllib.parse
import json

url = 'http://www.baidu.com'
# response = urllib.request.urlopen(url)
#
# content = response.read().decode('utf-8')

# print((content))
# print(response.getheaders())
# 下网页
# urllib.request.urlretrieve(url,'baidu.html')

# 下图片
# imgUrl = 'https://t7.baidu.com/it/u=1297102096,3476971300&fm=193&f=GIF'
# urllib.request.urlretrieve(imgUrl, '渐变.jpg')

# 下视频
# videoUrl = 'https://vd2.bdstatic.com/mda-pca8susmh9ir5bdd/sc/cae_h264/1678515479752627543/mda-pca8susmh9ir5bdd.mp4'
# urllib.request.urlretrieve(videoUrl, '视频.mp4')
path = '/s?wd='
# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
# name = '%E5%91%A8%E6%9D%B0%E4%BC%A6'
name = urllib.parse.quote('周杰伦')

# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
    'Cookie': ' BIDUPSID=CAFD62FF86598D7E9B0352AA06D9E908; PSTM=1679574647; BD_UPN=12314753; BAIDUID=DCE015904BA8F4D142187D3888449619:FG=1; BDUSS=WM5YUMzY2xlLU1-MUlMdkNwVmgwYWVnRUF2dVh6Z0pLLUNiYXNqVkV1bkl1VVJrRVFBQUFBJCQAAAAAAAAAAAEAAAAZJok-18-zx8Sn0~IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMgsHWTILB1kS; BDUSS_BFESS=WM5YUMzY2xlLU1-MUlMdkNwVmgwYWVnRUF2dVh6Z0pLLUNiYXNqVkV1bkl1VVJrRVFBQUFBJCQAAAAAAAAAAAEAAAAZJok-18-zx8Sn0~IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMgsHWTILB1kS; ab_sr=1.0.1_MWFjYzg2MGZhOGU2MWZlMjQyOTYzZDE1OTVmZmNkOTM5NThmNWFiOTE4YjkxNWI4MWYwZjhhYzIwZTI3M2VmMzYwM2I3NmUyOGVlMGUwMDMwNWUwOTJiM2UwODY5YmMwNzYyMjAzMzRiODAyYjk3MmQ3YzBmMTkxYjkzYTdkYjc4YTU0ZTFhZjEwNjAyNzU3OTkwMmFhMTQxMDE1MGVjNzdkYzM0OGExZmI5MzhjNWVlNmFlMDU5MjQxOTUzZmM1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=DCE015904BA8F4D142187D3888449619:FG=1; BA_HECTOR=8l2g8k8h2h200g048kaha1a61i1uegk1m; ZFY=08Il4jXY4YzylNIygwI:B9ra77rfpe:AyP975jeMEb:BlE:C; B64_BOT=1; delPer=0; BD_CK_SAM=1; PSINO=1; H_PS_PSSID=38185_36542_38412_38106_38348_38438_38398_37862_38468_38172_38289_38236_36803_37938_38383_38040_26350_22160_38281_37881; sugstore=1; H_PS_645EC=9487f8CJogpAp9yPfWxHpmMNqdGdWPpveeDtydOxv%2FWHG8dMIWYLSEKHQMI; baikeVisitId=d14bd979-ce8d-47d4-b484-fd076cab67d6'
}

request = urllib.request.Request(url=url + path + name, headers=headers)  # 转换

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

print(content)

# urllib.request.urlretrieve(url=(url + path + name), filename='error.html')
