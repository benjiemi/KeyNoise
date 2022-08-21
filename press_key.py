"""
    @ Version: ??
    @ Author: 笨笨
    @ Contact: xuekun@sina.cn
    @ 说明: 自动按键
    @ Software: PyCharm
    @ File: press_key.py
    @ Time: 2018/7/28 2:24

"""
"""
 键   键码      键   键码          键   键码       键      键码 
      A   65          0   96            F1   112       Backspace    8 
      B   66          1   97            F2   113       Tab       9 
      C   67          2   98            F3   114       Clear      12 
      D   68          3   99            F4   115       Enter      13 
      E   69          4   100           F5   116      Shift      16 
      F   70          5   101           F6   117      Control     17 
      G   71         6   102           F7   118      Alt       18 
      H   72         7   103           F8   119      Caps Lock    20 
      I    73          8   104          F9   120      Esc       27 
      J    74          9   105          F10  121     Spacebar    32 
      K   75         *   106           F11  122      Page Up     33 
      L   76         +   107           F12  123      Page Down    34 
      M   77        Enter 108                          End       35 
      N   78         -   109                              Home      36 
      O   79         .   110                              Left Arrow   37 
      P   80         /   111                              Up Arrow    38 
      Q   81                                                Right Arrow   39 
      R   82                                                Down Arrow    40 
      S   83                                                Insert      45 
      T   84                                                Delete      46 
      U   85                                                Help       47 
      V   86                                                Num Lock     144   
      W  87          
      X   88      
      Y   89      
      Z   90      
      0   48      
      1   49      
      2   50       
      3   51       
      4   52       
      5   53       
      6   54       
      7   55       
      8   56       
      9   57
"""

import win32api
import win32con
from time import sleep
import pyautogui

key_hex = {'backspace': 0x08,
           'tab': 0x09,
           'clear': 0x0C,
           'enter': 0x0D,
           'shift': 0x10,
           'ctrl': 0x11,
           'alt': 0x12,
           'pause': 0x13,
           'caps_lock': 0x14,
           'esc': 0x1B,
           'spacebar': 0x20,
           'page_up': 0x21,
           'page_down': 0x22,
           'end': 0x23,
           'home': 0x24,
           'left_arrow': 0x25,
           'up_arrow': 0x26,
           'right_arrow': 0x27,
           'down_arrow': 0x28,
           'select': 0x29,
           'print': 0x2A,
           'execute': 0x2B,
           'print_screen': 0x2C,
           'ins': 0x2D,
           'del': 0x2E,
           'help': 0x2F,
           '0': 0x30,
           '1': 0x31,
           '2': 0x32,
           '3': 0x33,
           '4': 0x34,
           '5': 0x35,
           '6': 0x36,
           '7': 0x37,
           '8': 0x38,
           '9': 0x39,
           'a': 0x41,
           'b': 0x42,
           'c': 0x43,
           'd': 0x44,
           'e': 0x45,
           'f': 0x46,
           'g': 0x47,
           'h': 0x48,
           'i': 0x49,
           'j': 0x4A,
           'k': 0x4B,
           'l': 0x4C,
           'm': 0x4D,
           'n': 0x4E,
           'o': 0x4F,
           'p': 0x50,
           'q': 0x51,
           'r': 0x52,
           's': 0x53,
           't': 0x54,
           'u': 0x55,
           'v': 0x56,
           'w': 0x57,
           'x': 0x58,
           'y': 0x59,
           'z': 0x5A,
           'numpad_0': 0x60,
           'numpad_1': 0x61,
           'numpad_2': 0x62,
           'numpad_3': 0x63,
           'numpad_4': 0x64,
           'numpad_5': 0x65,
           'numpad_6': 0x66,
           'numpad_7': 0x67,
           'numpad_8': 0x68,
           'numpad_9': 0x69,
           'multiply_key': 0x6A,
           'add_key': 0x6B,
           'separator_key': 0x6C,
           'subtract_key': 0x6D,
           'decimal_key': 0x6E,
           'divide_key': 0x6F,
           'F1': 0x70,
           'F2': 0x71,
           'F3': 0x72,
           'F4': 0x73,
           'F5': 0x74,
           'F6': 0x75,
           'F7': 0x76,
           'F8': 0x77,
           'F9': 0x78,
           'F10': 0x79,
           'F11': 0x7A,
           'F12': 0x7B,
           'F13': 0x7C,
           'F14': 0x7D,
           'F15': 0x7E,
           'F16': 0x7F,
           'F17': 0x80,
           'F18': 0x81,
           'F19': 0x82,
           'F20': 0x83,
           'F21': 0x84,
           'F22': 0x85,
           'F23': 0x86,
           'F24': 0x87,
           'num_lock': 0x90,
           'scroll_lock': 0x91,
           'left_shift': 0xA0,
           'right_shift ': 0xA1,
           'left_control': 0xA2,
           'right_control': 0xA3,
           'left_menu': 0xA4,
           'right_menu': 0xA5,
           'browser_back': 0xA6,
           'browser_forward': 0xA7,
           'browser_refresh': 0xA8,
           'browser_stop': 0xA9,
           'browser_search': 0xAA,
           'browser_favorites': 0xAB,
           'browser_start_and_home': 0xAC,
           'volume_mute': 0xAD,
           'volume_Down': 0xAE,
           'volume_up': 0xAF,
           'next_track': 0xB0,
           'previous_track': 0xB1,
           'stop_media': 0xB2,
           'play/pause_media': 0xB3,
           'start_mail': 0xB4,
           'select_media': 0xB5,
           'start_application_1': 0xB6,
           'start_application_2': 0xB7,
           'attn_key': 0xF6,
           'crsel_key': 0xF7,
           'exsel_key': 0xF8,
           'play_key': 0xFA,
           'zoom_key': 0xFB,
           'clear_key': 0xFE,
           '+': 0xBB,
           ',': 0xBC,
           '-': 0xBD,
           '.': 0xBE,
           '/': 0xBF,
           '`': 0xC0,
           ';': 0xBA,
           '[': 0xDB,
           '\\': 0xDC,
           ']': 0xDD,
           "'": 0xDE,
           '`': 0xC0}

