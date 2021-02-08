



def count():
    c = 0
    while True:
        v = yield c
        if v == 0:
            return c
        c += v

def mediador():
    while True:
        yield from count()



def client():
    coro = mediador()
    next(coro)
    for i in range(-10, 1):
        c = coro.send(i*-1)
        print(c)


client()