"""12. 例外処理 — try / except"""

# --- 基本的な例外処理 ---
print("=== 基本的な例外処理 ===")

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"  [except] ゼロ除算: {e}")
        return None
    except TypeError as e:
        print(f"  [except] 型エラー: {e}")
        return None
    else:
        print(f"  [else]   例外なし: {a}/{b} = {result}")
        return result
    finally:
        print(f"  [finally] 常に実行される")

safe_divide(10, 3)
print()
safe_divide(10, 0)
print()
safe_divide(10, "a")

# --- カスタム例外 ---
print("\n=== カスタム例外 ===")

class RobotError(Exception):
    """ロボット制御の基底例外"""
    pass

class MotorOverheatError(RobotError):
    """モーター過熱"""
    def __init__(self, motor_id: int, temperature: float):
        self.motor_id = motor_id
        self.temperature = temperature
        super().__init__(f"Motor {motor_id} overheated: {temperature}°C")

try:
    raise MotorOverheatError(motor_id=3, temperature=105.2)
except MotorOverheatError as e:
    print(f"  捕捉: {e}")
    print(f"  モーターID: {e.motor_id}")
    print(f"  温度: {e.temperature}°C")

# --- 例外の連鎖: raise from ---
print("\n=== 例外の連鎖 ===")

def parse_data(raw: str) -> int:
    try:
        return int(raw)
    except ValueError as e:
        raise RobotError(f"データ解析失敗: {raw!r}") from e

try:
    parse_data("abc")
except RobotError as e:
    print(f"  RobotError: {e}")
    print(f"  原因: {e.__cause__}")
