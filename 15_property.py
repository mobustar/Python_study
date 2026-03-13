"""15. プロパティ — @property"""

class Motor:
    def __init__(self, max_rpm: int = 6000):
        self._rpm = 0
        self._max_rpm = max_rpm

    @property
    def rpm(self) -> int:
        """getter: motor.rpm でアクセス"""
        return self._rpm

    @rpm.setter
    def rpm(self, value: int) -> None:
        """setter: motor.rpm = 3000 で呼ばれる"""
        if not 0 <= value <= self._max_rpm:
            raise ValueError(f"RPMは0〜{self._max_rpm}の範囲")
        self._rpm = value

    @rpm.deleter
    def rpm(self) -> None:
        """deleter: del motor.rpm で呼ばれる"""
        print(f"  RPMをリセット（{self._rpm} → 0）")
        self._rpm = 0

    @property
    def speed_percent(self) -> float:
        """読み取り専用プロパティ（setterなし）"""
        return (self._rpm / self._max_rpm) * 100

# --- 使用例 ---
print("=== getter / setter ===")
m = Motor(max_rpm=6000)
m.rpm = 3000
print(f"  RPM: {m.rpm}")
print(f"  速度: {m.speed_percent:.1f}%")

m.rpm = 5500
print(f"  RPM: {m.rpm}")
print(f"  速度: {m.speed_percent:.1f}%")

# --- バリデーション ---
print("\n=== バリデーション ===")
try:
    m.rpm = 9999
except ValueError as e:
    print(f"  エラー: {e}")

# --- deleter ---
print("\n=== deleter ===")
del m.rpm
print(f"  RPM: {m.rpm}")

# --- 読み取り専用プロパティへの書き込み ---
print("\n=== 読み取り専用プロパティ ===")
try:
    m.speed_percent = 50
except AttributeError as e:
    print(f"  エラー: {e}")
