#import webbrowser
import os,os.path
from pathlib import Path
#from selenium import webdriver

#driver = webdriver.Chrome()

def Quickstart():
    # if not os.path.isdir("credentials-sheets.json"):
    #     driver.get('https://developers.google.com/sheets/api/quickstart/python/')
    #     #element = driver.find_element_by_id("sheets.googleapis.com")
    # else:
    #     pass
    cwd = os.getcwd()
    json_file = '/credentials.json'
    downloads_path = str(Path.home() / "Downloads")
    file = downloads_path + json_file
    file_exists = os.path.exists(file)
    #new_file = downloads_path + "/credentials-sheets.json"
    current_directory = cwd + "/credentials-sheets.json"
    if file_exists == True:
         os.rename(file, current_directory)

    #print(downloads_path + "credentials-sheets.json")

Quickstart()