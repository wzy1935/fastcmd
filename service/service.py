from pathtub import add_to_path, remove_from_path
from py_setenv import setenv
from config import *



def up():
    print("This operation will add this folder (" + file_path + "\\.fastcmd) into environment variable."
          "If you are not confident enough about this, you can set it manually. Are you sure to continue? [Y/n]")
    op = input().strip()
    if (op == 'n' or op == 'N'):
        print("Canceled.")
    else:
        print('Setting...')
        add_to_path(file_path + "\\.fastcmd", mode='user')
        setenv('FASTCMD_HOME', file_path + "\\.fastcmd", user=True, suppress_echo=True)
        print('Done. You may need to restart your computer to start the service.')


def down():
    print("This operation will remove this folder (" + file_path + "\\.fastcmd) from environment path variable. "
          "If you are not confident enough about this, you can remove it manually. Are you sure to continue? [Y/n]")
    op = input().strip()
    if (op == 'n' or op == 'N'):
        print("Canceled.")
    else:
        print('Setting...')
        remove_from_path(file_path + "\\.fastcmd", mode='user')
        setenv('FASTCMD_HOME', user=True, delete=True, suppress_echo=True)
        print('Done.')