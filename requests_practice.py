import requests

# 发送GET请求

print("===== 带参数的GET请求到 本地服务器 =====")  
# response = requests.get("http://localhost:8000/history?limit=1&offset=0")等效于下面的
response = requests.get("http://localhost:8000/history",params = {"limit": "1", "offset": "0"})
print(response.status_code)
print(response.json())  


print("===== POST请求 =====")
response = requests.post("http://localhost:8000/chat",json= {"message":"你好"})
print(response.status_code)
print(response.json())

# 敏感信息会通过POST请求发送，而不是GET请求
# 因为GET请求会将参数信息拼接在URL中，而POST请求会将参数信息封装在请求体中

# 封装函数+异常处理
def query_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=j1"  # 去掉反引号
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        # 从 data 里找到正确的层级取 temp_C 和 weatherDesc
        
        return f"{city}的温度：{data['temp_C']}℃,天气：{data['weatherDesc']}"
    except requests.exceptions.RequestException as e:
        return f"查询失败：{str(e)}"

a = query_weather("北京")
print(a)

import json
# 异常处理练习
def load_chat_history(filename):
    try:
        with open(filename,"r",encoding="utf-8")as f:
             messages = json.load(f)
             return messages


    except FileNotFoundError:
        messages = []
        print("文件不存在")
        return messages

    except json.JSONDecodeError:
        messages = []
        print("文件内容损坏")
        return messages
    finally:
        print("load_chat_history 执行完毕")

# 测试
# 文件不存在
print(load_chat_history("file"))

# 内容不合规
print(load_chat_history("json/aaaa.json"))   

# 文件内容合规
print(load_chat_history("json/chat_history.json"))
