"""19. コンテキストマネージャ — with"""

import time
from contextlib import contextmanager

# --- クラスベース ---
print("=== クラスベースのコンテキストマネージャ ===")

class ManagedResource:
    """リソースの確保と解放を自動化"""
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f"  [enter]  {self.name} を確保")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"  [exit]   例外発生: {exc_val}")
        print(f"  [exit]   {self.name} を解放")
        return False   # Trueにすると例外を握りつぶす

# 正常系
with ManagedResource("データベース接続") as res:
    print(f"  [with]   {res.name} を使用中...")

# 例外発生時も __exit__ は呼ばれる
print()
try:
    with ManagedResource("ファイル") as res:
        print(f"  [with]   {res.name} を使用中...")
        raise RuntimeError("書き込みエラー")
except RuntimeError:
    print("  [catch]  例外を処理")

# --- contextlib.contextmanager ---
print("\n=== @contextmanager ===")

@contextmanager
def timer_context(label: str):
    """処理時間を計測する"""
    start = time.perf_counter()
    print(f"  [{label}] 開始")
    yield                    # ここで with ブロック本体が実行される
    elapsed = time.perf_counter() - start
    print(f"  [{label}] 完了: {elapsed:.4f}秒")

with timer_context("計算"):
    total = sum(range(1_000_000))
    print(f"  合計: {total}")

# --- 一時的に値を変更するコンテキストマネージャ ---
print("\n=== 一時的な値変更 ===")

class Config:
    debug = False

@contextmanager
def debug_mode(config):
    """一時的にデバッグモードをONにする"""
    original = config.debug
    config.debug = True
    print(f"  デバッグモード: ON")
    try:
        yield
    finally:
        config.debug = original
        print(f"  デバッグモード: OFF")

cfg = Config()
print(f"  debug = {cfg.debug}")   # False
with debug_mode(cfg):
    print(f"  debug = {cfg.debug}")   # True
print(f"  debug = {cfg.debug}")   # False

# --- 複数のコンテキストマネージャ ---
print("\n=== 複数のコンテキストマネージャ ===")

@contextmanager
def tag(name: str):
    print(f"  <{name}>")
    yield
    print(f"  </{name}>")

with tag("html"):
    with tag("body"):
        print("    Hello, World!")
