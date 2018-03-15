def add(n):
    return lambda x: x+n


add_one = add(1)
print(add_one(3))
