import requests
import tkinter as tk
from tkinter import ttk

def translate_word_en(word):
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
        translations = translate_word_en(input_text)
        text_output.delete("1.0", tk.END)
        
        if isinstance(translations, list):
            for k, v in translations:
                text_output.insert(tk.END, f"{k}: {v}\n")
        else:
            text_output.insert(tk.END, translations)

def on_entry_click(event):
    if text_input.get("1.0", tk.END).strip() == "请输入翻译的文本":
        text_input.delete("1.0", tk.END)
        text_input.config(fg="black")

def on_focusout(event):
    if text_input.get("1.0", tk.END).strip() == "":
        text_input.insert("1.0", "请输入翻译的文本")
        text_input.config(fg="grey")

# 创建主窗口
root = tk.Tk()
root.title("翻译工具")

# 输入文本框
text_input = tk.Text(root, height=10, width=50, fg="grey")
text_input.insert("1.0", "请输入翻译的文本")
text_input.bind("<FocusIn>", on_entry_click)
text_input.bind("<FocusOut>", on_focusout)
text_input.pack(pady=10)

# 翻译按钮
translate_button = tk.Button(root, text="翻译", command=on_translate)
translate_button.pack(pady=10)

# 输出文本框
text_output = tk.Text(root, height=10, width=50, fg="black")
text_output.pack(pady=10)

# 运行主循环
root.mainloop()