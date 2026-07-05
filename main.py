from fastapi import FastAPI
from pydantic import BaseModel
import json
import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载配置
load_dotenv()
api_key = os.getenv("SILICONFLOW_API_KEY")
client = OpenAI(api_key=api_key,base_url="https://api.siliconflow.cn/v1")

# 创建FastAPI应用
app = FastAPI()

# 定义请求格式
class ChatRequest(BaseModel):
    message: str

# 加载历史记录
log_life = "chat_history.json"
try:
    with open(log_life,"r",encoding="utf-8")as f:
        messages = json.load(f)
except FileNotFoundError:
    messages = []

# 路由
@app.post("/chat")
def chat(request: ChatRequest):
    messages.append({"role":"user","content":request.message})

    try:
        send_messages = messages[-20:]
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=send_messages
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = "调用失败: " + str(e)

    messages.append({"role":"assistant","content":answer})

    with open(log_life,"w",encoding="utf-8")as f:
        json.dump(messages,f,ensure_ascii=False,indent=2)

    return {"reply":answer}

@app.get("/history")
def get_history():
    return {"messages":messages}
