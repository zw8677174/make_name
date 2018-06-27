from service.PoemNameService import PoemNameService
from service.PoetryNameService import PoetryNameService


# ret = PoemNameService.get()
ret = PoetryNameService.get()
print(ret['content'])
print(ret['sentence'])
print(ret['name'])
