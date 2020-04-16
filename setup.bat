%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
pyinstaller -Fw QuickStart.py
pyinstaller -Fw ConfigPre.py
python __init__.py