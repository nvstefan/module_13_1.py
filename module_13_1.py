# Домашнее задание по теме
# "Асинхронность на практике"

# Задача "Асинхронные силачи":

import time
import asyncio

number_of_balls = 5

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(number_of_balls):
        delay = 1 / power
        await asyncio.sleep(delay)
        print(f'Силач {name} поднял {i + 1} шар' )
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task = [
           asyncio.create_task(start_strongman('Pasha', 3)),
           asyncio.create_task(start_strongman('Denis', 4)),
           asyncio.create_task(start_strongman('Apollon', 5))
           ]

    # Ожидаем завершение всех задач одновременно
    await asyncio.gather(*task)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(start_tournament())
    end = time.time()
    print(f"Working time = {round((end - start), 3)}")

