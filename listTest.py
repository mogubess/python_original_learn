

def testFunc():
    return False

#for 文をつかっていればそれはイテレータ
a = [12, 0.38, "abc", "DEF", 1000, {1:"orange"}, testFunc(), None, testFunc]
for i in a:
    print (i)

if all(a):
    print("list all ok")

if any(a):
    print("list any ok")

### イテレータの取得
#iterable = iter(a)
iterable = a.__iter__()
#iterable = a.__iter__()も同じ動作となる
print('list first value={}!!'.format(next(iterable)))
print(next(iterable))
### オブジェクトのClassを判定する、listなどでも使える
if isinstance(a,list) == True:
    print("list type")

### 長さの取得
# オブジェクトの長さ (要素の数) を返します。引数はシーケンス 
# (文字列、バイト列、タプル、リスト、range 等) かコレクション ]
# (辞書、集合、凍結集合等) です。
print('list length ={}!!'.format(len(a)))

### ファイルで呼び出すと一行ずつ読み込む
#for line in open("sample.txt"):
#   print(line)

### クラスにイテレータを作成してみた
class SampleIterator(object):
    def __init__(self, num):
        self.num = num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.num:
            raise StopIteration()

        ret = self.current
        self.current += 1
        return ret

### クラスでイテレータを作成
si = SampleIterator(3)
for si2 in si:
    print(si2)

### クラスは長さを持っていない
# print('Object(SampleIterator) length ={}!!'.format(len(si)))

############################################### __getitem(self, item)__
# Pythonの特殊メソッドのひとつで、オブジェクトに角括弧でアクセスしたときの挙動を定義できる。
# 
class Sample:
    def __getitem__(self, item):
        return item

b = Sample()
print(b["foo"]) # => foo
print(b[1]) # => 1