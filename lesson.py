# import lesson_package.utils
from lesson_package import utils
# 非推奨↓
# from lesson_package.utils import say_twice
from lesson_package.talk import human
from lesson_package.talk import animal
# 同じ階層のモジュールをどうやって一括インポートするか？
# これも非推奨
# from lesson_package.talk import *

r = utils.say_twice('hello')
print(r)

print(animal.sing())
