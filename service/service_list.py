from config import *
import os

def list(g, l):
    if g:
        print_list(name_list(False), False)
    if l:
        print_list(name_list(True), True)


def print_list(name_list, is_local):
    output = []
    for name in name_list:
        with open(f'{"./.fastcmd/" if is_local else (file_path + "/.fastcmd/")}{name}.txt') as f:
            output.append((name, f.read()))
    print(f'{"Local" if is_local else "Global"} shortcut:')
    for i in output:
        print(f'---\t{i[0]:<20}  {i[1]}')


def name_list(is_local):
    if is_local:
        dic = './.fastcmd'
    else:
        dic = file_path + '/.fastcmd'
    dict_list = []
    output = []
    for i in os.walk(dic):
        dict_list = i[2]
    for i in dict_list:
        if len(i) > 4 and i[-4:] == '.exe':
            output.append(i[:-4])
    return output