# from agent.core import run_agent
#
# if __name__ == "__main__":
#     while True:
#         user = input("你想让我做什么？> ")
#         if user in ("exit", "quit"):
#             break
#         print(run_agent(user))



from agent.core import run_agent
import sounddevice as sd
import queue
import vosk
import json
import pyttsx3

# 录音队列
q = queue.Queue()

# 麦克风回调函数
def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

# 加载 Vosk 离线中文模型（第一次使用需要下载模型）
# 下载链接：https://alphacephei.com/vosk/models  https://alphacephei.com/vosk/models?utm_source=chatgpt.com
# 例如下载 "vosk-model-small-cn-0.22"，解压到当前目录
# model_path = r"C:\Users\carah\Downloads/vosk-model-small-en-us-0.15"
# model = vosk.Model(model_path)
model = vosk.Model(r"C:\Pythoncode\AI\hybrid-agent\vosk-model-small-cn-0.22")

engine = pyttsx3.init()
# r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    rec = vosk.KaldiRecognizer(model, 16000)
    speak("你好，Miss Cara， 我亲爱的主人，我可以和你对话了, 请说出你的指令...")
    print("请说出你的指令...")
    with sd.RawInputStream(samplerate=16000, blocksize = 8000, dtype='int16',
                           channels=1, callback=callback):
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    speak(f"识别到指令: {text}")
                    print(f"识别到指令: {text}")
                    return text

if __name__ == "__main__":
    while True:
        command = listen_command()
        if command in ("退出", "结束", "quit", "exit"):
            speak("已退出语音控制。")
            print("已退出语音控制。")
            break
        speak(f"command{command}")
        print(f"command{command}")
        output = run_agent(command)
        speak(output)
        print(output)