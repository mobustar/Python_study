"""1. 変数と代入"""

# --- 変数は「オブジェクトへの参照」 ---
x = 42
y = x
print(f"x = {x}, y = {y}")        # 同じオブジェクトを参照
print(f"x is y: {x is y}")        # True（同一オブジェクト）

x = "hello"
print(f"x = {x}, y = {y}")        # x だけ変わる。y は 42 のまま

# --- 多重代入 ---
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")

# --- スワップ ---
a, b = b, a
print(f"スワップ後: a={a}, b={b}")

# --- 型の確認 ---
values = [42, 3.14, True, "hello", None]
for v in values:
    print(f"  {str(v):>8} → {type(v).__name__}")
