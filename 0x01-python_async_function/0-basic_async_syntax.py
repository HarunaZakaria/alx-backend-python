#!/usr/bin/env python3

import random
import asyncio

async def wait_random(max_delay=10)-> float:
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
