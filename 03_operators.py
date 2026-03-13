"""3. 演算子"""

# --- 算術演算子 ---
print("=== 算術演算子 ===")
print(f"10 / 3  = {10 / 3}")      # 3.333...（常にfloat）
print(f"10 // 3 = {10 // 3}")     # 3（切り捨て）
print(f"10 % 3  = {10 % 3}")      # 1（剰余）
print(f"2 ** 10 = {2 ** 10}")     # 1024（べき乗）

# --- == と is の違い ---
print("\n=== == と is の違い ===")
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(f"a == b: {a == b}")        # True（値が同じ）
print(f"a is b: {a is b}")        # False（別のオブジェクト）
print(f"a is c: {a is c}")        # True（同じオブジェクト）

# --- None の比較には is を使う ---
x = None
print(f"x is None: {x is None}")  # True

# --- 比較の連鎖 ---
print("\n=== 比較の連鎖 ===")
score = 75
print(f"score = {score}")
print(f"60 <= score < 80: {60 <= score < 80}")  # True

# --- 論理演算子の短絡評価 ---
print("\n=== 短絡評価 ===")
print(f'0 or "default"    → {"default"!r}')     # 0は偽 → 右辺を返す
print(f'"hello" and 42    → {42}')               # "hello"は真 → 右辺を返す
print(f'"" or "fallback"  → {"fallback"!r}')     # ""は偽 → 右辺を返す
print(f'None or 100       → {None or 100}')      # Noneは偽 → 右辺を返す

# --- ビット演算子 ---
print("\n=== ビット演算子 ===")
a, b = 0b1100, 0b1010
print(f"a     = {a:04b} ({a})")
print(f"b     = {b:04b} ({b})")
print(f"a & b = {a & b:04b} ({a & b})")    # AND
print(f"a | b = {a | b:04b} ({a | b})")    # OR
print(f"a ^ b = {a ^ b:04b} ({a ^ b})")    # XOR
print(f"a << 2= {a << 2:08b} ({a << 2})")  # 左シフト
