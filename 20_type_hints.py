"""20. 型ヒント — Type Hints"""

from typing import Optional, Callable, TypeVar, Generic, TypedDict

# --- 基本的な型ヒント ---
print("=== 基本的な型ヒント ===")

def add(a: int, b: int) -> int:
    return a + b

def greet(name: str, loud: bool = False) -> str:
    msg = f"Hello, {name}!"
    return msg.upper() if loud else msg

print(f"  add(3, 4) = {add(3, 4)}")
print(f"  greet('Alice') = {greet('Alice')}")
print(f"  greet('Bob', loud=True) = {greet('Bob', loud=True)}")

# --- Optional（Noneを取りうる値）---
print("\n=== Optional ===")

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

print(f"  find_user(1) = {find_user(1)!r}")
print(f"  find_user(9) = {find_user(9)!r}")

# --- Union: int | str（Python 3.10以降）---
print("\n=== Union (int | str) ===")

def double(value: int | str) -> int | str:
    if isinstance(value, int):
        return value * 2
    return value + value

print(f"  double(5) = {double(5)}")
print(f"  double('hi') = {double('hi')!r}")

# --- コレクション型 ---
print("\n=== コレクション型 ===")

def mean(values: list[float]) -> float:
    return sum(values) / len(values)

config: dict[str, int] = {"timeout": 30, "retries": 3}
coords: tuple[float, float, float] = (1.0, 2.0, 3.0)

print(f"  mean([1,2,3,4,5]) = {mean([1,2,3,4,5])}")
print(f"  config = {config}")
print(f"  coords = {coords}")

# --- TypedDict ---
print("\n=== TypedDict ===")

class SensorData(TypedDict):
    timestamp: float
    value: float
    unit: str

data: SensorData = {"timestamp": 1234567890.0, "value": 25.3, "unit": "°C"}
print(f"  data = {data}")

# --- Callable ---
print("\n=== Callable ===")

def apply_op(a: float, b: float, op: Callable[[float, float], float]) -> float:
    return op(a, b)

print(f"  apply_op(3, 4, add) = {apply_op(3, 4, lambda a, b: a + b)}")
print(f"  apply_op(3, 4, mul) = {apply_op(3, 4, lambda a, b: a * b)}")

# --- ジェネリクス ---
print("\n=== ジェネリクス ===")

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def __repr__(self) -> str:
        return f"Stack({self._items})"

stack: Stack[int] = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(f"  stack = {stack}")
print(f"  pop() = {stack.pop()}")
print(f"  peek() = {stack.peek()}")
print(f"  stack = {stack}")

# --- 型ヒントは実行時に強制されない ---
print("\n=== 型ヒントは実行時に強制されない ===")
result = add("hello", " world")     # 型が違ってもエラーにならない
print(f"  add('hello', ' world') = {result!r}")
print(f"  ※ 実行時エラーにはならないが、mypyで検出できる")
