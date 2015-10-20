# -*-encoding:utf-8-*-

from sqlobject import *
import MySimplerSpideTools as tools

import re

__author__ = 'wb-zhangjinzhong'

uri = r'sqlite:data/test.db'
sqlhub.processConnection = connectionForURI(uri)


class User(SQLObject):
    name = StringCol(length=10, notNone=True)
    email = StringCol(length=20, notNone=True)
    password = StringCol(length=20, notNone=True)


class Film(SQLObject):
    name = StringCol()
    time = DateCol()
    otherTinyInfo = StringCol()
    intro = StringCol()
    downloadUrl = StringCol()
    clickCount = IntCol()


# Film.dropTable()
# Film.createTable()

# print tools.getHtml('http://www.ygdy8.net/html/gndy/dyzz/index.html').decode('gbk')

def saveAndAnalyzeDate(content):

    baseUrl = 'http://www.ygdy8.net'

    pq = tools.pq

    t = tools.pq(content)

    items = t('.co_content8 tbody')

    for item in items:
        itemP =  pq(item)

        text =itemP.find('a').attr('href').decode('gbk')
        url = itemP.find('font[color="#8F8C89"]').text()






# def saveSingle(url, clickCount):



def downloadMain():
    baseUrl = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_%d.html'

    pattern = re.compile(r'</a>>')

    for i in range(1, 144):
        content = tools.getHtml(baseUrl % i)

        # t = content.replace('</a>>','</a>')

        # saveAndAnalyzeDate(t)



if __name__ == '__main__' :

    downloadMain()

    # Film.dropTable()
    # Film.createTable()

    # print tools.getHtml('http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html')


