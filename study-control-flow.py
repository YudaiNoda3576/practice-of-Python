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
