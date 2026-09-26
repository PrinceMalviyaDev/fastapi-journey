import time
import asyncio

def task1():
    time.sleep(3)
    return "Done"

print(task1())

async def task2():
    await asyncio.sleep(3)
    return "Done"

# print(task2())

async def main():
    result = await task2()
    print(result)

asyncio.run(main())