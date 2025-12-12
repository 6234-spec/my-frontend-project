import tkinter as tk
import random
import threading
import time
import sys
import os

exit_flag = False

def show_warm_tip():
    global exit_flag
    if exit_flag:
        return

    window = tk.Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 250
    window_height = 60
    x = random.randrange(0, screen_width - window_width)
    y = random.randrange(0, screen_height - window_height)

    window.title("🎄圣诞快乐")
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 固定提示语列表（无需修改）
    tips = [
        "天天开心😊~", "保持微笑~", "每天都要元气满满❤️~",
        "辛苦了大学生", "加油努力~", "好好爱自己~",
        "梦想成真~", "今天累吗？", "今天也要好好写代码", "圣诞节快乐"
    ]
    tip = random.choice(tips)

    bg_colors = [
        'lightblue', 'skyblue', 'lightgreen', 'lavender',
        'lightyellow', 'plum', 'coral', 'bisque', 'aquamarine'
    ]
    bg = random.choice(bg_colors)

    # 优化：减少标签冗余配置，加快渲染
    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=("微软雅黑", 16),
        wraplength=230  # 固定换行宽度，避免计算延迟
    ).pack(padx=10, pady=10)

    window.attributes("-topmost", True)

    def on_space(event):
        global exit_flag
        exit_flag = True
        window.destroy()
        os._exit(0) if os.name == 'nt' else sys.exit(0)

    window.bind("<space>", on_space)

    # 移除不必要的check_exit循环（减少资源占用）
    window.mainloop()

# 优化：缩短线程启动间隔（从0.05s改为0.01s），更快弹出所有窗口
threads = []
max_threads = 30  # 保持30个窗口，兼顾效果和速度
for i in range(max_threads):
    t = threading.Thread(target=show_warm_tip)
    t.daemon = True
    threads.append(t)
    t.start()
    time.sleep(0.01)  # 间隔极短，几乎同时弹出