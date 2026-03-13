"""16. 特殊メソッド（マジックメソッド）"""

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float):
        return self.__mul__(scalar)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __abs__(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __getitem__(self, index: int) -> float:
        if index == 0: return self.x
        if index == 1: return self.y
        raise IndexError(f"index {index} out of range")

    def __len__(self) -> int:
        return 2

    def __bool__(self) -> bool:
        return self.x != 0 or self.y != 0

    def __call__(self, scale: float):
        """インスタンスを関数のように呼べる"""
        return Vector2D(self.x * scale, self.y * scale)

# --- 演算 ---
print("=== 算術演算 ===")
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
print(f"  v1 = {v1}")
print(f"  v2 = {v2}")
print(f"  v1 + v2 = {v1 + v2}")
print(f"  v1 - v2 = {v1 - v2}")
print(f"  v1 * 3  = {v1 * 3}")
print(f"  3 * v1  = {3 * v1}")      # __rmul__ が呼ばれる

# --- abs ---
print(f"\n=== abs / len / bool ===")
print(f"  abs(v1)  = {abs(v1)}")     # 5.0（3-4-5の直角三角形）
print(f"  len(v1)  = {len(v1)}")
print(f"  bool(v1) = {bool(v1)}")

zero = Vector2D(0, 0)
print(f"  bool({zero}) = {bool(zero)}")

# --- インデックスアクセス ---
print(f"\n=== __getitem__ ===")
print(f"  v1[0] = {v1[0]}")
print(f"  v1[1] = {v1[1]}")

# --- __call__ ---
print(f"\n=== __call__ ===")
scaled = v1(10)    # v1.__call__(10)
print(f"  v1(10) = {scaled}")

# --- 比較 ---
print(f"\n=== __eq__ ===")
print(f"  Vector2D(1,2) == Vector2D(1,2): {Vector2D(1,2) == Vector2D(1,2)}")
print(f"  Vector2D(1,2) == Vector2D(3,4): {Vector2D(1,2) == Vector2D(3,4)}")
