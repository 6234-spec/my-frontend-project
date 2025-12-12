from flask import Flask
import subprocess
import os
import platform

app = Flask(__name__)

# ********** 必须修改：替换为你的happy.py绝对路径 **********
# 示例：PYTHON_SCRIPT_PATH = r"C:\Users\yang rui ze\Desktop\学习资料\python\happy.py"
PYTHON_SCRIPT_PATH = r"C:\Users\yang rui ze\Desktop\学习资料\python\happy.py"


@app.route('/run-popup')
def run_popup():
    # 兼容Windows/Mac的Python命令
    python_cmd = 'python' if platform.system() == "Windows" else 'python3'

    # 路径校验，避免写错
    if not os.path.exists(PYTHON_SCRIPT_PATH):
        return f"文件不存在！路径：{PYTHON_SCRIPT_PATH}", 404

    # Windows隐藏黑框
    startupinfo = None
    if platform.system() == "Windows":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    # 立刻启动Python
    try:
        subprocess.Popen(
            [python_cmd, PYTHON_SCRIPT_PATH],
            shell=False,
            startupinfo=startupinfo
        )
        return "弹窗已启动"
    except Exception as e:
        return f"调用失败：{str(e)}", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=False, debug=False)