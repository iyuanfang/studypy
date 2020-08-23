def generator(array):
    for i in array:
        yield i*i


gen = generator([1, 2, 3, 4, 5])
print(next(gen))
print(next(gen))
print(next(gen))
print("---------------")

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        print("bbb"+str(b))
        a, b = b, a + b
        n = n + 1



for n in fab(5):
    print(n)