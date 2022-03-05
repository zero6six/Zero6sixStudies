def translate(inputText):
    '''功能：利用百度翻译 API 对输入的字符串进行英译中并返回'''
    import hashlib
    import random
    import requests
    import time

    with open(r"gitcode\zero6six\Zero6sixStudies\temp\myAPI.txt","r") as file:
        readText = file.readlines()
        
        appid = str.strip(readText[0][6:])
        key = str.strip(readText[1][4:])

    if inputText.count("&") != 0:                          # 判断字符串中是否含有"&"
        inputTextList = inputText.split("&")               # 对字符串进行分割
        query = " and ".join(inputTextList)                # 对字符串进行合并
    else:
        query = inputText
   
    salt = str(random.randint(0,100))                      # 生成salt

    beforeEncode = appid + query + salt + key              # 对字符串进行拼接
    afterEncode = beforeEncode.encode()                    # 对拼接后字符串进行 utf-8 解码
    sign = hashlib.md5(afterEncode).hexdigest()            # 计算字符串的 md5 值

    requestURL = "https://fanyi-api.baidu.com/api/trans/vip/translate?q=" + query + "&from=en&to=zh&appid=" + appid + "&salt=" + salt + "&sign=" + sign # 拼接请求的 URL
    response = requests.get(requestURL).text               # 获取返回的包含 json 的字符串
    dstText = response.split('"dst":"')[1]
    utf8 = dstText[:len(dstText)-4]                        # 截取翻译后结果的 utf-8 字符串
    text = utf8.encode('utf-8').decode('unicode_escape')   # 转换为中文
    time.sleep(1)
    return(text)