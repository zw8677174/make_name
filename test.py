from service.PoemNameService import PoemNameService
from service.PoetryNameService import PoetryNameService
from random import *

key = randint(0, 10)

if key == 9 :
    ret = PoemNameService.get()
else:
    ret = PoetryNameService.get()

print(ret['content'])
print(ret['sentence'])
print(ret['name'])
