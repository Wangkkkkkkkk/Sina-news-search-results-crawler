import requests
from bs4 import BeautifulSoup
from openpyxl import workbook  # 写入Excel表所用

# 搜索界面页数表
list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
        '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
        '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
        '51', '52', '53', '54', '55', '56', '57', '58', '59', '60',
        '61', '62', '63', '64', '65', '66', '67', '68', '69', '70',
        '71', '72', '73', '74', '75', '76', '77', '78', '79', '80',
        '81', '82', '83', '84', '85', '86', '87', '88', '89', '90',
        '91', '92', '93', '94', '95', '96', '97', '98', '99', '100',
        ]

f = workbook.Workbook()
ws = f.active  # 获取当前正在操作的表对象
ws.append(['时间', '标题'])

for x in list:
    # 输入网址必须是末尾为页数
    res = requests.get('https://search.sina.com.cn/?q=%e5%bf%ab%e6%89%8b&c=news&from=world&col=&range=all&source=&country=&size=10&stime=&etime=&time=&dpc=0&a=&ps=0&pf=0&page=' + x) # 模拟get 请求获取链接返回的内容
    res.encoding = 'utf-8' # 设置编码格式为utf-8
    soup = BeautifulSoup(res.text, 'html.parser') # 前面已经介绍将html文档格式化为一个树形结构，每个节点都是一个对python对象，方便获取节点内容
    for new in soup.select('.box-result'): # BeautifulSoup提供的方法通过select选择想要的html节点类名，标签等，获取到的内容会被放到列表中
        if len(new.select('h2')) > 0:
            # 加[0]是因为select获取内容后是放在list列表中[内容,],text可以获取标签中的内容
            print(new.select('.fgray_time')[0].text+' '+new.select('h2')[0].text+' '+new.select('a')[0]['href'])
            ws.append([new.select('.fgray_time')[0].text, new.select('h2')[0].text])
f.save('qinshi.xlsx')  # 存入所有信息后，保存为filename.xlsx
