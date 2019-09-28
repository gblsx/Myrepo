'''
print ("1).hello World")

#数字乘幂
a = input("请输入一个数字！")
b = input("请输入第二个数字！")
print ("2).",float(a)**float(b))


#计算三角形面积
a = input("长")
b = input("宽")
c = input("高")

mj = (float(a) + float(b) + float(c)) / 2

print ("%0.2f"  %mj)


#判断是否为数字

def isnumber(s):
       try:
          float(s)
          return True
       except ValueError:
          pass

       try:
         import unicodedata
         unicodedata.numeric(s)
         return True
       except(TypeError,ValueError):
         pass

         return False

a = '24f8'
#print(isnumber(a))
#pathon 自带的isdigit()方法
print(a.isdigit())



while True:
    try:
        num=int(input('输入一个整数：')) #判断输入是否为整数
    except ValueError: #不是纯数字需要重新输入
        print("输入的不是整数！")
        continue
    if num%2==0:
        print('偶数')
    else:
        print('奇数')
    break


'''

# 引入日历模块
import calendar
 
# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))
 
# 显示日历
print(calendar.month(yy,mm))


