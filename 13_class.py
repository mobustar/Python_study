"""13. クラス — class"""

class Robot:
    """ロボットを表すクラス"""

    # クラス変数: 全インスタンスで共有
    total_count = 0

    def __init__(self, name: str, speed: float = 1.0):
        # インスタンス変数: 各インスタンス固有
        self.name = name
        self.speed = speed
        self._battery = 100.0         # 非公開（慣例）
        Robot.total_count += 1

    def move(self, distance: float) -> None:
        """指定距離を移動する"""
        cost = distance / self.speed
        self._battery = max(0, self._battery - cost)
        print(f"  {self.name} が {distance}m 移動（残バッテリー: {self._battery:.1f}%）")

    def __repr__(self) -> str:
        return f"Robot(name={self.name!r}, speed={self.speed})"

    def __str__(self) -> str:
        return f"ロボット「{self.name}」"

# --- インスタンス生成と操作 ---
print("=== インスタンス生成 ===")
r1 = Robot("Atlas", speed=2.0)
r2 = Robot("Spot", speed=5.0)
print(f"  str:  {r1}")
print(f"  repr: {repr(r1)}")

print("\n=== メソッド呼び出し ===")
r1.move(10)
r1.move(20)
r2.move(50)

print(f"\n=== クラス変数 ===")
print(f"  生成されたロボット数: {Robot.total_count}")

# --- クラスメソッド / スタティックメソッド ---
print("\n=== classmethod / staticmethod ===")

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter: float) -> "Circle":
        """ファクトリメソッド"""
        return cls(diameter / 2)

    @staticmethod
    def is_valid_radius(value: float) -> bool:
        return value > 0

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

c1 = Circle(5)
c2 = Circle.from_diameter(10)    # ファクトリメソッドで生成
print(f"  c1: 半径={c1.radius}, 面積={c1.area():.2f}")
print(f"  c2: 半径={c2.radius}, 面積={c2.area():.2f}")
print(f"  is_valid_radius(-1) = {Circle.is_valid_radius(-1)}")
print(f"  is_valid_radius(5)  = {Circle.is_valid_radius(5)}")
