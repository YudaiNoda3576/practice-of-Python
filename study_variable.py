import math
# 型定義は不要
num = 1.5
# 型指定も可能
num2: float = 2.5
name = "Yudai"
is_ok = True
pie = 3.1415151515
result = math.sqrt(25)
log = math.log2(10)
word = 'python'

# 型の出力も可能
print(num, type(num))
print(num2)
print(name)
print(is_ok)
# sepを指定することで,区切り文字を指定出来る
# endを指定することで改行コードなどを挟める
print('Hi', 'Mike', sep=',', end='\n')
print('Hi', 'Yudai', sep=',', end='\n')

print(2 + 2)
# 丸目処理
print(round(pie, 2))

print(result)

print(log)
# help関数を使用するとドキュメントを表示することが可能
# print(help(math))
# 改行コードを文字列として認識させたい場合「r」を記述する
print('C:\name\name2')
print(r'C:\name\name2')
# """"で改行設定にすることが可能
print('###########')
print("""
line1
line2
line3
""")
print('###########')
# ↑だと空白行が出来てしまうので、空白行を抜くために\を記載する
print('###########')
print("""\
line1
line2
line3\
""")
print('###########')
print('Hi' * 3)
print('###########')
print(word[0])
print(word[-1])
# スライス記法
print(word[0:2])
# 最初から最後までは省略可能
print(word[:2])
print(word[2:])
# lengthを出力するメソッド
n = len(word)
print(n)
print('###########')
# {} に代入することが出来る
str = 'a is {}'
print(str.format('test'))
str2 = 'a is {}{}{}'
print(str2.format(1, 2, 3))
str2 = 'a is {0}{1}{2}'
print(str2.format("I'm", 'Yudai', 'Noda'))
str3 = 'a is {prefix}{firstName}{familyName}'
print(str3.format(prefix="I'm", firstName='Yudai', familyName='Noda'))
print('###########')
# Python3.6からは以下の書き方で上記と同じ動作を実行できる。こっちの方が早い
a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. Watashi ha {family} {name}')
print('###########')
