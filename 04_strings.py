"""4. 文字列操作"""

# --- f文字列 ---
print("=== f文字列 ===")
name, age = "Alice", 30
print(f"名前: {name}, 年齢: {age}, 来年: {age + 1}")

# 書式指定
pi = 3.14159265
print(f"小数2桁: {pi:.2f}")
print(f"カンマ区切り: {1234567:,}")
print(f"パーセント: {0.856:.1%}")
print(f"16進数: {255:#x}")
print(f"2進数: {42:#010b}")
print(f"右寄せ: [{'hello':>15}]")
print(f"左寄せ: [{'hello':<15}]")
print(f"中央: [{'hello':^15}]")
print(f"ゼロ埋め: {42:05d}")

# --- strメソッド ---
print("\n=== strメソッド ===")
s = "  Hello, World!  "
print(f"strip()   → {s.strip()!r}")
print(f"split(',')→ {s.split(',')}")
print(f"upper()   → {s.upper()!r}")
print(f"replace() → {s.replace('World', 'Python')!r}")
print(f"find()    → {s.find('World')}")
print(f"startswith→ {s.strip().startswith('Hello')}")

# --- join ---
words = ["Python", "is", "awesome"]
print(f"join      → {' '.join(words)!r}")
print(f"CSV join  → {','.join(words)!r}")

# --- raw文字列 ---
print("\n=== raw文字列 ===")
normal = "改行は\nここ"
raw = r"改行は\nここ"
print(f"通常: {normal!r}")
print(f"raw:  {raw!r}")
