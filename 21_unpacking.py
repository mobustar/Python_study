"""21. アンパックと可変長引数"""

# --- 基本のアンパック ---
print("=== 基本のアンパック ===")
first, second, third = [10, 20, 30]
print(f"  first={first}, second={second}, third={third}")

# --- * でまとめて受け取る ---
print("\n=== * アンパック ===")
first, *rest = [1, 2, 3, 4, 5]
print(f"  first={first}, rest={rest}")

first, *middle, last = [1, 2, 3, 4, 5]
print(f"  first={first}, middle={middle}, last={last}")

*head, last = [1, 2, 3, 4, 5]
print(f"  head={head}, last={last}")

# --- ネストしたアンパック ---
print("\n=== ネストしたアンパック ===")
data = ("Alice", (90, 85, 92))
name, (math, english, science) = data
print(f"  {name}: 数学={math}, 英語={english}, 理科={science}")

# --- 関数呼び出し時のアンパック ---
print("\n=== 関数呼び出し時のアンパック ===")

def setup(host, port, protocol):
    print(f"  {protocol}://{host}:{port}")

# リストを位置引数に展開
args = ["localhost", 8080, "https"]
print("  *args:")
setup(*args)

# 辞書をキーワード引数に展開
kwargs = {"host": "db.example.com", "port": 5432, "protocol": "tcp"}
print("  **kwargs:")
setup(**kwargs)

# --- リストの結合 ---
print("\n=== リスト/集合の展開 ===")
a = [1, 2, 3]
b = [4, 5, 6]
combined = [*a, *b, 7, 8]
print(f"  [*a, *b, 7, 8] = {combined}")

set_a = {1, 2, 3}
set_b = {3, 4, 5}
combined_set = {*set_a, *set_b}
print(f"  {{*set_a, *set_b}} = {combined_set}")

# --- 辞書のマージ（Python 3.9以降）---
print("\n=== 辞書のマージ ===")
default = {"color": "red", "size": 10, "weight": 1}
custom = {"size": 20, "weight": 5}

# ** で展開してマージ
merged_old = {**default, **custom}
print(f"  **展開: {merged_old}")

# | でマージ（Python 3.9以降）
merged_new = default | custom
print(f"  |演算子: {merged_new}")

# |= で破壊的マージ
config = {"debug": False, "verbose": True}
config |= {"debug": True, "log_level": "INFO"}
print(f"  |=演算子: {config}")

# --- アンパックの実用例 ---
print("\n=== 実用例: 座標の入れ替え ===")
points = [(1, 2), (3, 4), (5, 6)]
x_coords, y_coords = zip(*points)   # zip + アンパック
print(f"  points = {points}")
print(f"  x座標 = {x_coords}")
print(f"  y座標 = {y_coords}")
