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
print(help(math))
