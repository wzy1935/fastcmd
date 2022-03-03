from config import *
import os, sys

def up():
    env = os.environ['Path']
    env = os.getcwd() + '\\.fastcmd;' + env
    if not os.path.exists('./.fastcmd'):
        os.mkdir('./.fastcmd')
    with open('./fastcmd_load.bat', mode='w+') as f:
        f.write(f'set Path={env}\n\nset FASTCMD_HOME={os.getcwd()}\\.fastcmd')

def down():
    os.remove('./.fastcmd')
    os.remove('./fastcmd_load.bat')