key_num = {"A": 65,
           "0": 96,
           "F1": 112,
           "Backspace": 8,
           "B": 66,
           "C": 67,
           "D": 68,
           "E": 69,
           "F": 70,
           "G": 71,
           "H": 72,
           "I": 73,
           "J": 74,
           "K": 75,
           "L": 76,
           "M": 77,
           "N": 78,
           "O": 79,
           "P": 80,
           "Q": 81,
           "R": 82,
           "S": 83,
           "T": 84,
           "U": 85,
           "V": 86,
           "W": 87,
           "X": 88,
           "Y": 89,
           "Z": 90,
           "0": 48,
           "1": 49,
           "2": 50,
           "3": 51,
           "4": 52,
           "5": 53,
           "6": 54,
           "7": 55,
           "8": 56,
           "9": 57,
           "1": 97,
           "2": 98,
           "3": 99,
           "4": 100,
           "5": 101,
           "6": 102,
           "7": 103,
           "8": 104,
           "9": 105,
           "*": 106,
           "+": 107,
           "Enter": 108,
           "-": 109,
           ".": 110,
           "/": 111,
           "F2": 113,
           "F3": 114,
           "F4": 115,
           "F5": 116,
           "F6": 117,
           "F7": 118,
           "F8": 119,
           "F9": 120,
           "F10": 121,
           "F11": 122,
           "F12": 123,
           "Tab": 9,
           "Clear": 12,
           "Enterr": 13,
           "Shift": 16,
           "Control": 17,
           "Alt": 18,
           "CapsLock": 20,
           "Esc": 27,
           "Spacebar": 32,
           "PageUp": 33,
           "PageDown": 34,
           "End": 35,
           "Home": 36,
           "LeftArrow": 37,
           "UpArrow": 38,
           "RightArrow": 39,
           "DownArrow": 40,
           "Insert": 45,
           "Delete": 46,
           "Help": 47,
           "NumLock": 144}


def auto_press_key(key_name, dis_time=0.1):
    """
    每隔一段时间自动按键
    :param key_name: 键名
    :param dis_time: 间隔
    :return:
    """
    num = key_num[key_name]

    win32api.keybd_event(num, 0, 0, 0)  # v键位码是86
    sleep(dis_time)

    win32api.keybd_event(num, 0, win32con.KEYEVENTF_KEYUP, 0)


import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def auto_press_key_super(key_name, dis_time=0.1):
    # directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
    new_key = key_name.upper() if key_name.lower() not in key_num.keys() else key_name.lower()
    num = key_num[new_key]
    num = 0x1E
    print(key_name, num)
    PressKey(num)
    time.sleep(dis_time)
    ReleaseKey(num)
    time.sleep(dis_time)


def auto_press_key_pyautogui(key_name, dis_time=0.1):
    pyautogui.press(key_name)


from ctypes import *

import time

# 注册DD DLL，64位python用64位，32位用32位，具体看DD说明文件。
# 测试用免安装版。
# 用哪个就调用哪个的dll文件。
# dd_dll = windll.LoadLibrary('64/DD81200x64.64.dll')

# DD虚拟码，可以用DD内置函数转换。
vk = {'5': 205, 'c': 503, 'n': 506, 'z': 501, '3': 203, '1': 201, 'd': 403, '0': 210, 'l': 409, '8': 208, 'w': 302,
      'u': 307, '4': 204, 'e': 303, '[': 311, 'f': 404, 'y': 306, 'x': 502, 'g': 405, 'v': 504, 'r': 304, 'i': 308,
      'a': 401, 'm': 507, 'h': 406, '.': 509, ',': 508, ']': 312, '/': 510, '6': 206, '2': 202, 'b': 505, 'k': 408,
      '7': 207, 'q': 301, "'": 411, '\\': 313, 'j': 407, '`': 200, '9': 209, 'p': 310, 'o': 309, 't': 305, '-': 211,
      '=': 212, 's': 402, ';': 410}
