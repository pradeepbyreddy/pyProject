b = lambda x,y:x*y

print(b(2,3))


def tripler(n):
    return lambda a: a*n


triplet = tripler(b(2,3))

print(triplet(4))