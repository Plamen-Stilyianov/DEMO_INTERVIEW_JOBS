import asyncio
from time import sleep, perf_counter
from concurrent.futures import ProcessPoolExecutor


def heavy_work(i: int) -> int:
    """CPU intensive function"""
    sleep(1.0)
    return i


async def main():
    start = perf_counter()
    loop = asyncio.get_event_loop()

    with ProcessPoolExecutor() as pool:
        r1, r2 = await asyncio.gather(
            loop.run_in_executor(pool, heavy_work, 1),
            loop.run_in_executor(pool, heavy_work, 2),
        )

        print(r1, r2)

    elapsed = perf_counter() - start
    print(f"Time: {elapsed:.2f} s")


if __name__ == "__main__":
    asyncio.run(main())