import json

data_file = "data.json"
def get_user_data(name, email):
    user = {}
    user['user'] = {'name': name, 'email': email}
    with open(data_file, 'w')as f:
        json.dump(user, f)

def extract_data():
    with open(data_file, "r") as read_file:
        data = json.load(read_file)
    return data


