import threading
import time
import itertools


def spinner(text: str, event: threading.Event):
    for i in itertools.cycle(r"\|/-"):
        status = f"\r{i} {text}"
        print(status, end='', flush=True)
        if event.wait(.21):
            break
    empty = ' ' * len(status)
    print(f"\r{empty}\r", end="")


def long_computation() -> int:
    time.sleep(3)
    return 123123123


def manager() -> int:
    event = threading.Event()
    thread = threading.Thread(target=spinner, args=("ja dumaju", event))
    print(thread)
    thread.start()
    result = long_computation()
    event.set()
    thread.join()
    return result


def main() -> int:
    result = manager()
    print(f"Result: {result}")
    return result


if __name__ == "__main__":
    main()
