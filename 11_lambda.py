"""11. lambda式"""

# --- 基本 ---
print("=== 基本的なlambda ===")
square = lambda x: x ** 2
print(f"  square(5) = {square(5)}")

add = lambda a, b: a + b
print(f"  add(3, 4) = {add(3, 4)}")

# --- ソートのキー関数 ---
print("\n=== ソートのキー関数 ===")
students = [("Alice", 90), ("Bob", 85), ("Charlie", 92), ("Diana", 88)]
print(f"  元:       {students}")

# スコアで降順ソート
students.sort(key=lambda s: s[1], reverse=True)
print(f"  スコア順: {students}")

# 名前でソート
students.sort(key=lambda s: s[0])
print(f"  名前順:   {students}")

# --- map / filter ---
print("\n=== map / filter ===")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled = list(map(lambda x: x * 2, nums))
print(f"  map(x*2):     {doubled}")

odds = list(filter(lambda x: x % 2 != 0, nums))
print(f"  filter(奇数):  {odds}")

# --- 内包表記のほうが推奨される ---
print("\n=== 内包表記との比較 ===")
result_map = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
result_comp = [x ** 2 for x in nums if x % 2 == 0]
print(f"  map/filter:  {result_map}")
print(f"  内包表記:    {result_comp}")  # 同じ結果だが読みやすい

# --- sorted の応用 ---
print("\n=== sorted の応用 ===")
data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
sorted_data = sorted(data, key=lambda d: d["age"])
for d in sorted_data:
    print(f"  {d['name']}: {d['age']}歳")
