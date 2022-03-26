import requests
import json
import base64

'''
通用文字识别（高精度版）
https://ai.baidu.com/ai-doc/OCR/1k3h7y3db
将桌面上的 OCR.png 文字识别并 Print
'''
getAccessToken = False #是否重新获取 Access Token

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



# 二进制方式打开图片文件
with open(r"C:\Users\zero6six\Desktop\OCR.png", "rb") as file:
    img = base64.b64encode(file.read())
with open(r"gitcode\zero6six\Zero6sixStudies\python\temp\OCRAPI.json", "r") as file:
    jsonSet = json.load(file)
    access_token = jsonSet["access_token"]

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
params = {"image":img}
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.post(request_url, data=params, headers=headers)
if response:
    jsonSet = response.json()
    for i in jsonSet.items():
        print(i)