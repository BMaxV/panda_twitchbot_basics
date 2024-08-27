"""Example using zmq with asyncio coroutines"""

# Copyright (c) PyZMQ Developers.
# This example is in the public domain (CC-0)

import asyncio
import time

import zmq
from zmq.asyncio import Context, Poller

url = 'tcp://127.0.0.1:5555'

ctx = Context.instance()

async def sender() -> None:
    """send a message every second"""
    tic = time.time()
    push = ctx.socket(zmq.PUSH)
    push.bind(url)
    while True:
        print("sending")
        push.send_multipart(["switch".encode('ascii')])
        await asyncio.sleep(5)

#async def main() -> None:
    #tasks = [asyncio.create_task(coroutine()) for coroutine in [sender]]
    #await asyncio.wait(tasks)


if __name__ == "__main__":
    asyncio.run(sender())
