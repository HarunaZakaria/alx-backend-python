import asyncio
import random

async def wait_n(n: int, max_delay: int) -> list:
    delays = []
    tasks = []
    for i in range(n):
        delay = random.uniform(0, max_delay)
        task = asyncio.create_task(sleep_and_return_delay(i, delay, delays))
        tasks.append(task)
    await asyncio.gather(*tasks)
    return delays

async def sleep_and_return_delay(i: int, delay: float, delays: list) -> None:
    await asyncio.sleep(delay)
    delays.append(delay)
    print(f"Task {i} slept for {delay:.2f} seconds")
    return None
