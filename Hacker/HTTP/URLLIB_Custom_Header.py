#!/usr/bin/python3.4
# -*- coding=utf-8 -*-
#本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
#教主QQ:605658506
#亁颐堂官网www.qytang.com
#乾颐盾是由亁颐堂现任明教教主开发的综合性安全课程
#包括传统网络安全（防火墙，IPS...）与Python语言和黑客渗透课程！
import sys
sys.path.append('/usr/local/lib/python3.4/dist-packages/PyQYT/ExtentionPackages')
sys.path.append('/usr/lib/python3.4/site-packages/PyQYT/ExtentionPackages')
sys.path.append('../../ExtentionPackages')

import urllib.request
from bs4 import BeautifulSoup

def qyt_browser_proxy(url, proxy):
	ProxyHandlered= urllib.request.ProxyHandler(proxy)
	opener = urllib.request.build_opener(ProxyHandlered)
	urllib.request.install_opener(opener)
	urlContent = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(urlContent, "html.parser")
	print(soup)

if __name__ == '__main__':
	#Proxy网址
	proxy = {'http': '120.198.244.29:8080'}
	url = 'http://www.qytang.com/'
	qyt_browser_proxy(url, proxy)
