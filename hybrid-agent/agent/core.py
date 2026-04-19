from agent.planner import plan
from tools.browser import open_and_search
from tools.shell import launch_app
from safety.whitelist import APP_WHITELIST


def run_agent(user_input: str):
    action = plan(user_input=user_input, APP_WHITELIST=APP_WHITELIST)
    print(f"action:{action}")

    if action["type"] == "browser":
        open_and_search(action["target"])
        return "已通过浏览器完成任务"

    elif action["type"] == "shell":
        launch_app(action["target"])
        return f"已帮你打开本地应用：{action['target']}"
    else:
        return "当前请求无需执行工具"