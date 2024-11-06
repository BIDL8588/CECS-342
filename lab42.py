import asyncio

async def factorial(name, number):
    result = 1
    for i in range(1, number +1):
        result *= i
        print(f"Current task name: {name}, current factorial value {number}, current loop i = {i}")

        await asyncio.sleep(1)
    print(f"Task name:{name}, Final factorial value: {result}")
    return result

async def main():
    result = await asyncio.gather(factorial("A", 3),
                                  factorial("B", 4),
                                  factorial("C", 5))
    print(result)

asyncio.run(main())
