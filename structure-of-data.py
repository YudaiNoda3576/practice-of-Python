list = [1, 20, 3, 45, 67, 432]
print(list)
print(len(list))
print(type(list))
# listの要素を一つ飛ばしで取得する
print(list[::2])
# ネストした配列
a = [1, 2, 3, 4, 5]
n = ['野田', '山田', '本田', '木田', '和田']
x = [a, n]
print(x)
print('###########')
list2 = ['a', 'b', 'c', 'd', 'e']
list2[0] = 'x'
print(list2)
list2[2:5] = ['C', 'D', 'E']
print(list2)
list2[2:5] = []
print(list2)
list2[:] = []
print(list2)
print('###########')
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.append(100)
print(n)
n.insert(0, 200)
print(n)
n.pop(0)
print(n)
# 存在自体が消えるので注意が必要
# del n[0]
# こちらの方が安全
n.remove(2)
print(n)
print('###########')
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)
print('###########')
s = 'My name is Mike'
# 任意の文字列を引数の文字列を区切りとしてListに格納する
to_split = s.split(' ')
print(to_split)
# 分割した配列を元の文字列に成型する
x = ' '.join(to_split)
print(x)
print('###########')
i = [1, 2, 3, 4, 5]
# 参照渡しになるので、
# j = i
# copyメソッドを使用して値を渡してやること
j = i.copy()
print(i)
print(j)
print('###########')
# タプル型
# ()で囲う
sk = ('yudai', 'noda', 29)
# （）は省略可
sk2 = 'haruka', 'tonoike', 26
# 空のタプルは()省略不可
sk3 = ()
# tuple関数によって生成可能
mylist = ['yudainoda', 'harukatonoike', 'yurinoda']
sk4 = tuple(mylist)
print(sk)
print(sk2)
print(sk3)
print(sk4)
# インデックス番号を使用してアクセス可能
print(sk4[0])
# tupleはimmutableなのでエラーとなる
# sk4[0] = 'yoshionoda'
# tupleのパック・アンパック
# パック
mytuple = (1, 2, 3)
# アンパック
(x, y, z) = mytuple
min, max = 0, 100
i = 10
j = 20
tmp = i
i = j
print(x, y, z)
print(i, j)

a = 100
b = 200
print(a, b)
# 変数の入れ替えが簡単に出来る
a, b = b, a
print(a, b)
