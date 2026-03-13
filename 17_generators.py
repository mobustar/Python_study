"""17. イテレータとジェネレータ — yield"""

from itertools import islice

# --- イテレータクラス ---
print("=== イテレータクラス ===")

class Countdown:
    """カウントダウンするイテレータ"""
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print("  カウントダウン:", list(Countdown(5)))

# --- ジェネレータ関数 ---
print("\n=== ジェネレータ関数 ===")

def fibonacci():
    """無限フィボナッチ数列"""
    a, b = 0, 1
    while True:
        yield a                # ここで一時停止し、値を返す
        a, b = b, a + b       # 次の next() で再開

fib_10 = list(islice(fibonacci(), 10))
print(f"  フィボナッチ(10個): {fib_10}")

# --- 有限ジェネレータ ---
def squares_up_to(n):
    """n以下の平方数を生成"""
    i = 1
    while i * i <= n:
        yield i * i
        i += 1

print(f"  100以下の平方数: {list(squares_up_to(100))}")

# --- メモリ効率の比較 ---
print("\n=== メモリ効率 ===")
import sys

list_version = [x ** 2 for x in range(10000)]
gen_version = (x ** 2 for x in range(10000))

print(f"  リスト: {sys.getsizeof(list_version):,} bytes")
print(f"  ジェネレータ: {sys.getsizeof(gen_version):,} bytes")

# --- yield from ---
print("\n=== yield from ===")

def chain(*iterables):
    """複数のイテラブルを連結"""
    for it in iterables:
        yield from it

result = list(chain([1, 2], "AB", [10, 20]))
print(f"  chain([1,2], 'AB', [10,20]) = {result}")

# --- send() でジェネレータに値を送る ---
print("\n=== send() ===")

def accumulator():
    """送られた値を累積するジェネレータ"""
    total = 0
    while True:
        value = yield total     # 現在の合計を返し、send()の値を受け取る
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)              # 最初の yield まで進める
print(f"  send(10) → {acc.send(10)}")
print(f"  send(20) → {acc.send(20)}")
print(f"  send(5)  → {acc.send(5)}")

# --- ジェネレータでパイプライン ---
print("\n=== ジェネレータパイプライン ===")

def read_data():
    """データソース"""
    for i in [1, 5, 3, 8, 2, 9, 4, 7, 6]:
        yield i

def filter_even(data):
    """偶数のみ通す"""
    for x in data:
        if x % 2 == 0:
            yield x

def multiply(data, factor):
    """倍率をかける"""
    for x in data:
        yield x * factor

# パイプライン: データ → 偶数フィルタ → 10倍
pipeline = multiply(filter_even(read_data()), 10)
print(f"  結果: {list(pipeline)}")
