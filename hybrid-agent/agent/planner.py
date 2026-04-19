import requests
import json

def llm(prompt: str) -> str:
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen3:0.6b",
            "prompt": prompt,
            "stream": False
        }
    )
    return r.json()["response"]

def plan(user_input: str, APP_WHITELIST: str) -> dict:
    prompt = f"""
    你是一个任务规划器，只返回 JSON，不要解释。

    规则：
    - 搜索 → type=browser
    - 打开本地应用 / 执行程序 → type=shell
    - 否则 → type=none

    示例：
    用户：打开腾讯
    返回：
    {{"type":"shell","target":"tencent"}}
    用户：打开微信/weixin
    返回：
    {{"type":"shell","target":"wechat"}}

    用户：搜索什么什么
    返回：
    {{"type":"browser","target":"什么什么"}}

    target的输出，你可以参考这个文档的key值：{APP_WHITELIST}
    用户请求：{user_input}
    """
    return json.loads(llm(prompt))


 # {{"type": "browser", "target": "搜索 Playwright 教程"}}
