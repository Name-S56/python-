import requests
import tkinter as tk
from tkinter import ttk, messagebox
from Baidu_Text_transAPI import Sentence_translate
import keyboard
import os

def translate_word_en(word, mode):
    url = "https://fanyi.baidu.com/sug"
    data_name = {"kw": word}
    resp = requests.post(url, data=data_name)

    if resp.status_code == 200:
        result = resp.json()
        if result.get("errno") == 0:
            return [(item['k'], item['v']) for item in result['data']]
        else:
            return f"错误信息: {result.get('errmsg')}"
    else:
        return f"请求失败，状态码：{resp.status_code}"

def on_translate():
    input_text = text_input.get("1.0", tk.END).strip()
    if input_text and input_text != "请输入翻译的文本":
        mode = "字典模式" if mode_var.get() == 1 else "句词模式"

        if mode == "字典模式":
            translations = translate_word_en(input_text, mode)
            text_output.delete("1.0", tk.END)
            
            if isinstance(translations, list):
                for k, v in translations:
                    text_output.insert(tk.END, f"{k}: {v}\n")
            else:
                text_output.insert(tk.END, translations)
        else:
            translation_result = Sentence_translate(input_text, 'auto', 'zh')
            text_output.delete("1.0", tk.END)

            if 'trans_result' in translation_result:
                for item in translation_result['trans_result']:
                    text_output.insert(tk.END, item['dst'] + "\n")
            else:
                error_message = translation_result.get('errmsg', '未知错误')
                text_output.insert(tk.END, f"错误信息: {error_message}")


def on_save():
    output_text = text_output.get("1.0", tk.END).strip()
    if output_text:
        file_path = os.path.join(os.getcwd(), "translations.txt")
        try:
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(output_text + "\n")  # 添加换行符以分隔条目
            messagebox.showinfo("保存成功", "翻译结果已添加到 translations.txt")
        except PermissionError:
            messagebox.showerror("保存失败", "没有权限写入文件，请检查文件状态。")
        except Exception as e:
            messagebox.showerror("保存失败", f"发生错误: {e}")
    else:
        messagebox.showwarning("保存失败", "没有翻译结果可保存。")

def on_entry_click(event):
    if text_input.get("1.0", tk.END).strip() == "请输入翻译的文本":
        text_input.delete("1.0", tk.END)
        text_input.config(fg="black")

def on_focusout(event):
    if text_input.get("1.0", tk.END).strip() == "":
        text_input.insert("1.0", "请输入翻译的文本")
        text_input.config(fg="grey")

# 隐藏窗口的函数
def toggle_window():
    if root.winfo_viewable():  # 检查窗口是否可见
        root.withdraw()  # 隐藏窗口
    else:
        root.deiconify()  # 恢复窗口

# 创建主窗口
root = tk.Tk()
root.title("翻译工具")

# 输入文本框
text_input = tk.Text(root, height=10, width=50, fg="grey")
text_input.insert("1.0", "请输入翻译的文本")
text_input.bind("<FocusIn>", on_entry_click)
text_input.bind("<FocusOut>", on_focusout)
text_input.pack(pady=10)

# 单选框
mode_var = tk.IntVar(value=1)
radio_dict = tk.Radiobutton(root, text="字典模式", variable=mode_var, value=1)
radio_sentence = tk.Radiobutton(root, text="句词模式", variable=mode_var, value=2)
radio_dict.pack(anchor='w')
radio_sentence.pack(anchor='w')

# 翻译按钮
translate_button = tk.Button(root, text="翻译", command=on_translate)
translate_button.pack(pady=10)

# 保存按钮
save_button = tk.Button(root, text="保存", command=on_save)
save_button.pack(pady=10)

# 输出文本框
text_output = tk.Text(root, height=10, width=50, fg="black")
text_output.pack(pady=10)

# 设置全局快捷键
keyboard.add_hotkey('alt+h', toggle_window)
keyboard.add_hotkey('ctrl+enter', on_translate)
keyboard.add_hotkey('ctrl+s', on_save)

# 运行主循环
root.mainloop()