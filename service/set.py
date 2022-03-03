from config import *
import os, shutil


def set(is_local, shortcut, prefix):
    path = file_path
    if is_local: path = '.'
    prefix = prefix.replace('?/', os.getcwd() + '/')
    prefix = prefix.replace('?\\', os.getcwd() + '\\')
    prefix = prefix.replace('\'', '\"')
    shutil.copy(file_path + '/resource/base.exe', path + '/.fastcmd/' + shortcut + '.exe')
    with open(path + '/.fastcmd/' + shortcut + '.txt', mode='w+') as f:
        f.write(prefix)