# _*_ coding: utf-8
# @Time: 2023/3/28 18:46
# @Author: ljy
# @File: 03 豆瓣
# @project: urlib
import urllib.request
import urllib.parse


def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&'
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=header)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download(page, content):
    with open('download/douban' + str(page) + '.json', 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    startPage = int(input('请输入起始页'))
    endPage = int(input('请输入结束页'))

    for page in range(startPage, endPage + 1):
        request = create_request(page)
        content = get_content(request)
        download(page, content)
