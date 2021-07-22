import xlwt
import re

data = input("请输入原字符串（无标点符号，阿拉伯数字及英文)")
number = 0
dataSet = set()
dataList = []
work_book = xlwt.Workbook(encoding='utf-8')                          # 新建工作簿
sheet = work_book.add_sheet(sheetname='Sheet1')                      # 新建工作表

for i in data:
    dataSet.add(i)                                                   # 将输入字符串单个添加到集合去重
for i in dataSet:
    dataList.append(i)                                               # 将集合转换为列表
for i in range(len(dataList)):
    sheet.write(i,1,dataList[i])                                     # 写入 excel
work_book.save('活 字 印 刷.xls')                                    # 保存文件（注意：此处不可保存为 xlsx 文件）