

# 打包方式 -否丢失 webbrowser 模块
pyinstaller --onefile --hidden-import=webbrowser mian.py
