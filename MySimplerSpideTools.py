# coding=utf-8
__author__ = 'wb-zhangjinzhong'

import urllib
import urllib2

from pyquery import PyQuery  as pq

import os
import os.path


def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}

    req = urllib2.Request(url, None, headers)

    response = urllib2.urlopen(req)

    html = response.read()
    return html


def analyzeAndDownloadImg(content, path):
    baseUrl = 'http://fc.gamehome.tv/fc'

    t = pq(content)

    imgs = t('table[cellpadding="4"]').find('a')

    i = 0
    for item in imgs:
        href = pq(item).attr('href')

        href = href[1:]

        urllib.urlretrieve(baseUrl + href, path + '/%d.jpg' % i)
        i += 1


if __name__ == '__main__':
    # print getHtml('http://fc.gamehome.tv/fc/index.asp?page=1').decode('gbk')


    mainUrl = 'http://fc.gamehome.tv/fc/index.asp?page=%d'

    for i in range(1, 19):

        pathName = 'imgs/%d' % i

        if not os.path.exists(pathName):
            os.mkdir(pathName)

        content = getHtml(mainUrl % i)

        analyzeAndDownloadImg(content.decode('gbk'), pathName)




# getHtml("http://jingyan.baidu.com/list/11").decode('utf-8')

# a = u'中文'
#
# print a
