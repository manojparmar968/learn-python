import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
# print(sys.path.insert(0, abspath(join(dirname(__file__), '..'))))
from one import one
print("fsagfjsagfjasgfjasg")

actualpath = one.paths()
print(actualpath)
