import asyncio
import itertools


async def spinner(text: str) -> None:
    for i in itertools.cycle(r"\|/-"):
        status = f"\r{i} {text}"
        print(status, end='', flush=True)

        try:
            await asyncio.sleep(0.21)
        except asyncio.CancelledError:
            break

    empty = ' ' * len(status)
    print(f"\r{empty}\r", end="")


async def long_comp() -> int:
    await asyncio.sleep(3)
    return 123123123


async def manager() -> int:
    task = asyncio.create_task(spinner("chel"))
    result = await long_comp()
    task.cancel()
    return result


def main() -> None:
    result = asyncio.run(manager())
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
