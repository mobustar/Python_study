"""27. ディスクリプタ"""

# --- バリデーション付きディスクリプタ ---
print("=== バリデーション付きディスクリプタ ===")

class Validated:
    """範囲チェック付き属性"""
    def __init__(self, min_val: float, max_val: float):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        # クラス定義時に属性名が通知される
        self.name = name
        self.private_name = f"_{name}"
        print(f"  [__set_name__] {owner.__name__}.{name} を登録")

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self   # クラスからアクセスした場合はディスクリプタ自体を返す
        value = getattr(obj, self.private_name, None)
        return value

    def __set__(self, obj, value):
        if not self.min_val <= value <= self.max_val:
            raise ValueError(
                f"{self.name} は {self.min_val}〜{self.max_val} の範囲 (入力: {value})"
            )
        setattr(obj, self.private_name, value)

class MotorConfig:
    speed = Validated(0, 100)
    torque = Validated(0, 50)

print()
m = MotorConfig()
m.speed = 80
m.torque = 30
print(f"  speed = {m.speed}, torque = {m.torque}")

m.speed = 50
print(f"  speed 変更後 = {m.speed}")

try:
    m.speed = 150
except ValueError as e:
    print(f"  エラー: {e}")

try:
    m.torque = -10
except ValueError as e:
    print(f"  エラー: {e}")

# --- 型チェックディスクリプタ ---
print("\n=== 型チェックディスクリプタ ===")

class Typed:
    """型を強制するディスクリプタ"""
    def __init__(self, expected_type: type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.name = name
        self.private_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} には {self.expected_type.__name__} が必要 "
                f"(入力: {type(value).__name__})"
            )
        setattr(obj, self.private_name, value)

class SensorReading:
    name = Typed(str)
    value = Typed(float)
    timestamp = Typed(float)

s = SensorReading()
s.name = "temperature"
s.value = 25.3
s.timestamp = 1234567890.0
print(f"  {s.name}: {s.value} (t={s.timestamp})")

try:
    s.value = "not a number"
except TypeError as e:
    print(f"  エラー: {e}")

# --- データディスクリプタ vs 非データディスクリプタ ---
print("\n=== データ vs 非データディスクリプタ ===")

class NonDataDesc:
    """非データディスクリプタ: __get__ のみ"""
    def __get__(self, obj, objtype=None):
        return "非データディスクリプタの値"

class DataDesc:
    """データディスクリプタ: __get__ と __set__"""
    def __get__(self, obj, objtype=None):
        return "データディスクリプタの値"
    def __set__(self, obj, value):
        pass  # 何もしないが __set__ があるのがポイント

class Demo:
    non_data = NonDataDesc()
    data = DataDesc()

d = Demo()

# 非データディスクリプタはインスタンス __dict__ で上書きできる
d.__dict__["non_data"] = "インスタンスの値"
print(f"  非データ: {d.non_data}")   # インスタンスの値が優先

# データディスクリプタはインスタンス __dict__ より優先される
d.__dict__["data"] = "インスタンスの値"
print(f"  データ:   {d.data}")       # ディスクリプタの値が優先

# --- @property の正体 ---
print("\n=== @property はディスクリプタ ===")

class Example:
    @property
    def value(self):
        return 42

print(f"  type(Example.value) = {type(Example.value)}")
print(f"  hasattr __get__: {hasattr(Example.value, '__get__')}")
print(f"  hasattr __set__: {hasattr(Example.value, '__set__')}")
print(f"  → @property はデータディスクリプタ")
