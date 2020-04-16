import subprocess
import sys
import winreg
import ctypes
import re
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def admin_get():
    if is_admin():
        return True
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            sys.exit()
        else:#in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", (sys.executable), (__file__), None, 1)
            sys.exit()


def find_and_delete_key(key_str):
    print(key_str)
    key=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,key_str,0,winreg.KEY_ALL_ACCESS)

    countkey=winreg.QueryInfoKey(key)[0]

    if countkey!=0:
        for i in range(countkey-1,-1,-1):
            key_name=winreg.EnumKey(key,i) #取键名
            find_and_delete_key(key_str+"\\"+key_name)
    try:
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, key_str)
    except FileNotFoundError:
        pass
        return
    return 0

def CheckAdmin():
    if is_admin():
        return 0
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

def delete_key(pos):
    try:
        uploads = "*\\shell\\quick_start_pre\\Shell\\"+pos
        find_and_delete_key(uploads)
        return 0
    except Exception as e:
        print(e)
        return -1

def submains_register_in_shell(pos,name,icon):
    try:
        uploads = "*\\shell\\quick_start_pre\\Shell\\"
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, uploads, 0, winreg.KEY_WRITE)

        newKey = winreg.CreateKey(key, 'PRECONFIGSECONDLIST_'+str(pos))
        winreg.SetValueEx(newKey, "MUIVerb", 0,winreg.REG_SZ, str(name))
        winreg.SetValueEx(newKey, "icon", 0,winreg.REG_SZ, str(icon))
        winreg.SetValueEx(newKey, "SubCommands", 0, winreg.REG_SZ, '')

        uploads2 = "*\\shell\\quick_start_pre\\Shell\\" + 'PRECONFIGSECONDLIST_'+str(pos)+"\\"
        keys = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, uploads2, 0, winreg.KEY_WRITE)
        winreg.CreateKey(keys, 'Shell')
        winreg.SetValue(keys, "Shell", winreg.REG_SZ, '')
        return 0
    except Exception as e:
        print(e)
        return -1



def Key_register_in_shell(pos,name,command,icon):
    try:
        if pos != "BASIC":
            uploads = "*\\shell\\quick_start_pre\\Shell\\" + str(pos) + "\\Shell"
        else :
            uploads = "*\\shell\\quick_start_pre\\Shell\\"
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,uploads,0, winreg.KEY_WRITE)

        newKey = winreg.CreateKey(key, name)
        winreg.SetValueEx(newKey, "MUIVerb", 0,winreg.REG_SZ, str(name))
        winreg.SetValueEx(newKey, "icon", 0,winreg.REG_SZ, str(icon))

        if pos != "BASIC":
            uploads = "*\\shell\\quick_start_pre\\Shell\\" + str(pos) + "\\Shell\\" + str(name)
        else:
            uploads = "*\\shell\\quick_start_pre\\Shell\\"+ str(name)
        keys = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,uploads,0, winreg.KEY_WRITE)

        commandKey = winreg.CreateKey(keys, 'command')
        winreg.SetValue(keys, "command", winreg.REG_SZ,command)

        return 0
    except Exception as e:
        print(e)
        return -1

def subNodeKey(key, patchlist,iconlist,commandlist):
    count = winreg.QueryInfoKey(key)[0]
    for index in range(count):
        name = winreg.EnumKey(key, index)
        subs = winreg.OpenKey(key, name)
        patchlist.append(name)
        iconlist.append(winreg.QueryValueEx(subs, 'icon')[0])
        commands = winreg.OpenKey(subs,'command')
        commandlist.append(winreg.QueryValue(commands,None))



def BasicNodeRead():
    iconlist = []
    commandlist = []
    patchlist = []
    updates = '*\\shell\\quick_start_pre\\Shell'
    key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, updates)
    count = winreg.QueryInfoKey(key)[0]
    for index in range(count):
        name = winreg.EnumKey(key, index)
        print(name)
        if "PRECONFIGSECONDLIST" not in name:
            subs = winreg.OpenKey(key, name)
            iconlist.append(winreg.QueryValueEx(subs, 'icon')[0])
            patchlist.append(name)
            commands = winreg.OpenKey(subs, 'command')
            commandlist.append(winreg.QueryValue(commands, None))
    return patchlist,iconlist,commandlist


def subRegKey(key, pattern, patchlist ,MUIList ,iconList):
    # 个数
    count = winreg.QueryInfoKey(key)[0]
    for index in range(count):
        name = winreg.EnumKey(key, index)
        if "PRECONFIGSECONDLIST" in name:
            subs = winreg.OpenKey(key, name)
            patchlist.append(name)
            MUIList.append(winreg.QueryValueEx(subs,'MUIVerb' )[0])
            iconList.append(winreg.QueryValueEx(subs,'icon' )[0])


def fetch_lists():
    patchlistchild = []
    patchlisticon = []
    patchlidcommand = []
    patchlist = []
    MUIList = []
    iconList = [ ]
    updates = '*\\shell\\quick_start_pre\\Shell'
    key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, updates)
    subRegKey(key, 'quick_start_pre', patchlist,MUIList,iconList)
    print ('Count: ' + str(len(patchlist)))
    for p in patchlist:
        print(p)
        temploc = updates + "\\" + p + "\\Shell"
        tempkey = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, temploc)
        patchlisttemp = []
        childicon = []
        commandlist = []
        subNodeKey(tempkey,patchlisttemp,childicon,commandlist)
        patchlistchild.append(patchlisttemp)
        patchlisticon.append(childicon)
        patchlidcommand.append(commandlist)
    winreg.CloseKey(key)
    return MUIList,iconList,patchlist,patchlistchild,patchlisticon,patchlidcommand


def run_it(exec_d,args_after):
    run = subprocess.Popen(exec_d + ' ' + args_after)
    sys.exit()

