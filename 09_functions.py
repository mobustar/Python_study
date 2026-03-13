"""9. 関数定義 — def"""

# --- 基本的な関数 ---
def greet(name: str) -> str:
    """挨拶メッセージを返す"""
    return f"Hello, {name}!"

print("=== 基本的な関数 ===")
print(f"  {greet('Alice')}")
print(f"  {greet('Bob')}")

# --- 複数の戻り値（タプル）---
def divmod_custom(a, b):
    """商と余りを返す"""
    return a // b, a % b

print("\n=== 複数の戻り値 ===")
quotient, remainder = divmod_custom(17, 5)
print(f"  17 ÷ 5 = {quotient} あまり {remainder}")

# --- 関数はファーストクラスオブジェクト ---
print("\n=== 関数を変数に代入 ===")
say_hello = greet
print(f"  {say_hello('Charlie')}")

# --- 関数を引数に渡す ---
def apply(func, value):
    return func(value)

print(f"  apply(len, 'hello') = {apply(len, 'hello')}")

# --- スコープ: LEGB規則 ---
print("\n=== スコープ: LEGB規則 ===")
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(f"  inner:  x = {x!r}")
    inner()
    print(f"  outer:  x = {x!r}")

outer()
print(f"  global: x = {x!r}")

# --- global / nonlocal ---
print("\n=== global / nonlocal ===")
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
increment()
print(f"  global counter = {counter}")

def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = make_counter()
print(f"  nonlocal counter: {c()}, {c()}, {c()}")
