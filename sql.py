import pyodbc as p
import datetime
import time
import re #RegEx library
import threading
from time import ctime
 
 
import requests
from bs4 import BeautifulSoup



def getPM25(piao):
    hea = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}


    site = 'http://data.eastmoney.com/DataCenter_V3/gdzjc.ashx?pagesize=50&page=1&js=var%20OeCpDACK&param=&sortRule=-1&sortType=BDJZ&tabid=all&code='+piao+'&name=&rt=51444269'
      

    response  = requests.get(site)
    html = response.text
    
   # html ='''["600830,香溢融通,5.30,0.00,浙江香溢控股有限公司,增持,201.04,0.44,二级市场,6235.3727,13.72,6235.3727,13.72,2018-10-19,2018-10-19,2018-10-20,0.4424","600830,香溢融通,5.30,0.00,浙江香溢控股有限公司,增持,234.6427,0.52,二级市场,6034.3327,13.28,6034.3327,13.28,2018-10-18,2018-10-18,2018-10-19,0.5164","600830,香溢融通,5.30,0.00,浙江香溢控股有限公司,增持,796.85,1.75,二级市场,5799.69,12.77,5799.69,12.77,2018-10-17,2018-10-17,2018-10-18,1.7545","600830,香溢融通,5.30,0.00,浙江香溢控股有限公司,增持,502.84,1.11,二级市场,5002.84,11.01,5002.84,11.01,2018-10-15,2018-10-16,2018-10-17,1.1066","600830,香溢融通,5.30,0.00,中天发展控股集团有限公司,减持,20,0.04,二级市场,2268.1625,4.99,2268.1625,4.99,2016-10-19,2016-10-19,2016-10-20,0.044","600830,香溢融通,5.30,0.00,中天发展控股集团有限公司,增持,1.2,0,二级市场,2288.1625,5.04,2288.1625,5.04,2014-12-22,2014-12-22,2014-12-23,0.0026","600830,香溢融通,5.30,0.00,中天发展控股集团有限公司,减持,350.6066,0.77,二级市场,2288.1625,5.04,2288.1625,5.04,2014-12-22,2014-12-22,2014-12-23,0.7723","600830,香溢融通,5.30,0.00,中天发展控股集团有限公司,减持,6,0.01,二级市场,2637.5691,5.81,2637.5691,5.81,2014-12-18,2014-12-18,2014-12-20,0.0132","600830,香溢融通,5.30,0.00,中天发展控股集团有限公司,减持,75,0.17,二级市场,2643.5691,5.82,2643.5691,5.82,2014-11-25,2014-11-25,2014-12-20,0.1651","600830,香溢融通,5.30,0.00,中天发展控股集团有限公司,减持,1910,4.2,二级市场,2718.5691,5.98,2718.5691,5.98,2013-10-14,2013-10-14,2013-10-16,4.2014","600830,香溢融通,5.30,0.00,中天发展控股集团有限公司,减持,281.6066,0.62,二级市场,4628.5691,10.19,4628.5691,10.19,2013-09-24,2013-09-24,2013-10-16,0.62"]'''
   # print( response.text )
    return response.text




server = 'IT1705\SQLEXPRESS'
database = '2019'
table = 'StockList'
Col1 = 'SCODE'
Col2 = 'SNAME'
Col3 = 'SP1'

connStr = ( r'DRIVER={SQL Server};SERVER=' +
            server + ';DATABASE=' + database + ';' +
            'Trusted_Connection=yes'    )
conn = p.connect(connStr)
 
sql = ('select ' + Col1 + ',' + Col2 + ' as memo ' + ',' + Col3 +
       ' from '+ table
         ) 
dbCursor = conn.cursor()
dbCursor.execute(sql)

now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


for row in dbCursor.fetchall():
   # print (row[0])
    SCODE = row[0]
    Datatext = getPM25(SCODE)
    insertsql =  "insert into DataHistory (SCODE,SyncDatetime,DataText) values ("+"'"+ row[0].strip() +"'"+","+"'"+ now_time +"'"+",'"+Datatext+"')" 
    #print (insertsql)
    dbCursor = conn.cursor()
    
        
    try:
        dbCursor.execute(insertsql)    
        dbCursor.commit()
    except:
        dbCursor.rollback()
        
    #finally:
        #conn.close()
      

conn.close()




