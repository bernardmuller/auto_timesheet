import webbrowser
import os,os.path
from pathlib import Path

def Quickstart():
    # if not os.path.isdir("credentials-sheets.json"):
    #     webbrowser.open('https://developers.google.com/sheets/api/quickstart/python/')
    # else:
    #     pass
    #cwd = os.getcwd()
    json_file = '/credentials.json'
    downloads_path = str(Path.home() / "Downloads")
    file = downloads_path + json_file
    file_exists = os.path.exists(file)
    new_file = downloads_path + "/credentials-sheets.json"
    if file_exists == True:
         os.rename(file, new_file)

    #print(downloads_path + "credentials-sheets.json")

Quickstart()