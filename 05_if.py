"""5. 条件分岐 — if / elif / else"""

# --- 基本の条件分岐 ---
print("=== 成績判定 ===")
scores = [95, 82, 73, 55]
for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"  スコア {score} → 成績 {grade}")

# --- 条件式（三項演算子）---
print("\n=== 条件式（三項演算子）===")
for score in scores:
    status = "合格" if score >= 60 else "不合格"
    print(f"  スコア {score} → {status}")

# --- Falsy値の一覧 ---
print("\n=== Falsy値の判定 ===")
falsy_values = [False, None, 0, 0.0, "", [], {}, set()]
for val in falsy_values:
    print(f"  bool({str(val):>8}) → {bool(val)}")

# --- 空コレクションの判定（Pythonicな書き方）---
print("\n=== 空リスト判定 ===")
items = []
if not items:
    print("  リストは空です")
items.append("data")
if items:
    print(f"  リストにデータあり: {items}")
