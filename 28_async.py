"""28. 非同期処理 — async / await"""

import asyncio
import time

# --- 基本的なコルーチン ---
print("=== 基本的なコルーチン ===")

async def say_hello(name: str, delay: float):
    """指定秒数後に挨拶する"""
    print(f"  [{name}] 開始...")
    await asyncio.sleep(delay)   # I/O待ちをシミュレート
    print(f"  [{name}] 完了! ({delay}秒)")
    return f"Hello, {name}!"

async def demo_basic():
    result = await say_hello("Alice", 0.5)
    print(f"  戻り値: {result}")

asyncio.run(demo_basic())

# --- gather: 並行実行 ---
print("\n=== asyncio.gather（並行実行）===")

async def fetch_sensor(sensor_id: int, delay: float) -> dict:
    """センサーデータを非同期に取得"""
    print(f"  センサー{sensor_id}: 取得開始")
    await asyncio.sleep(delay)
    print(f"  センサー{sensor_id}: 取得完了")
    return {"id": sensor_id, "value": sensor_id * 10.5}

async def demo_gather():
    start = time.perf_counter()

    # 3つのセンサーを並行取得
    results = await asyncio.gather(
        fetch_sensor(1, 0.3),
        fetch_sensor(2, 0.5),
        fetch_sensor(3, 0.2),
    )
    elapsed = time.perf_counter() - start

    print(f"\n  結果:")
    for r in results:
        print(f"    {r}")
    print(f"  合計時間: {elapsed:.2f}秒（逐次なら1.0秒かかるところ）")

asyncio.run(demo_gather())

# --- 逐次実行との比較 ---
print("\n=== 逐次 vs 並行の比較 ===")

async def demo_sequential():
    start = time.perf_counter()

    # 逐次実行: 1つずつ待つ
    r1 = await fetch_sensor(1, 0.3)
    r2 = await fetch_sensor(2, 0.3)
    r3 = await fetch_sensor(3, 0.3)

    elapsed = time.perf_counter() - start
    print(f"  逐次実行: {elapsed:.2f}秒")

async def demo_concurrent():
    start = time.perf_counter()

    # 並行実行: 全部同時に待つ
    r1, r2, r3 = await asyncio.gather(
        fetch_sensor(1, 0.3),
        fetch_sensor(2, 0.3),
        fetch_sensor(3, 0.3),
    )

    elapsed = time.perf_counter() - start
    print(f"  並行実行: {elapsed:.2f}秒")

print("逐次:")
asyncio.run(demo_sequential())
print("\n並行:")
asyncio.run(demo_concurrent())

# --- 非同期ジェネレータ ---
print("\n=== 非同期ジェネレータ（async for）===")

async def sensor_stream(count: int, interval: float):
    """非同期にデータを逐次生成"""
    for i in range(count):
        await asyncio.sleep(interval)
        yield {"id": i, "value": i * 1.5}

async def demo_async_for():
    async for data in sensor_stream(5, 0.1):
        print(f"  受信: {data}")

asyncio.run(demo_async_for())

# --- 非同期コンテキストマネージャ ---
print("\n=== 非同期コンテキストマネージャ（async with）===")

class AsyncConnection:
    def __init__(self, name: str):
        self.name = name

    async def __aenter__(self):
        print(f"  [{self.name}] 接続確立中...")
        await asyncio.sleep(0.1)
        print(f"  [{self.name}] 接続完了")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"  [{self.name}] 切断中...")
        await asyncio.sleep(0.1)
        print(f"  [{self.name}] 切断完了")

async def demo_async_with():
    async with AsyncConnection("DB") as conn:
        print(f"  [{conn.name}] データ操作中...")
        await asyncio.sleep(0.1)

asyncio.run(demo_async_with())

# --- create_task: バックグラウンドタスク ---
print("\n=== create_task（バックグラウンド処理）===")

async def background_job(name: str, count: int):
    """バックグラウンドで定期的に動作するタスク"""
    for i in range(count):
        await asyncio.sleep(0.15)
        print(f"  [BG:{name}] ステップ {i+1}/{count}")
    return f"{name} 完了"

async def demo_tasks():
    # タスクを生成（即座にスケジュールされる）
    task1 = asyncio.create_task(background_job("監視", 3))
    task2 = asyncio.create_task(background_job("記録", 3))

    # メイン処理（タスクと並行して実行）
    print("  [メイン] 処理開始")
    await asyncio.sleep(0.2)
    print("  [メイン] 処理中...")
    await asyncio.sleep(0.2)
    print("  [メイン] 処理完了")

    # タスクの完了を待つ
    result1 = await task1
    result2 = await task2
    print(f"  結果: {result1}, {result2}")

asyncio.run(demo_tasks())

# --- タイムアウト ---
print("\n=== asyncio.wait_for（タイムアウト）===")

async def slow_operation():
    await asyncio.sleep(5.0)
    return "完了"

async def demo_timeout():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=0.5)
        print(f"  結果: {result}")
    except asyncio.TimeoutError:
        print("  タイムアウト! (0.5秒で打ち切り)")

asyncio.run(demo_timeout())

# --- セマフォ（同時実行数の制限）---
print("\n=== セマフォ（同時実行数制限）===")

async def limited_task(semaphore, task_id):
    async with semaphore:
        print(f"  タスク{task_id}: 実行中（同時最大2）")
        await asyncio.sleep(0.2)
        print(f"  タスク{task_id}: 完了")

async def demo_semaphore():
    sem = asyncio.Semaphore(2)   # 同時実行数を2に制限
    tasks = [limited_task(sem, i) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(demo_semaphore())
