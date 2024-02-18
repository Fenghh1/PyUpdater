import tkinter as tk
from tkinter import messagebox

import pyupdater  
import sys  
  
def on_update_downloaded(version):  
    print(f"更新版本 {version} 已下载，准备安装...")  
    # 在这里添加代码来安装更新  
    pyupdater.install_update()  
  
def on_update_installed():  
    print("更新已安装，重新启动应用程序...")  
    # 在这里添加代码来重新启动应用程序  
    sys.exit(0)  
  
def main():  
    # 初始化pyupdater  
    pyupdater.initialize('config.ini')  
  
    # 设置回调函数  
    pyupdater.set_callback(on_update_downloaded=on_update_downloaded, on_update_installed=on_update_installed)  
  
    # 检查并处理更新  
    if pyupdater.check_for_update():  
        if pyupdater.download_update():  
            # 下载完成后，调用回调函数处理下载完成事件  
            on_update_downloaded(pyupdater.get_latest_version())  
        else:  
            print("更新下载失败！")  
    else:  
        print("应用程序是最新的，无需更新。")  
  
    # 运行你的应用程序的主要逻辑  
    # ...  
     
    # 创建主窗口
    root = tk.Tk()
    root.withdraw() # 隐藏主窗口

    # 显示消息对话框
    messagebox.showinfo("提示", "这是一个弹窗小程序!!!")

    # 进入主事件循环
    root.mainloop()
  
if __name__ == "__main__":  
    main()