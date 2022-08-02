def tree(cls, level=0):
    yield cls.__name__, level
    for sub in cls.__subclasses__():
        yield from tree(sub, level + 1)


def traverse(cls):
    for name, i in tree(cls):
        print(" " * i + name)


if __name__ == "__main__":
    print(traverse(BaseException))
