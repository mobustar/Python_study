"""2. 基本データ型"""

# --- int: 任意精度 ---
big = 10 ** 50
print(f"10^50 = {big}")
print(f"桁数: {len(str(big))}")

# --- float: 浮動小数点の注意点 ---
print(f"0.1 + 0.2 = {0.1 + 0.2}")          # 0.30000000000000004
print(f"0.1 + 0.2 == 0.3 → {0.1 + 0.2 == 0.3}")  # False

# --- bool は int のサブクラス ---
print(f"True + True = {True + True}")       # 2
print(f"True * 10 = {True * 10}")           # 10
print(f"issubclass(bool, int) = {issubclass(bool, int)}")

# --- ミュータブル vs イミュータブル ---
# str はイミュータブル → 変更すると新しいオブジェクトが生成される
s1 = "hello"
s2 = s1
s1 = s1 + " world"
print(f"s1 = {s1!r}")       # 'hello world'（新しいオブジェクト）
print(f"s2 = {s2!r}")       # 'hello'（元のまま）

# list はミュータブル → 変更が参照元にも反映される
list1 = [1, 2, 3]
list2 = list1              # 同じリストへの参照
list1.append(4)
print(f"list1 = {list1}")  # [1, 2, 3, 4]
print(f"list2 = {list2}")  # [1, 2, 3, 4]（同じオブジェクトなので変わる）
