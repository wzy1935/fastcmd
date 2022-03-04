intro = '''
    =@@@@@@`   ,@@@^    ,@@@@@@`=@@@@@@@@^  ]@@@@@@^ =@@@^    =@@@` .@@@@@@@@`       
    @@^       /@/@@^   /@@         @@^    /@@[      ,@@@@^   @@@@/  /@/   ,@@@       
   /@@]]]`   @@` @@^   @@@@]      =@@    /@/        @@^@@^ ,@/=@@  =@@     @@/       
  ,@@[[[[  ,@@\]]@@^    ,\@@@^   .@@^   =@@.       =@/ @@^/@^ @@^  @@^    /@@        
  @@^     /@@[[[[@@^ ,    =@@`   /@/    =@@^      ,@@  @@@@` /@/  /@/   ]@@/         
 =@@     @@/     @@^,@@@@@@/    =@@      \@@@@@@  @@^  @@/  =@@. =@@@@@@/`           
'''
import sys

import argparse
from service import service_service, service_build, service_set, service_unset, service_list, service_explain


def func_service(args):
    if args.manage == 'up':
        service_service.up()
    if args.manage == 'down':
        service_service.down()

def func_build(args):
    if args.manage == 'up':
        service_build.up()
    if args.manage == 'down':
        service_build.down()

def func_set(args):
    if args.place == 'global':
        service_set.set(False, args.shortcut, args.command_prefix)
    if args.place == 'local':
        service_set.set(True, args.shortcut, args.command_prefix)

def func_unset(args):
    if args.place == 'global':
        service_unset.unset(False, args.shortcut)
    if args.place == 'local':
        service_unset.unset(True, args.shortcut)

def func_list(args):
    if args.place == 'global':
        service_list.list(True, False)
    if args.place == 'local':
        service_list.list(False, True)
    if args.place == 'all':
        service_list.list(True, True)

def func_explain(args):
    service_explain.explain(args.command)




parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# service
parser_1 = subparsers.add_parser("service")
parser_1.add_argument('manage', choices=['up', 'down'], help='create or destroy the whole fastcmd service')
parser_1.set_defaults(func=func_service)

# build
parser_2 = subparsers.add_parser("build")
parser_2.add_argument('manage', choices=['up', 'down'], help='create or destroy local fastcmd service in this dictionary')
parser_2.set_defaults(func=func_build)

# set
parser_3 = subparsers.add_parser("set")
parser_3.add_argument('place', choices=['global', 'local'], help='set a new shortcut')
parser_3.add_argument("shortcut")
parser_3.add_argument("command_prefix")
parser_3.set_defaults(func=func_set)

# list
parser_4 = subparsers.add_parser("list")
parser_4.add_argument('place', choices=['global', 'local', 'all'], help='list all shortcuts')
parser_4.set_defaults(func=func_list)

# explain
parser_5 = subparsers.add_parser("explain")
parser_5.add_argument('command', help='display actual command it runs')
parser_5.set_defaults(func=func_explain)

# unset
parser_6 = subparsers.add_parser("unset")
parser_6.add_argument('place', choices=['global', 'local'], help='unset a shortcut')
parser_6.add_argument("shortcut")
parser_6.set_defaults(func=func_unset)


if __name__ == '__main__':
    args = parser.parse_args()
    if 'func' not in args:
        print(intro)
    else:
        args.func(args)