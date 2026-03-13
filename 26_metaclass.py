"""26. メタクラス — metaclass"""

# --- クラスは type のインスタンス ---
print("=== クラスは type のインスタンス ===")

class MyClass:
    pass

print(f"  type(MyClass) = {type(MyClass)}")          # <class 'type'>
print(f"  type(42)      = {type(42)}")               # <class 'int'>
print(f"  type(int)     = {type(int)}")              # <class 'type'>
print(f"  isinstance(MyClass, type) = {isinstance(MyClass, type)}")

# --- type() でクラスを動的に生成 ---
print("\n=== type() でクラスを動的生成 ===")

# type(名前, 基底クラス, 属性辞書) でクラスを作れる
DynamicClass = type("DynamicClass", (), {
    "value": 42,
    "greet": lambda self: f"Hello from {self.__class__.__name__}!",
})

obj = DynamicClass()
print(f"  obj.value = {obj.value}")
print(f"  obj.greet() = {obj.greet()}")

# --- シングルトンメタクラス ---
print("\n=== シングルトンメタクラス ===")

class SingletonMeta(type):
    """クラスのインスタンスを1つに制限する"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"  [メタクラス] {cls.__name__} の新規インスタンス生成")
            cls._instances[cls] = super().__call__(*args, **kwargs)
        else:
            print(f"  [メタクラス] {cls.__name__} の既存インスタンスを返却")
        return cls._instances[cls]

class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {}

a = Config()
b = Config()
c = Config()
print(f"  a is b: {a is b}")   # True
print(f"  a is c: {a is c}")   # True

# --- 属性を自動変換するメタクラス ---
print("\n=== 属性変換メタクラス ===")

class UpperAttrMeta(type):
    """メソッド以外の属性名を大文字に変換する"""
    def __new__(mcs, name, bases, namespace):
        uppercase_attrs = {}
        for key, value in namespace.items():
            if key.startswith("__"):
                uppercase_attrs[key] = value   # 特殊属性はそのまま
            elif callable(value):
                uppercase_attrs[key] = value   # メソッドはそのまま
            else:
                uppercase_attrs[key.upper()] = value  # 属性名を大文字に
        return super().__new__(mcs, name, bases, uppercase_attrs)

class Settings(metaclass=UpperAttrMeta):
    host = "localhost"
    port = 8080
    debug = True

print(f"  Settings.HOST  = {Settings.HOST}")
print(f"  Settings.PORT  = {Settings.PORT}")
print(f"  Settings.DEBUG = {Settings.DEBUG}")

try:
    print(Settings.host)
except AttributeError as e:
    print(f"  Settings.host → {e}")

# --- __init_subclass__（メタクラスの軽量代替）---
print("\n=== __init_subclass__（プラグイン登録）===")

class Plugin:
    """サブクラスを自動登録する基底クラス"""
    registry: dict[str, type] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.registry[cls.__name__] = cls
        print(f"  [登録] {cls.__name__}")

class LidarPlugin(Plugin):
    pass

class CameraPlugin(Plugin):
    pass

class IMUPlugin(Plugin):
    pass

print(f"\n  登録済みプラグイン: {list(Plugin.registry.keys())}")

# --- クラス生成の流れ ---
print("\n=== クラス生成の流れ ===")

class TraceMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"  1. __new__:  クラス '{name}' を生成")
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

    def __init__(cls, name, bases, namespace):
        print(f"  2. __init__: クラス '{name}' を初期化")
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        print(f"  3. __call__: '{cls.__name__}()' が呼ばれた")
        instance = super().__call__(*args, **kwargs)
        print(f"  4. インスタンス生成完了")
        return instance

print("クラス定義時:")
class Traced(metaclass=TraceMeta):
    def __init__(self):
        print(f"  (Traced.__init__ 実行)")

print("\nインスタンス生成時:")
t = Traced()
