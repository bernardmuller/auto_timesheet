import json
import os


data_file = "data.json"
def get_user_data(name, email):
    user = {}
    user['user'] = {'name': name, 'email': email}
    with open(data_file, 'w')as f:
        json.dump(user, f)
    Setup_Dir()

def extract_data():
    with open(data_file, "r") as read_file:
        data = json.load(read_file)
    return data

def get_dir():
    cwd = os.getcwd()
    return cwd

def Setup_Dir():
    prog_dir = get_dir()
    with open(data_file, 'r+')as f:
        data = json.load(f)
        data.update({'directory': prog_dir})
        f.seek(0)
        json.dump(data, f)



