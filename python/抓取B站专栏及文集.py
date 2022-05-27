import requests
from bs4 import BeautifulSoup

# 专栏这种格式太多了，用 markdown 保存对于字体大小无法修改，用 bs4 还会莫名其妙把注释漏掉，麻了。
# 也许我还不如用正则表达式处理字符串。
# 目前能将正文的 html 单独丢进 markdown 文件。

# r = requests.get('https://www.bilibili.com/read/cv11636153')
with open(r'E:\Develop\project\gitcode\zero6six\Zero6sixStudies\python\temp\temp.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')
    head = '# ' + soup.find(class_="inner-title").string + '\n'
    text = soup.find(id="read-article-holder")
    
    textList = []   
    file2 = open(r'E:\Develop\project\gitcode\zero6six\Zero6sixStudies\python\temp\temp.md', 'w+', encoding='utf-8')
    file2.write(head)
    for i in text.find_all('p'):
        file2.write(str(i))
        file2.write("\n")
    file2.close
