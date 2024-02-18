import tkinter as tk
from tkinter import messagebox
 
# 创建主窗口
root = tk.Tk()
root.withdraw() # 隐藏主窗口
 
# 显示消息对话框
messagebox.showinfo("提示", "这是一个弹窗小程序！")
 
# 进入主事件循环
root.mainloop()