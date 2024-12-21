import requests
import random
from hashlib import md5

# 请确保在代码中定义 appid 和 appkey
appid = '你的appid'
appkey = '你的appkey'

endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path

def Sentence_translate(query, from_lang='auto', to_lang='zh'):
    # 生成盐值和签名
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # 构建请求
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        'appid': appid,
        'q': query,
        'from': from_lang,
        'to': to_lang,
        'salt': salt,
        'sign': sign
    }

    # 发送请求
    r = requests.post(url, data=payload, headers=headers)

    # 检查响应状态
    if r.status_code == 200:
        result = r.json()
        return result  # 返回 JSON 响应
    else:
        return {'error': '请求失败，状态码：{}'.format(r.status_code)}

# 示例调用
if __name__ == "__main__":
    query = "Hello, how are you?"
    response = Sentence_translate(query)
    print(response)