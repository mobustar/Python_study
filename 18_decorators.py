"""18. デコレータ — @decorator"""

import time
import functools

# --- 基本のデコレータ ---
print("=== 実行時間計測デコレータ ===")

def timer(func):
    """関数の実行時間を計測する"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__}: {elapsed:.6f}秒")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

result = slow_sum(1_000_000)
print(f"  結果: {result}")

# --- ログ出力デコレータ ---
print("\n=== ログ出力デコレータ ===")

def log_call(func):
    """関数呼び出しをログ出力する"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join([repr(a) for a in args])
        kwargs_str = ", ".join([f"{k}={v!r}" for k, v in kwargs.items()])
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"  → {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"  ← {func.__name__} = {result!r}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

@log_call
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(3, 4)
greet("Alice", greeting="Hi")

# --- 引数付きデコレータ ---
print("\n=== 引数付きデコレータ（リトライ）===")

def retry(max_attempts: int = 3):
    """失敗時にリトライする"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  試行 {attempt}/{max_attempts}: {e}")
                    if attempt == max_attempts:
                        raise
        return wrapper
    return decorator

call_count = 0

@retry(max_attempts=3)
def flaky_function():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError("接続失敗")
    return "成功！"

result = flaky_function()
print(f"  結果: {result}")

# --- functools.wraps の効果 ---
print("\n=== functools.wraps の効果 ===")
print(f"  slow_sum.__name__ = {slow_sum.__name__!r}")   # wrapsがないと "wrapper"

# --- デコレータの積み重ね ---
print("\n=== デコレータの積み重ね ===")

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"_{func(*args, **kwargs)}_"
    return wrapper

@bold
@italic
def message(text):
    return text

# 適用順: message → italic → bold（下から上）
print(f"  {message('Hello')}")   # **_Hello_**

# --- lru_cache（キャッシュデコレータ）---
print("\n=== functools.lru_cache ===")

@functools.lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(f"  fib(30) = {fib(30)}")
print(f"  キャッシュ情報: {fib.cache_info()}")
