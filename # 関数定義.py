# 関数定義
def say_somthing():
    s = 'hi'
    return s


# 上から順にスクリプトが読み込まれる
# Pythonでは関数はfunction型
result = say_somthing()
print(result)


def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"


result = what_is_this('green')
print(result)


def add_num(a: int, b: int) -> int:
    return a + b


# 型を引数に宣言することが出来るが、Pythonはエラーとして認識しないので注意
# 今のところ型宣言は主流ではないらしい。。。。
r = add_num('1', '3')
print(r)

# 位置引数とデフォルト引数とキーワード引数

# デフォルト引数を渡すことが可能


def menu(entree='chicken', drink='whine', desert='chocolate'):
    print('entree:' + entree)
    print('drink:' + drink)
    print('desert:' + desert)


# デフォルト引数は上書きされる
# 位置引数とキーワード引数は混ぜて使うことも可能。順番が狂うとエラーになるよ
menu('beef', drink='beer')
# デフォルト引数の注意

# 空のリストやディクショナリ（参照渡しとなるもの）をデフォルト引数におくべきではない
# def test_func(x, l=[]):


def test_func(x, list=None):
  # このような形で空のリストを入れたいときは対応する
    if list is None:
        list = []
        list.append(x)
        return list


y = [1, 2, 3]
r = test_func(100, y)

y = [1, 2, 3]
r = test_func(200, y)
print(r)
# 空のリストに追加
r = test_func(100)
print(r)
# 参照渡しになるので、先ほどのリストに追加することになる
#
r = test_func(100)
print(r)
