import time
import math
import asyncio
import concurrent.futures

def fibonacci(n):  # содержимое функции не менять
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')


# запускать с f, a, b, n равными соответственно math.sin, 0, math.pi, 20000000
def trapezoidal_rule(f, a, b, n):  # содержимое функции не менять
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')


async def sequence():
    start_time = time.perf_counter()
    await asyncio.gather(
        asyncio.to_thread(fibonacci, 700003),
        asyncio.to_thread(trapezoidal_rule, math.sin, 0, math.pi, 20000000)
    )
    end_time = time.perf_counter()
    print(f'sequence time: {end_time - start_time: 0.2f} \n')

async def threads():
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        tasks = [
            loop.run_in_executor(executor, fibonacci, 700003),
            loop.run_in_executor(executor, trapezoidal_rule, math.sin, 0, math.pi, 20000000)
        ]
        await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    print(f'threads time: {end_time - start_time: 0.2f} \n')

async def main():
    await sequence()
    await threads()

if __name__ == '__main__':
    asyncio.run(main())
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):

        fibonacci = 7
        trapezoidal_rule = 2.000000000000087
        sequence async time:  5.11
        
        trapezoidal_rule = 2.000000000000087
        fibonacci = 7
        threads async time:  5.23       
    """
