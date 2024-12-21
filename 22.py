import keyboard
import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("翻译助手")
root.geometry("300x200")

# 隐藏窗口的函数
def toggle_window():
    if root.winfo_viewable():  # 检查窗口是否可见
        root.withdraw()  # 隐藏窗口
    else:
        root.deiconify()  # 恢复窗口

# 设置全局快捷键
keyboard.add_hotkey('ctrl+h', toggle_window)

# 启动主循环
root.mainloop()