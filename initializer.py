import user_data
import os.path
import os, winshell
from win32com.client import Dispatch

def get_cwd():
    cwd = os.getcwd()
    return cwd

def startup_dir():
    cwd = get_cwd()
    string = cwd.split("\\")
    Startup_dir = str(string[0] + "\\" + string[1] + "\\" + string[2] + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" )
    return Startup_dir

def initialize():
    if not os.path.exists(get_cwd() + "\\initialize.bat"):
        user = user_data.extract_data()
        bat_text = open("initialize.bat", "w")
        directory = user['directory']
        bat_text.write("START " + directory + "\\auto.exe")
        bat_text.close()
        shortcut()

def shortcut():
    start_dir = startup_dir()
    path = os.path.join(start_dir, "initialize.lnk")
    target = f"{get_cwd()}\\initialize.bat"
    icon = f"{get_cwd()}\\initialize.bat"

    shell = Dispatch('WScript.shell')
    shortcut = shell.CreateShortcut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = get_cwd()
    shortcut.IconLocation = icon
    shortcut.save()

#initialize()
startup_dir()