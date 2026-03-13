"""10. 引数の種類"""

# --- デフォルト引数 ---
print("=== デフォルト引数 ===")
def connect(host, port=3306, timeout=30):
    print(f"  接続先: {host}:{port} (timeout={timeout}s)")

connect("localhost")
connect("db.example.com", port=5432)
connect("192.168.1.1", 8080, timeout=10)

# --- *args: 可変長位置引数 ---
print("\n=== *args ===")
def sum_all(*args):
    print(f"  args = {args}")   # タプルとして受け取る
    return sum(args)

print(f"  合計: {sum_all(1, 2, 3, 4, 5)}")

# --- **kwargs: 可変長キーワード引数 ---
print("\n=== **kwargs ===")
def print_config(**kwargs):
    print(f"  kwargs = {kwargs}")   # 辞書として受け取る
    for key, value in kwargs.items():
        print(f"    {key} = {value}")

print_config(speed=100, direction="forward", mode="auto")

# --- 引数の順序ルール: pos_only / normal / kw_only ---
print("\n=== 位置専用 / 通常 / キーワード専用 ===")
def func(pos_only, /, normal, *, kw_only):
    print(f"  pos_only={pos_only}, normal={normal}, kw_only={kw_only}")

func(1, 2, kw_only=3)            # OK: 位置 / 位置 / キーワード
func(1, normal=2, kw_only=3)     # OK: 位置 / キーワード / キーワード

try:
    func(pos_only=1, normal=2, kw_only=3)  # エラー
except TypeError as e:
    print(f"  エラー: {e}")

# --- ⚠ ミュータブルなデフォルト引数の罠 ---
print("\n=== ミュータブルなデフォルト引数の罠 ===")

# 悪い例
def bad_append(item, lst=[]):
    lst.append(item)
    return lst

print(f"  1回目: {bad_append(1)}")   # [1]
print(f"  2回目: {bad_append(2)}")   # [1, 2] ← 前回の結果が残る！

# 正しい例
def good_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(f"  1回目: {good_append(1)}")  # [1]
print(f"  2回目: {good_append(2)}")  # [2] ← 正しく独立
