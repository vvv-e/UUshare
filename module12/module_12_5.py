# Домашнее задание по теме "Асинхронность на практике"
import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {i} шар")
    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    pash = asyncio.create_task(start_strongman('Pasha', 3))
    den = asyncio.create_task(start_strongman('Denis', 4))
    apol = asyncio.create_task(start_strongman('Apollon', 5))
    await pash
    await den
    await apol


asyncio.run(start_tournament())
