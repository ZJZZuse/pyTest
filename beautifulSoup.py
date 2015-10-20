#encoding=utf-8

__author__ = 'wb-zhangjinzhong'

from bs4 import BeautifulSoup

import MySimplerSpideTools as tools

soup = BeautifulSoup(tools.getHtml("http://www.ygdy8.net/html/gndy/dyzz/list_23_142.html"))

itemAll = soup.find('div',class_="co_content8")

itemAll = soup.find('div',class_="co_content8")