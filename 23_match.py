"""23. match文 — 構造的パターンマッチング（Python 3.10以降）"""

from dataclasses import dataclass

# --- 基本的なパターンマッチング ---
print("=== 基本的なmatch文 ===")

def handle_command(command: str):
    match command.split():
        case ["quit"]:
            return "終了します"
        case ["move", direction]:
            return f"{direction} に移動"
        case ["move", direction, distance]:
            return f"{direction} に {distance}m 移動"
        case ["set", key, value]:
            return f"{key} を {value} に設定"
        case _:
            return f"不明なコマンド: {command!r}"

commands = ["quit", "move forward", "move left 10", "set speed 100", "fly"]
for cmd in commands:
    print(f"  {cmd!r:25s} → {handle_command(cmd)}")

# --- リテラルパターン ---
print("\n=== リテラルパターン ===")

def http_status(code: int):
    match code:
        case 200:
            return "OK"
        case 301:
            return "Moved Permanently"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return f"Unknown ({code})"

for code in [200, 301, 404, 500, 418]:
    print(f"  {code} → {http_status(code)}")

# --- ガード条件（if）---
print("\n=== ガード条件 ===")

def classify_number(n):
    match n:
        case 0:
            return "ゼロ"
        case x if x > 0 and x < 10:
            return f"1桁の正の数 ({x})"
        case x if x > 0:
            return f"大きな正の数 ({x})"
        case x:
            return f"負の数 ({x})"

for n in [0, 5, 42, -7]:
    print(f"  {n:3d} → {classify_number(n)}")

# --- シーケンスパターン ---
print("\n=== シーケンスパターン ===")

def analyze_list(lst):
    match lst:
        case []:
            return "空のリスト"
        case [x]:
            return f"要素1つ: {x}"
        case [x, y]:
            return f"要素2つ: {x}, {y}"
        case [first, *rest]:
            return f"先頭: {first}, 残り: {rest}"

test_lists = [[], [42], [1, 2], [1, 2, 3, 4, 5]]
for lst in test_lists:
    print(f"  {str(lst):20s} → {analyze_list(lst)}")

# --- マッピング（辞書）パターン ---
print("\n=== マッピングパターン ===")

def process_message(msg: dict):
    match msg:
        case {"type": "error", "code": code, "message": text}:
            return f"エラー [{code}]: {text}"
        case {"type": "data", "values": [first, *rest]}:
            return f"データ: 先頭={first}, 残り{len(rest)}件"
        case {"type": str() as t}:
            return f"未知のタイプ: {t}"
        case _:
            return "不明なメッセージ"

messages = [
    {"type": "error", "code": 404, "message": "Not Found"},
    {"type": "data", "values": [10, 20, 30, 40]},
    {"type": "info", "detail": "ok"},
    {"foo": "bar"},
]
for msg in messages:
    print(f"  {msg}")
    print(f"    → {process_message(msg)}")

# --- クラスパターン ---
print("\n=== クラスパターン ===")

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Circle:
    center: Point
    radius: float

@dataclass
class Rectangle:
    top_left: Point
    width: float
    height: float

def describe_shape(shape):
    match shape:
        case Point(x=0, y=0):
            return "原点"
        case Point(x, y) if x == y:
            return f"対角線上の点 ({x}, {y})"
        case Point(x, y):
            return f"点 ({x}, {y})"
        case Circle(center=Point(0, 0), radius=r):
            return f"原点中心の円 (半径 {r})"
        case Circle(center=c, radius=r):
            return f"円 (中心=({c.x},{c.y}), 半径={r})"
        case Rectangle(top_left=p, width=w, height=h):
            return f"矩形 ({p.x},{p.y}) {w}x{h}"

shapes = [
    Point(0, 0),
    Point(3, 3),
    Point(1, 2),
    Circle(Point(0, 0), 5),
    Circle(Point(3, 4), 2),
    Rectangle(Point(1, 1), 10, 5),
]
for s in shapes:
    print(f"  {s!r:45s} → {describe_shape(s)}")

# --- OR パターン ---
print("\n=== OR パターン ===")

def day_type(day: str):
    match day.lower():
        case "saturday" | "sunday":
            return "週末"
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "平日"
        case _:
            return "不明"

for d in ["Monday", "Saturday", "Wednesday", "Sunday"]:
    print(f"  {d:10s} → {day_type(d)}")
