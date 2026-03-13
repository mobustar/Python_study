"""6. ループ — for / while"""

# --- 基本のforループ ---
print("=== for ループ ===")
for fruit in ["apple", "banana", "cherry"]:
    print(f"  {fruit}")

# --- range ---
print("\n=== range ===")
print(f"  range(5)       → {list(range(5))}")
print(f"  range(2, 10, 3)→ {list(range(2, 10, 3))}")

# --- enumerate ---
print("\n=== enumerate ===")
colors = ["red", "green", "blue"]
for i, color in enumerate(colors):
    print(f"  [{i}] {color}")

# --- zip ---
print("\n=== zip ===")
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 92]
ages = [20, 22, 21]
for name, score, age in zip(names, scores, ages):
    print(f"  {name}(age={age}): {score}点")

# --- while ---
print("\n=== while ===")
count = 5
while count > 0:
    print(f"  カウントダウン: {count}")
    count -= 1
print("  発射！")

# --- break / continue ---
print("\n=== break / continue ===")
for i in range(10):
    if i == 3:
        continue         # 3をスキップ
    if i == 7:
        break            # 7で終了
    print(f"  i = {i}")

# --- for-else（素数判定）---
print("\n=== for-else（素数判定）===")
for n in range(2, 20):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        # breakされずにループ完了 → 素数
        print(f"  {n} は素数")
