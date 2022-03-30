import time
import asyncio

start = time.time()

# заготовить тесто а
# нарежем колбаску а
# замесим соус а
# натрем сыр а
# поставим в духовку
# нарезать свежую зелень
# посыпем свежей зеленью а



async def slice():
    await asyncio.sleep(1)

async def souce():
    await asyncio.sleep(5)


async def chezzy():
    await asyncio.sleep(1)


async def duhofka():
    await asyncio.sleep(4)


def slice_fresh():
    time.sleep(5)


async def fresh():
    await asyncio.sleep(1)


async def cook():
    # await asyncio.sleep(4)
    task3 = asyncio.create_task(cook)
    await task3
    await slice()
    await souce()
    await chezzy()
    await duhofka()
    slice_fresh()
    await fresh()


asyncio.run(cook())

print("Время исполнения", time.time() - start, "секунд")