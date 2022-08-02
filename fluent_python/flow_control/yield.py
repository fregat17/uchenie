def cubes():
    res = 1
    while True:
        yield res*res*res
        res += 1


class cubes3:
    def __init__(self, max_nums):
        self.index = 1
        self.max_nums = max_nums

    def __iter__(self):
        while self.index < self.max_nums:
            yield self.index*self.index*self.index
            self.index += 1


def numbers(n):
    for i in range(n):
        yield i


def odd_or_not(n):
    for i in n:
        if i % 2:
            yield i


if __name__ == "__main__":
    for i in odd_or_not(numbers(100)):
        print(i)


