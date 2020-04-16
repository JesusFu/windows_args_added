# coding:utf-8
import winreg
import os
import ctypes

def add_context_menu():
    menu_name = '为程序启动添加参数'
    meanu_name_2 = '为程序添加预设启动参数'

    menu_command = '"'+ os.getcwd() + '\dist\QuickStart.exe" "%1"'
    menu_command_2 = '"' + os.getcwd() + '\dist\ConfigPre.exe"'

    key1 = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, '*\\shell',0, winreg.KEY_WRITE)
    newKey1 = winreg.CreateKey(key1, 'quick_start')
    winreg.SetValueEx(newKey1, "MUIVerb", 0, winreg.REG_SZ, menu_name)

    key2 = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, '*\\shell\\quick_start',0, winreg.KEY_WRITE)
    winreg.CreateKey(key2, 'command')
    winreg.SetValue(key2, "command", winreg.REG_SZ, menu_command)

    key3 = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, '*\\shell',0, winreg.KEY_WRITE)
    newKey3 = winreg.CreateKey(key3, 'quick_start_pre')
    winreg.SetValueEx(newKey3, "MUIVerb", 0, winreg.REG_SZ, meanu_name_2)
    winreg.SetValueEx(newKey3, "SubCommands", 0, winreg.REG_SZ,'')

    key4 = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, '*\\shell\\quick_start_pre',0, winreg.KEY_WRITE)
    winreg.CreateKey(key4, 'Shell')

    key5 = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, '*\\shell\\quick_start_pre\\Shell',0, winreg.KEY_WRITE)
    newKey5 = winreg.CreateKey(key5, 'add_pre')
    winreg.SetValueEx(newKey5, "MUIVerb", 0, winreg.REG_SZ, "启动预设编辑器")
    winreg.SetValueEx(newKey5, "icon", 0, winreg.REG_SZ,'')

    key6 = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, '*\\shell\\quick_start_pre\\Shell\\add_pre',0, winreg.KEY_WRITE)
    winreg.CreateKey(key6, 'command')
    winreg.SetValue(key6, "command", winreg.REG_SZ, menu_command_2)

if __name__ == '__main__':
    try:
        add_context_menu()
    except:
        ctypes.windll.user32.MessageBoxW(None,'注册列表写入失败，请以管理员身份运行注册程序！', '警告', 16)