# 需要组合shift的按键。
vk2 = {'"': "'", '#': '3', ')': '0', '^': '6', '?': '/', '>': '.', '<': ',', '+': '=', '*': '8', '&': '7', '{': '[',
       '_': '-',
       '|': '\\', '~': '`', ':': ';', '$': '4', '}': ']', '%': '5', '@': '2', '!': '1', '(': '9'}


def down_up(code, pre_time):
    # 进行一组按键。

    dd_dll.DD_key(vk[code], 1)
    sleep(pre_time)
    dd_dll.DD_key(vk[code], 2)


def down(code):
    dd_dll.DD_key(vk[code], 1)


def up(code):
    dd_dll.DD_key(vk[code], 2)


def dd(i, last_time):
    if isinstance(i, int):
        dd_dll.DD_key(i, 1)
        sleep(0.5)
        dd_dll.DD_key(i, 2)
    else:
        # 500是shift键码。
        if i.isupper():
            # 如果是一个大写的玩意。

            # 按下抬起。
            dd_dll.DD_key(500, 1)
            down_up(i.lower(), last_time)
            dd_dll.DD_key(500, 2)

        elif i in '~!@#$%^&*()_+{}|:"<>?':
            # 如果是需要这样按键的玩意。
            dd_dll.DD_key(500, 1)
            down_up(vk2[i], last_time)
            dd_dll.DD_key(500, 2)
        else:
            down_up(i, last_time)


def auto_press_key_dll(key_name, last_time=0.1):
    dd(key_name, last_time)


class key_obj:
    def __init__(self, key, dis_time, pre_time, off_set, last_time=0.5, sleep_time=0):
        self.key = key  # 键值
        self.dis_time = dis_time  # 间隔
        self.pre_time = pre_time  # 上次执行时间
        self.off_set = off_set  # 偏移
        self.pre_time = self.pre_time + self.off_set
        self.last_time = last_time  # 持续时间
        self.sleep_time = sleep_time  # 前后等待时间


class key_mgr:
    """
    按键管理
    """
    key_list = []

    def __init__(self):
        pass

    def add_key(self, key, dis_time, off_set=0, last_time=0.5, sleep_time=0):
        key_info = key_obj(key, dis_time, time.time(), off_set, last_time, sleep_time)
        self.key_list.append(key_info)

    def process(self):
        while 1:
            for key_info in self.key_list:

                if (time.time() - key_info.pre_time) > key_info.dis_time:
                    if key_info.sleep_time > 0:
                        sleep(key_info.sleep_time)
                    print(key_info.key)
                    auto_press_key_dll(key_info.key, key_info.last_time)
            sleep(0.05)

    def test(self):
        for i in range(700, 1000):
            for x in range(5):
                print(i)
                dd(i, 0.5)


# while 1:
#     pyautogui.FAILSAFE = False
#     auto_press_key_dll("a", 0.05)
#     sleep(1)

# def test1():
#     key_mgr = key_mgr()
#     # key_mgr.add_key("s", 1)
#     key_mgr.add_key("1", 30)
#     key_mgr.add_key("a", 0.1, last_time=5)
#     # key_mgr.add_key("w", 8)
#     # key_mgr.add_key(709, 400, off_set=30, last_time=1, sleep_time=0)  # ↑
#     # key_mgr.add_key(710, 400, off_set=0, last_time=1, sleep_time=0)  # ←
#     # key_mgr.add_key(711, 400, off_set=10, last_time=1, sleep_time=0)  # ↓
#     # key_mgr.add_key(712, 400, off_set=20, last_time=1, sleep_time=0)  # →
#     key_mgr.process()
#     # key_mgr.test()
#

import pyautogui


def ttest2():
    # im1 = pyautogui.screenshot()
    # im1.save('my_screenshot.png')
    #
    # im2 = pyautogui.screenshot('my_screenshot2.png')
    sleep(0.1)
    file = "feng.png"

    # 保护措施，避免失控
    pyautogui.FAILSAFE = True
    # 为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。
    pyautogui.PAUSE = 1

    # 在当前屏幕中查找指定图片(图片需要由系统截图功能截取的图)
    coords = pyautogui.locateOnScreen(file)
    print(coords)
    # 获取定位到的图中间点坐标
    # x, y = pyautogui.center(coords)
    # print(x,y)
    # 右击该坐标点
    pyautogui.moveTo(870, 736, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.doubleClick(interval=0.3)
    # pyautogui.rightClick(x, y)
    # dd_dll.SetCursorPos(x , y)
    pass


if __name__ == '__main__':
    ttest2()
