from pathtub import add_to_path, remove_from_path
from py_setenv import setenv
import sys, os
import shutil


def up():
    print("This operation will add this folder (" + sys.path[0]+ "/.fastcmd) into environment variable."
          "If you are not confident enough about this, you can set it manually. Are you sure to continue? [Y/n]")
    op = input().strip()
    if (op == 'n' or op == 'N'):
        print("Canceled.")
    else:
        print('Setting...')
        add_to_path(sys.path[0] + "/.fastcmd", mode='user')
        setenv('FASTCMD_HOME', sys.path[0] + "/.fastcmd", user=True, suppress_echo=True)
        print('Done. You may need to restart your computer to start the service.')


def down():
    print("This operation will remove this folder (" + sys.path[0] + "/.fastcmd) from environment path variable. "
          "If you are not confident enough about this, you can remove it manually. Are you sure to continue? [Y/n]")
    op = input().strip()
    if (op == 'n' or op == 'N'):
        print("Canceled.")
    else:
        print('Setting...')
        remove_from_path(sys.path[0] + "/.fastcmd", mode='user')
        setenv('FASTCMD_HOME', user=True, delete=True, suppress_echo=True)
        print('Done.')


def add(name, cmd):
    cmd = cmd.replace('?/', os.getcwd() + '/')
    cmd = cmd.replace('?\\', os.getcwd() + '\\')
    cmd = cmd.replace('\'', '\"')
    shutil.copy(sys.path[0] + '/src/base.exe', sys.path[0] + '/.fastcmd/' + name + '.exe')
    with open(sys.path[0] + '/.fastcmd/' + name + '.txt', mode='w+') as f:
        f.write(cmd)



if __name__ == '__main__':
    up()