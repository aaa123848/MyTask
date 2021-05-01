def pipe(n, *fs):
    for f in fs:
        n = f(n)
    return n
