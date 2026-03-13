"""14. 継承とポリモーフィズム"""

from abc import ABC, abstractmethod

# --- 抽象基底クラス ---
class Sensor(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def read(self) -> float:
        ...

    def __str__(self):
        return f"Sensor({self.name})"

# --- サブクラス ---
class LidarSensor(Sensor):
    def __init__(self, name: str, max_range: float):
        super().__init__(name)
        self.max_range = max_range

    def read(self) -> float:
        return 3.5  # ダミー値

class IMUSensor(Sensor):
    def read(self) -> float:
        return 0.02  # ダミー値

class CameraSensor(Sensor):
    def __init__(self, name: str, resolution: tuple):
        super().__init__(name)
        self.resolution = resolution

    def read(self) -> float:
        return 30.0  # FPS

# --- ポリモーフィズム ---
print("=== ポリモーフィズム ===")
sensors: list[Sensor] = [
    LidarSensor("rplidar", max_range=12.0),
    IMUSensor("bno055"),
    CameraSensor("webcam", resolution=(640, 480)),
]
for s in sensors:
    print(f"  {s.name}: {s.read()}")

# --- 抽象クラスの直接インスタンス化はエラー ---
print("\n=== 抽象クラスのインスタンス化 ===")
try:
    Sensor("test")
except TypeError as e:
    print(f"  エラー: {e}")

# --- 多重継承とMRO ---
print("\n=== 多重継承とMRO ===")

class A:
    def who(self):
        return "A"

class B(A):
    def who(self):
        return "B"

class C(A):
    def who(self):
        return "C"

class D(B, C):
    pass

d = D()
print(f"  D().who() = {d.who()!r}")
print(f"  MRO: {' → '.join(cls.__name__ for cls in D.__mro__)}")

# --- isinstance / issubclass ---
print("\n=== isinstance / issubclass ===")
lidar = LidarSensor("test", 10.0)
print(f"  isinstance(lidar, Sensor):       {isinstance(lidar, Sensor)}")
print(f"  isinstance(lidar, LidarSensor):  {isinstance(lidar, LidarSensor)}")
print(f"  issubclass(LidarSensor, Sensor): {issubclass(LidarSensor, Sensor)}")
