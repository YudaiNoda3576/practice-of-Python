x = -10

# インデントを入れる（４つが望ましい）
if x < 10:
    print('negative')
elif x == 0:
    print('ZERO')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

y = [1, 2, 3, 4, 5]
x = 1

if x in y:
    print('in')

if x not in y:
    print('not in')

# 値が入っていない判定をするテクニック
is_ok = [1, 2, 3, 4, 5]
# lengthを使う必要ない
# どんな型でも中身が無ければFalseとなる
if len(is_ok) > 0:
    print('Ok')
else:
    print('NG')

if is_ok:
    print('OK')
else:
    print('NG')
# PythonではNULLはnoneが入る
is_empty = None
# ==は使用しないこと
# isはオブジェクト比較
if is_empty is None:
    print('None')
# while文
count = 0
# while count < 5:
#     print(count)
#     count += 1

while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1
else:
    print('Done')

# input関数
# while True:
#     word = input('Entre:')
#     if word == 100:
#         break
#     print('next')
# for文
some_list = [1, 2, 3, 4, 5]
for i in some_list:
    print(i)

greeting = ['My', 'name', 'is', 'Yudai', 'Noda']
for word in greeting:
    if word == 'Noda':
        break
    elif word == 'Yudai':
        continue
    else:
        print(word)

# range関数
for i in range(10):
    print(i)
# 第一引数にスタート値を入れられる
for j in range(2, 10):
    print(j)
# 第三引数に何個飛ばしでカウントするかを入れられる
# 文字を繰り返し出力するみたいなことも可能
for k in range(2, 10, 3):
    print('hello')
# iteratorを使用しない場合は_で明示する
for _ in range(2, 10, 3):
    print('hello')

# enumerate関数
i = 0
fruits = ['banana', 'apple', 'orange']
for fruit in fruits:
    print(i, fruit)
    i += 1
# ↓同じ
for fruit in enumerate(fruits):
    print(i, fruit)

# zip関数
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'apple', 'orange']
drinks = ['coffee', 'juice', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])
# ↓同じ
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# dictionaryをforループ処理
d = {'x': 100, 'y': 200}

# listの中にtuple型のキー・バリューがセットで格納された値が返却される
# 頻出
print(d.items())
for v in d.items():
    print(k, ':', v)

# 位置引数のタプル化
# *argsでスプレッド構文みたいに使える


def say_something(word, *args):
    print(word, args)


say_something('Hi!', 'Mike', 'Nancy')

# キーワード引数の辞書化


def menu(**kwargs):
  # 辞書形式で値が保存される
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


# menu(entree='beef', drink='beer')
d = {
    'entree': 'beef',
    'drink': 'beer',
    'desert': 'ice'
}
# 辞書型で記述して、引数に渡すという方法は可読性が向上するので使われる
menu(**d)
# 位置引数とタプル化、辞書化は全てまとめて行うことが可能
# 一つめのアスタリスクを先に書かないとエラーとなる


def menu2(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)


menu2('banana', 'apple', 'orange', entree='beef', drink='coffee')

# Docstrings


def sample_func(param1, param2):
    """
    ここのドキュメントが出力されます
    """
    print(param1)
    print(param2)
    return True


# 以下のどちらかで見れる
print(sample_func.__doc__)
help(sample_func)

# inner関数


def outer(a, b):
    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)


outer(1, 2)
# クロージャ


def outer(a, b):
    def inner():
        return a + b

    return inner


# この時点ではinnerオブジェクトが返ってくるが、実行はされない
f = outer(1, 2)
# fに格納した関数を実行して始めてinner関数の処理が行われる
r = f()
print(r)


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area


# このように外側の関数の引数は最初の段階で固定し、
ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.14592)
# 細かい円周率で計算するか否かのように、用途に応じて使い分ける
print(ca1(10))
print(ca2(10))

# デコレ―ター
# 関数の前後に何か処理を行いたいOR関数に処理を付け加えたい時に使える


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

# アノテーションでデコレ―ターを呼び出すことが可能
# アノテーションをふたつ付けることが可能
# 順序によって処理が変わる


@print_info
@print_more
def add_num(a, b):
    return a + b


# print('start')
# r = add_num(10, 20)
# print('end')

f = print_info(add_num)
r = f(10, 20)
print(r)

# ラムダ
sample_list = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words(words, func):
    for word in words:
        print(func(word))


# def sample_func(word):
#     return word.capitalize()

def sample_func(word): return word.capitalize()


# functionを引数とするものは引数の中で定義すればコード量の削減につなげられる
change_words(sample_list, sample_func)
change_words(sample_list, lambda word: word.capitalize())

# ジェネレータ
# for文のように一度の処理で全てのループを抜けてしまうのではなく、
# yieldごとのデータを保持するので、途中に処理を挟むなどの用途に使用することが可能
# l = ['Good morning', 'Good afternoon', 'Good evening']

# for i in l:
#     print(i)

# print('#########')


def counter(num=10):
    for _ in range(num):
        yield 'run'

# 重い処理がyieldの途中に挟まっている場合等に小分けに処理を行うことが可能


def greetin():
    yield 'Good mornig'
    # for i in range(100000):
    #     print(i)
    yield 'Good afternoon'
    # for i in range(100000):
    # print(i)
    yield 'Good evening'


g = greetin()
c = counter()
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print('@@@@@@@@@@')
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))

print('@@@@@@@@@@')

print(next(g))

# リスト内包表記
t = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)
r = []

for i in t:
    r.append(i)

print(r)
# メモリの節約、処理の高速化
r = [i for i in t if i % 2 == 0]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

r = [i * j for i in t for j in t2]
print(r)
# 辞書包括表記
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'juice']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)

# ジェネレータ内包表記


def g():
    for i in range(10):
        yield i


g = g()
print(type(g))
print(next(g))

g = (i for i in range(10))
# tupleと間違えないように
g = tuple(i for i in range(10))

# 名前空間とスコープ
animal = 'cat'


def f():
    # ローカル変数を参照するので未定義になる
    # グローバル変数のアニマルを書き換える場合は
    global animal
    animal = 'dog'
    print('local:', animal)


f()
print('global:', animal)

# 例外処理
l = [1, 2, 3]
i = 5

try:
    l[i]
except IndexError as ex:
    print("Don't Worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print("other:{}".format(ex))
# 正常実行出来た場合にelse句に処理が入っていく
else:
    print('done')
finally:
    print("例外出してるんじゃねーよ！！！")
# 独自例外の作成


class UpperCaseError(Exception):
    pass


def check():
    words = ['apple', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UpperCaseError(word)


try:
    check()
except UpperCaseError as exc:
    print("This is my fault. Go next")
