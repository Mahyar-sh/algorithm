def calc(num):
    f = []
    f.insert(0, 0)
    f.insert(1, 1)
    i = 2
    while i < num + 1:
        f.insert(i, f[i - 1] + f[i - 2])
        i = i + 1

    return f[num]


n = int(input())
print(calc(n))
