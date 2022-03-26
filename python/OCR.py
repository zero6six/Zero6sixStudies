import requests
import json
import base64
import os
from PIL import ImageGrab
from io import BytesIO

'''
通用文字识别（高精度版）
https://ai.baidu.com/ai-doc/OCR/1k3h7y3db
'''
getAccessToken = False #是否重新获取 Access Token



# 刷新 Access Token(一个 token 有效期 30 天)
if getAccessToken:
    with open(r"gitcode\zero6six\Zero6sixStudies\python\temp\OCRAPI.json", "r") as file:
        jsonSet = json.load(file)
        API_key = jsonSet["API_key"]
        secret_key = jsonSet["secret_key"]
    
    host = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + API_key + "&client_secret=" + secret_key        
    response = requests.get(host)
    if response:
        access_token = response.json()["access_token"]
        jsonSet["access_token"] = access_token
        jsonData = json.dumps(jsonSet)
        with open(r"gitcode\zero6six\Zero6sixStudies\python\temp\OCRAPI.json", "w+") as file:
            file.write(jsonData)

# 获取 Access Token
with open(r"gitcode\zero6six\Zero6sixStudies\python\temp\OCRAPI.json", "r") as file:
    jsonSet = json.load(file)
    access_token = jsonSet["access_token"]

# 调用 Snipaste 截图到剪贴板
os.system("D:\Snipaste-1.16.2-x64\Snipaste.exe snip -o clipboard")
input("输入任意以继续")
os.system("cls")                       # 清屏

# 将剪贴板图像 base64 编码
bytesIO = BytesIO()                    # 初始化
ImageGrab.grabclipboard().save(bytesIO, format="png")
img = base64.b64encode(bytesIO.getvalue())

# 拼接请求网址
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
params = {"image":img}
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}

# 发送请求
response = requests.post(request_url, data=params, headers=headers)
if response:
    jsonSet = response.json()
    for i in jsonSet.items():
        print(i)