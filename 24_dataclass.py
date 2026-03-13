"""24. dataclass"""

from dataclasses import dataclass, field, asdict, astuple

# --- 基本の dataclass ---
print("=== 基本の dataclass ===")

@dataclass
class Pose:
    x: float
    y: float
    theta: float = 0.0
    tags: list[str] = field(default_factory=list)

p1 = Pose(1.0, 2.0)
p2 = Pose(1.0, 2.0, theta=0.5, tags=["start"])
p3 = Pose(1.0, 2.0)

# __repr__ が自動生成される
print(f"  p1 = {p1}")
print(f"  p2 = {p2}")

# __eq__ が自動生成される
print(f"  p1 == p3: {p1 == p3}")   # True（値が同じ）
print(f"  p1 == p2: {p1 == p2}")   # False

# --- asdict / astuple ---
print("\n=== asdict / astuple ===")
print(f"  asdict(p2)  = {asdict(p2)}")
print(f"  astuple(p1) = {astuple(p1)}")

# --- frozen=True（イミュータブル）---
print("\n=== frozen=True ===")

@dataclass(frozen=True)
class ImmutablePoint:
    x: float
    y: float

ip = ImmutablePoint(3, 4)
print(f"  ip = {ip}")

try:
    ip.x = 10
except AttributeError as e:
    print(f"  変更エラー: {e}")

# ハッシュ可能 → 辞書のキーやsetの要素として使える
point_set = {ImmutablePoint(0, 0), ImmutablePoint(1, 1), ImmutablePoint(0, 0)}
print(f"  set: {point_set}")   # 重複が除去される

# --- order=True（比較演算子の自動生成）---
print("\n=== order=True ===")

@dataclass(order=True)
class Student:
    gpa: float
    name: str = field(compare=False)   # ソート時に無視

students = [
    Student(3.5, "Alice"),
    Student(3.8, "Bob"),
    Student(3.2, "Charlie"),
    Student(3.8, "Diana"),
]
for s in sorted(students, reverse=True):
    print(f"  GPA {s.gpa}: {s.name}")

# --- __post_init__（初期化後の処理）---
print("\n=== __post_init__ ===")

@dataclass
class Vector3D:
    x: float
    y: float
    z: float
    magnitude: float = field(init=False)   # __init__ の引数にしない

    def __post_init__(self):
        """初期化後に大きさを自動計算"""
        self.magnitude = (self.x**2 + self.y**2 + self.z**2) ** 0.5

v = Vector3D(3, 4, 0)
print(f"  v = {v}")
print(f"  magnitude = {v.magnitude}")

# --- field の活用 ---
print("\n=== field の活用 ===")

@dataclass
class Config:
    name: str
    values: list[int] = field(default_factory=list)
    _internal: str = field(default="", repr=False)   # reprに表示しない

c1 = Config("sensor1")
c2 = Config("sensor2")
c1.values.append(100)
print(f"  c1 = {c1}")
print(f"  c2 = {c2}")   # c2.values は独立した空リスト

# --- slots=True（Python 3.10以降）---
print("\n=== slots=True ===")

@dataclass(slots=True)
class SlottedPoint:
    x: float
    y: float

sp = SlottedPoint(1.0, 2.0)
print(f"  sp = {sp}")

try:
    sp.z = 3.0   # slots により動的な属性追加は不可
except AttributeError as e:
    print(f"  属性追加エラー: {e}")

# --- 継承 ---
print("\n=== dataclass の継承 ===")

@dataclass
class Shape:
    color: str = "red"

@dataclass
class Circle(Shape):
    radius: float = 1.0

    @property
    def area(self):
        import math
        return math.pi * self.radius ** 2

c = Circle(color="blue", radius=5)
print(f"  c = {c}")
print(f"  面積 = {c.area:.2f}")
