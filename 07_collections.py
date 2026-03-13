"""7. リスト・タプル・辞書・集合"""

# --- リスト ---
print("=== リスト ===")
nums = [5, 2, 8, 1, 9, 3]
print(f"  元のリスト: {nums}")

nums.append(7)
print(f"  append(7):  {nums}")

nums.sort()
print(f"  sort():     {nums}")

# スライス
print(f"  [1:4]:      {nums[1:4]}")
print(f"  [::2]:      {nums[::2]}")
print(f"  [::-1]:     {nums[::-1]}")

# --- タプル ---
print("\n=== タプル ===")
point = (10, 20)
x, y = point     # アンパック
print(f"  point = {point}, x = {x}, y = {y}")

single = (42,)    # 要素1つのタプルにはカンマが必要
not_tuple = (42)
print(f"  (42,) の型: {type(single).__name__}")
print(f"  (42)  の型: {type(not_tuple).__name__}")

# --- 辞書 ---
print("\n=== 辞書 ===")
user = {"name": "Alice", "age": 30, "city": "Tokyo"}
print(f"  user = {user}")
print(f"  user['name'] = {user['name']}")
print(f"  get('email', 'なし') = {user.get('email', 'なし')}")

user["email"] = "alice@example.com"
print(f"  キー追加後: {user}")

print("  items():")
for key, value in user.items():
    print(f"    {key}: {value}")

# --- 集合 ---
print("\n=== 集合 ===")
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(f"  a = {a}")
print(f"  b = {b}")
print(f"  a | b (和集合)   = {a | b}")
print(f"  a & b (積集合)   = {a & b}")
print(f"  a - b (差集合)   = {a - b}")
print(f"  a ^ b (対称差)   = {a ^ b}")

# 重複除去
dupes = [1, 2, 2, 3, 3, 3, 4]
print(f"\n  重複あり: {dupes}")
print(f"  重複除去: {list(set(dupes))}")
