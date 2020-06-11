import time
import os

def get_dir():
    cwd = os.getcwd()
    return cwd

def Setup_Dir():
    saved_dir = ''
    program_directory = open("directory.txt", "w")
    prog_dir = get_dir()
    #print('Program directory saved.')
    program_directory.write(prog_dir)
    program_directory.close()
    saved_dir = saved_dir + prog_dir
    time.sleep(0.5)
    #print('+------------------------------+')
    time.sleep(0.5)
    return saved_dir


if __name__ == '__main__':
    Setup_Dir()
