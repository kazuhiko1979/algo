def g():
    for i in range(10):
        yield i

def g2():
    yield from g()
    yield from g()


print([i for i in g2()])
