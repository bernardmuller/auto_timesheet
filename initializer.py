import user_data
import os
import os.path

def get_cwd():
    cwd = os.getcwd()
    return cwd

def startup_dir():
    cwd = get_cwd()
    string = cwd.split("\\")
    Startup_dir = str(string[0] + "\\" + string[1] + "\\" + string[2] + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" )
    return Startup_dir

def initialize():
    if not os.path.exists(str(startup_dir()) + "\\initialize.bat"):
        start_dir = startup_dir()
        #start_dir = "C:\\Users\\Bernard\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
        user = user_data.extract_data()
        os.chdir(start_dir)
        bat_text = open("initialize.bat", "w")
        directory = user['directory']
        bat_text.write("START " + directory + "\\auto.exe")
        bat_text.close()


initialize()
#startup_dir()