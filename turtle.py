from tkinter import*
 
#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('Python GUI Learning')
#设置窗口大小
width = 880
height = 300
#获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = myWindow.winfo_screenwidth()  
screenheight = myWindow.winfo_screenheight() 
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)   
myWindow.geometry(alignstr)
#设置窗口是否可变长、宽，True：可变，False：不可变
myWindow.resizable(width=False, height=True)
 
#框架布局
frame_root = Frame(myWindow)  
frame_l = Frame(frame_root)  
frame_r = Frame(frame_root) 
#创建一个标签，并在窗口上显示
Label(frame_l, text="中国", bg="green", font=("Arial", 12), width=10, height=2).pack(side=TOP)
Label(frame_l, text="日本", bg="red", font=("Arial", 12), width=10, height=2).pack(side=TOP)
Label(frame_r, text="美国", bg="yellow", font=("Arial", 12), width=10, height=2).pack(side=TOP)
Label(frame_r, text="韩国", bg="blue", font=("Arial", 12), width=10, height=2).pack(side=TOP)



#创建一个button 
data = IntVar()
var = StringVar()    # 这时文字变量储存器
def hit_me():
    global on_hit
    if on_hit == False:     # 从 False 状态变成 True 状态
        on_hit = True
        
        var.set('you hit me:%.3f' %(5))   # 设置标签的文字为 'you hit me'
      
    else:       # 从 True 状态变成 False 状态
        on_hit = False
        var.set('') # 设置 文字为空
      

#创建一个lable 
l = Label(myWindow, 
    textvariable=var,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='green', font=('Arial', 12), width=15, height=2)
l.pack() 


b = Button(myWindow, 
    text='hit me',      # 显示在按钮上的文字
    width=15, height=2, 
    command=hit_me)     # 点击按钮式执行的命令
b.pack()    # 按钮位置

on_hit = False  # 默认初始状态为 False



#框架的位置布局
frame_l.pack(side=LEFT)
frame_r.pack(side=RIGHT)
frame_root.pack() 
 
#进入消息循环
myWindow.mainloop()
