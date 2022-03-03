import sys, os
sys.path.append('..')
from config import *

os.environ["A"] = '5'

os.system('set A="5"')