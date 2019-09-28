import requests
import re

def getHTMLText(url):
    """提取页面HTML代码，并返回HTML文本"""
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("页面提取错误")
        return ""

def parsePage(infoList, html):
    """解析页面，将[价格，名字] 存入列表"""
    try:
        #分析网页源码解析出价格
        price = re.findall(r'\"view_price\":\"\d+\.\d+?"',html)
        title = re.findall(r'\"raw_title\":\".+?\"',html)
        #test this re
        #print(price)
        #print(title)
        for i in range(len(price)):
            _price = eval(price[i].split(':')[1])
            _title = eval(title[i].split(':')[1])
            infoList.append([_price, _title])
    except:
        print('页面解析错误')

def printGoodsList(infoList):
    """将解析好的商品页面打印出来"""
    tplt = '{:^4}\t{:^6}\t{:^10}'
    print(tplt.format("数量","价格", "名字"))
    count = 0
    for goods in infoList:
        count+=1
        print(tplt.format(count,goods[0], goods[1]))        

def main():
    keyword = "电脑"
    deep = 1 #页数
    url = 'https://s.taobao.com/search?q=' + keyword
    infoList = []
    for i in range(deep):
        _url = url + '&s=' + str(i*44)
        text = getHTMLText(_url)
        parsePage(infoList, text)
        printGoodsList(infoList)

main()
 
