import subprocess
from safety.whitelist import APP_WHITELIST

def launch_app(app_key: str):
    if app_key not in APP_WHITELIST:
        raise ValueError("应用不在白名单中")

    subprocess.Popen(f'"{APP_WHITELIST[app_key]}"', shell=True)
    print(f"OPENED {APP_WHITELIST[app_key]}")