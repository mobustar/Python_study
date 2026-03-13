"""22. ウォルラス演算子 — :="""

import re

# --- 基本: 式の中で代入する ---
print("=== 基本的な使い方 ===")

# 通常の書き方
data = [1, 5, 12, 3, 18, 7, 25, 2]
filtered = []
for x in data:
    doubled = x * 2
    if doubled > 10:
        filtered.append(doubled)
print(f"  通常: {filtered}")

# ウォルラス演算子で簡潔に
filtered2 = [y for x in data if (y := x * 2) > 10]
print(f"  := :  {filtered2}")

# --- whileループでの活用 ---
print("\n=== while ループ ===")

# 通常の書き方
import io
stream = io.StringIO("line1\nline2\nline3\n")
print("  通常:")
line = stream.readline().strip()
while line:
    print(f"    {line}")
    line = stream.readline().strip()

# ウォルラス演算子で簡潔に
stream = io.StringIO("line1\nline2\nline3\n")
print("  := :")
while line := stream.readline().strip():
    print(f"    {line}")

# --- 正規表現でのマッチ ---
print("\n=== 正規表現 ===")

texts = [
    "error: file not found",
    "warning: low battery",
    "info: system ready",
    "error: motor overheated",
]

for text in texts:
    if m := re.match(r"error: (.+)", text):
        print(f"  エラー検出: {m.group(1)}")

# --- リスト処理での中間結果保持 ---
print("\n=== 中間結果の保持 ===")

import math
values = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]

# sqrt が 1.5 以上のものだけを変換後の値で収集
results = [s for x in values if (s := math.sqrt(x)) >= 1.5]
print(f"  元の値: {values}")
print(f"  sqrt >= 1.5: {[f'{r:.3f}' for r in results]}")

# --- 条件式での活用 ---
print("\n=== 条件分岐での活用 ===")

def get_sensor_data():
    """センサーデータを返す（Noneの場合もある）"""
    return {"temperature": 42.5, "unit": "°C"}

if (data := get_sensor_data()) is not None:
    print(f"  データ取得: {data}")
else:
    print("  データなし")

# --- any / all との組み合わせ ---
print("\n=== any() との組み合わせ ===")

numbers = [2, 4, 6, 8, 15, 10]
# 最初の奇数を見つける
found = None
if any((found := x) and x % 2 != 0 for x in numbers):
    print(f"  最初の奇数: {found}")
