"""8. 内包表記"""

# --- リスト内包表記 ---
print("=== リスト内包表記 ===")
squares = [x ** 2 for x in range(8)]
print(f"  二乗:     {squares}")

evens = [x for x in range(20) if x % 2 == 0]
print(f"  偶数:     {evens}")

# --- ネストした内包表記 ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [val for row in matrix for val in row]
print(f"  行列:     {matrix}")
print(f"  平坦化:   {flat}")

# --- if-else 付き ---
labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(6)]
print(f"  偶奇:     {labels}")

# --- 辞書内包表記 ---
print("\n=== 辞書内包表記 ===")
words = ["apple", "banana", "cherry", "date"]
word_len = {w: len(w) for w in words}
print(f"  文字数: {word_len}")

# キーと値の入れ替え
inverted = {v: k for k, v in word_len.items()}
print(f"  反転:   {inverted}")

# --- 集合内包表記 ---
print("\n=== 集合内包表記 ===")
lengths = {len(w) for w in words}
print(f"  ユニークな文字数: {lengths}")

# --- ジェネレータ式（メモリ効率が良い）---
print("\n=== ジェネレータ式 ===")
total = sum(x ** 2 for x in range(1_000_000))
print(f"  0〜999999の二乗の合計: {total}")
