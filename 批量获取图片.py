import requests

def getPhoto(url,name):
    import os.path
    text = requests.get(url).content
    path1 = r"C:\Users\zero6six\Desktop\picture"
    path2 = name + ".jpg"
    path = os.path.join(path1,path2)
    with open(path,"wb") as file:
        file.write(text)

urls = ["test.com"]

for i in range(len(urls)):
    getPhoto(urls[i],str(i))