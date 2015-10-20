# -*- coding: utf-8 -*-

__author__ = 'wb-zhangjinzhong'

from selenium.webdriver.support.ui import WebDriverWait
from  selenium import webdriver
from pyquery import PyQuery  as pq

import urllib2
import re
import os

import codecs

def webGo():
    browser = webdriver.PhantomJS()
    #browser = webdriver.Chrome()

    browser.get("http://jingyan.baidu.com/list/1?type=1&pn=18")
    browser.refresh()
    # browser.save_screenshot("1.jpg")
    # browser.find_element_by_id('kw').send_keys(u'中文')
    # browser.find_element_by_id('su').click()



    # WebDriverWait(browser,10).until(lambda browser:
    #
    #                         browser.find_element_by_class_name('exp-info')
    #
    #                     )

    # browser.save_screenshot("2.jpg")
    # print browser.page_source
    source = browser.page_source

    browser.close()

    return source


def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}

    req = urllib2.Request(url, None, headers)

    response = urllib2.urlopen(req)

    html = response.read()
    return html


def downloadText(url):
    content = getHtml(url)

    text = pq(content)
    text2 = text('#format-exp')
    ft = re.sub('<[^>]+>','',text2.text())

    with open("text/%s.txt" % (text('.exp-title>h1').text()) ,'w') as fp:

         fp.write(ft)




def analyze(content):
    q = pq(content)
    links = q('.exp-link')

    for link in links:

        downloadText( 'http://jingyan.baidu.com' +  pq(link).attr('href'))



analyze(webGo())
# print getHtml('http://jingyan.baidu.com/article/64d05a02620e13de55f73bb6.html')
