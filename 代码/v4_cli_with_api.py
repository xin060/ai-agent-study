import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("SILICONFLOW_API_KEY")
client = OpenAI(api_key=api_key, base_url="https://api.siliconflow.cn/v1")

print("欢迎使用 AI 学习助手 v4")
print("输入 '退出' 结束对话")
print("输入 '历史' 查看聊天记录")

log_file = "json/chat_history.json" 

try:
    with open(log_file, "r", encoding="utf-8") as f:
        messages = json.load(f)
except FileNotFoundError:
    messages = []

while True:
    question = input("你：")
    if question == "退出":
        print("AI：下次再见，继续加油！")
        break
    if question == "历史":
        if len(messages) == 0:
            print("AI：还没有任何聊天记录")
        else:
            print("===== 历史聊天记录 =====")
            for msg in messages:
                role = "你" if msg["role"] == "user" else "AI"
                print(f"{role}：{msg['content']}")
            print("========================")
        continue

    messages.append({"role": "user", "content": question})
    try:
        send_messages = messages[-20:]
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=send_messages
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = "调用失败：" + str(e)

    print("AI：" + answer)
    messages.append({"role": "assistant", "content": answer})
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)