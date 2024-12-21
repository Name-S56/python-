import requests
from Baidu_Text_transAPI import Sentence_translate
def translate_word_en():
    url = "https://fanyi.baidu.com/sug"
    print("字典模式,默认为英文模式")
    while True:
        data_name = {
            "kw": input('输入一个单词 (输入 "~exit" 退出): \n>>')
        }
        first_item_processed = True  #首行标志>>
        if data_name["kw"].lower() == "~exit":
            break
        # elif data_name["kw"].lower() =="~2":
        #     translate_word_jp()
        elif data_name["kw"].lower() =="~s":
            flag = not flag
        resp = requests.post(url, data=data_name)

        if resp.status_code == 200:
            result = resp.json()
            if result.get("errno") == 0:
                print("翻译结果:")
                for item in result['data']:
                    print(f"{item['k']}: {item['v']}")
                    if save_model == True:
                        save_bef(first_item_processed)
                        first_item_processed = save_bef(first_item_processed) 
                        save(f"{item['k']}: {item['v']}")
            else:
                print("错误信息:", result.get("errmsg"))
        else:
            print("请求失败，状态码：", resp.status_code)
    print('\n')

def translate_word_jp():

    # url= "https://www.mojidict.com/"
    print("输入“~1”可切换为英文文模式")
    while True:
        data_name = {
                "kw": input('输入一个单词 (输入 "~exit" 退出): \n>>')
            }
        first_item_processed = True  #首行标志>>
        if data_name["kw"].lower() == "~exit":
            break
        elif data_name["kw"].lower() =="~1":
            translate_word_en()
        elif data_name["kw"].lower() =="~s":
            flag = not flag

        resp = requests.post(url, data={'searchbar':data_name})
        if resp.status_code == 200:
            result = resp.json()
            if result.get("errno") == 0:
                print("翻译结果:")
                for item in result['data']:
                    print(f"{item['k']}: {item['v']}")
                    if save_model == True:
                        save_bef(first_item_processed)
                        first_item_processed = save_bef(first_item_processed) 
                        save(f"{item['k']}: {item['v']}")
            else:
                print("错误信息:", result.get("errmsg"))
        else:
            print("请求失败，状态码：", resp.status_code)
    print('\n')

def save_bef(first_item_processed):
    if first_item_processed:
        with open(file_path,'a', encoding='utf-8') as file:
           file.write("\n>>")
           first_item_processed = False
        return first_item_processed

def save(content_add):
# 调用翻译函数
    # 使用with语句处理文件
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content_add + '\n')

file_path = 'word.txt'
save_model  = True
print("“~s”切换记录保存方式,默认记录模式")
translate_word_en()



def S_translate():
    query = input("(句词翻译模式)请输入要翻译的文本:")
    result = Sentence_translate(query)
    print(json.dumps(result, indent=4, ensure_ascii=False))