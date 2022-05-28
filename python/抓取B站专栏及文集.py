import requests
import re
from lxml import etree
import os
import time

# 该脚本可将 b 站专栏转为 txt
# 测试网页使用 https://www.bilibili.com/read/cv11636153 文本格式过多，无法完美转换，仍存在问题
# 使用过程中疑似出现漏字和漏篇，可能需要对是否成功爬取做判断/延时调整

def getArticleUrls(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    html = etree.HTML(r.text)
    scripts = html.xpath('//script/text()')[0]
    pattern = r"articlelistIds += +\[(\d*,)*\d*]"
    match = re.search(pattern, scripts)
    urlLists = match.group().split()[-1].strip('[]').split(',')
    frontUrl = 'https://www.bilibili.com/read/cv'
    for i in range(len(urlLists)):
        urlLists[i] = frontUrl + urlLists[i]
    return urlLists

def downloadArticle(url):
    if wait:
        time.sleep(0.5)
    r = requests.get(url)
    r.encoding = 'utf-8'
    html = etree.HTML(r.text)
    head = html.xpath('//p[@class="inner-title"]/text()')[0]
    articleHolder = html.xpath('//div[@id="read-article-holder"]')[0]
    paragraphs = articleHolder.xpath('p|blockquote')
    outputPara = []
    for i in paragraphs:
        if i.tag == 'p':
            para = i.xpath('string()').strip()
            outputPara.append(para)
        if i.tag == 'blockquote':
            for n in i.iterfind('p'):
                para = n.xpath('string()').strip()
                outputPara.append(para)

    with open(r'C:\Users\zero6six\desktop\download.txt', 'a',encoding='utf-8') as file:
        file.write(head+'\n')
        for i in outputPara:
            file.write(i+'\n')
        file.write('\n'*2)

while True:
    print('该脚本用于抓取 B 站专栏及文集( txt 格式)\n'
    '请注意：下载后的文档需及时改名，否则之后下载的会在原文档末尾追加！\n'
    '[0]退出 [1]专栏 [2]文集')
    choice = input('您的选择是 ')
    if choice == '0':
        break
    elif choice == '1':
        downloadArticle(input('请输入链接 '))
    elif choice == '2':
        wait = True
        urls = getArticleUrls(input('请输入链接 '))
        for i in range(len(urls)):
            downloadArticle(urls[i])
            if i == 0:
                print('时间较长，请耐心等待！')
            print('已完成 '+str(i+1)+"/"+str(len(urls)))
    os.system('cls')