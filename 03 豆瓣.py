# _*_ coding: utf-8
# @Time: 2023/3/28 18:46
# @Author: ljy
# @File: 03 豆瓣
# @project: urlib
import urllib.request
import urllib.parse



url = 'https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&start=0&limit=20'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=header)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

with open('download/douban.json', 'w', encoding='utf-8') as file:
    file.write(content)
