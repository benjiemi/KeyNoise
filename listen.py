import keyboard

import wave
import pyaudio
import json
import os
import threading
from queue import Queue
import numpy as np
import string
import random
import win32clipboard as wc
import win32con
import win32gui, win32api

# 声音目录
path = 'sound'
# 子目录
key = 'bubbles2'
key = 'mechanical4'
# 线程通信队列
q = Queue()
# 每个循环播放声音的bytes
chunk = 1024
current_path = os.path.dirname(__file__)
def load_json():
    with open(os.path.join(current_path, "sound.json"), 'r') as fp:
        return json.load(fp)
def read_trunk(file_name):
    if not file_name.endswith(".wav"):
        file_name += ".wav"
    file_name = os.path.join(current_path, file_name)
    print(file_name)
    wf = wave.open(file_name, 'rb')
    data = wf.readframes(chunk*1024)  # 读取数据
    return data
def x_times(in_data, size):
    # TODO://倍速播放(未完成)
    size = 1 if size <= 0 else size
    factor = 1/size
    f_data = np.frombuffer(in_data, 
        dtype=np.int).astype(np.float) # need to use floats for interpolation 
    data_size = len(f_data)
    x0 = np.linspace(0, data_size - 1, data_size) 
    x1 = np.linspace(0, data_size - 1, int(data_size * factor)) # i.e. 0.5 will play twice as fast 
    # x1 = x1[:int(len(f_data) * factor)] 
    print("x1", len(x1))
    print("x0", len(x0))
    print("f_data", len(f_data))
    data = np.interp(x1, x0, f_data).astype(np.int)
    print("data", len(data))
    return data

def config():
    # 配置
    pass
def play():
    # 播放声音线程
    tt = load_json()[key][0]["path"][-1]
    if not tt.endswith(".wav"):
        tt += ".wav"
    print("xxx:", os.path.join(path, tt))
    full_path = os.path.join(current_path, path, tt)
    wf = wave.open(full_path, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                    rate=wf.getframerate(), output=True)
    try:
        back= None
        pp = None
        while True:  # 播放
            try:
                data = q.get_nowait()
                back = data
            except:
                if not back or (back and len(back) == 0):
                    data = q.get()
                    back = data
            if back:
                size = chunk if len(back) > chunk else len(back)            
                pp = back[:size]
                if len(back) > 0:
                    back = back[size:]
                    stream.write(pp)
    finally:
        stream.stop_stream()  # 停止数据流
        stream.close()
        p.terminate()  # 关闭 PyAudio

all_keys = ['{','}','(',')','end', 'up', 'caps lock', 'tab', "'", 'f6', 'clear', '[', 'left windows', 'left', 'f11', 'right shift', '=', 'home', 'right windows', 'f9', '.', 'alt', ';', '/', 'f5', 'right', 'ctrl', 'f4', 'f7', 'f2', 'shift', 'num lock', 'page up', 'f10', '$', ']', 'f1', '-', 'right alt', 'f8', 'f3', 'insert', 'f12', 'space', 'down', '`', 'backspace', 'esc', '*', 'delete', '+', ',', 'right ctrl', 'page down', 'enter', '\\']
all_keys += [x for x in string.ascii_lowercase]
all_keys += [str(i) for i in range(10)]

x_key = [x.replace(" ", "") for x in all_keys]
all_keys = list(set(all_keys + x_key))

all_index = {}
cnf = load_json()[key][0]
all_path = cnf["path"]
all_data = [read_trunk(os.path.join(path, x))  for x in all_path]
non_unique_count = cnf["non_unique_count"]

key_status = {}
for x in all_path:
    lk = os.path.basename(x).lower()
    v = all_path.index(x)
    if lk in all_keys:
        all_index[lk] = v
if "map" in cnf:
    for k in cnf["map"]:
        lk = k.lower()
        v = cnf["map"][k]
        if lk.lower() in all_keys and v < len(all_data):
            all_index[lk] = v

for kk in all_keys:
    if kk not in all_index:
        all_index[kk] = random.randint(0, non_unique_count-1)
    

def abc(x):
    global key_status
    lk =  x.name.lower()
    if x.event_type != 'down':
        key_status[lk] = 0
        return
    # 键盘映射
    # with open("1.txt", 'a') as fp:
    #     fp.write(f'"{x.name}",')
    try:
        if lk in all_index:
            data = all_data[all_index[lk]]
            print(lk, all_path[all_index[lk]])
        else:
            lk = lk.replace(" ", "")
            print(lk, all_path[all_index[lk]])
            data = all_data[all_index[lk]]
    except:
        idx = random.randint(0, non_unique_count)
        all_index[lk] = idx
        data = all_data[all_index[lk]]
    if lk not in key_status or key_status[lk] == 0:
        key_status[lk] = 1
        q.put(data)

def use_for_test(x):
    if x.event_type != 'down':
        return
    data = x_times(all_data[-1], 2)
    tt = load_json()[key][0]["path"][-1]
    if not tt.endswith(".wav"):
        tt += ".wav"
    wf = wave.open(os.path.join(path, tt), 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                    rate=wf.getframerate(), output=True)
    try:
        # while True:  # 播放
        stream.write(data)
    finally:
        stream.stop_stream()  # 停止数据流
        stream.close()
        p.terminate()  # 关闭 PyAudio


def opt(ctx):
    print(ctx)
    wc.OpenClipboard()
    try:
        wc.EmptyClipboard()
        wc.SetClipboardData(win32con.CF_UNICODETEXT, ctx)
    except Exception as e:
        print("异常:", str(e))
    finally:
        wc.CloseClipboard()
def regist(key, ctx):
    keyboard.add_hotkey(key, opt, (ctx,))
t1 = threading.Thread(target=play)
t1.start()
# thread_pool = ThreadPoolExecutor(max_workers=3)
# thread_pool.submit(play)
# thread_pool.submit(play)
# thread_pool.shutdown(wait=True)
regist("ctrl+4", "/usr/local/shark-security/var/log/")
regist("ctrl+5", "/usr/local/shark-security/etc/")
regist("ctrl+6", "/usr/local/shark-security/etc/channel.d/")
regist("ctrl+7", "/usr/local/shark/var/log")
regist("ctrl+8", "/usr/local/shark/etc/")
regist("ctrl+9", "/usr/local/shark/var/log/security_logs/")



keyboard.hook(abc)
# keyboard.hook(acc)

#按下任何按键时，都会调用abc，其中一定会传一个值，就是键盘事件
keyboard.wait()
q.join()
