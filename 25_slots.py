"""25. スロット — __slots__"""

import sys

# --- 通常のクラス（__dict__ を使う）---
class PointDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# --- __slots__ を使ったクラス ---
class PointSlots:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

# --- メモリ使用量の比較 ---
print("=== メモリ使用量の比較 ===")
pd = PointDict(1, 2)
ps = PointSlots(1, 2)

print(f"  PointDict:  インスタンス {sys.getsizeof(pd)} bytes + __dict__ {sys.getsizeof(pd.__dict__)} bytes")
print(f"  PointSlots: インスタンス {sys.getsizeof(ps)} bytes（__dict__ なし）")

# 大量インスタンスでの比較
dict_points = [PointDict(i, i) for i in range(10000)]
slots_points = [PointSlots(i, i) for i in range(10000)]

dict_total = sum(sys.getsizeof(p) + sys.getsizeof(p.__dict__) for p in dict_points)
slots_total = sum(sys.getsizeof(p) for p in slots_points)

print(f"\n  10,000インスタンスの合計:")
print(f"    PointDict:  {dict_total:>10,} bytes")
print(f"    PointSlots: {slots_total:>10,} bytes")
print(f"    削減率:     {(1 - slots_total / dict_total) * 100:.1f}%")

# --- 動的な属性追加の制限 ---
print("\n=== 動的な属性追加 ===")

# __dict__ ありなら自由に追加できる
pd.z = 30
print(f"  PointDict: z = {pd.z} (動的追加OK)")

# __slots__ では宣言外の属性を追加できない
try:
    ps.z = 30
except AttributeError as e:
    print(f"  PointSlots: {e}")

# --- __dict__ の有無 ---
print("\n=== __dict__ の有無 ===")
print(f"  PointDict.__dict__  存在: {hasattr(pd, '__dict__')}")
print(f"  PointSlots.__dict__ 存在: {hasattr(ps, '__dict__')}")
print(f"  PointDict の属性一覧: {pd.__dict__}")

# --- slots と継承 ---
print("\n=== slots と継承 ===")

class Base:
    __slots__ = ("x",)
    def __init__(self, x):
        self.x = x

class Child(Base):
    __slots__ = ("y",)   # 親の slots に追加
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

c = Child(10, 20)
print(f"  Child: x={c.x}, y={c.y}")
print(f"  Base.__slots__  = {Base.__slots__}")
print(f"  Child.__slots__ = {Child.__slots__}")

try:
    c.z = 30
except AttributeError as e:
    print(f"  動的追加: {e}")

# --- slots + デフォルト値（Python 3.10 dataclass）---
print("\n=== dataclass(slots=True) ===")

from dataclasses import dataclass

@dataclass(slots=True)
class Particle:
    x: float
    y: float
    vx: float = 0.0
    vy: float = 0.0

p = Particle(1.0, 2.0, vx=0.5)
print(f"  Particle: {p}")
print(f"  __slots__ = {Particle.__slots__}")
