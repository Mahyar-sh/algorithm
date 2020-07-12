def lcm(a, b):
    big = 0
    small = 0
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a

    m = 1
    r = (big * m) % small
    while r != 0:
        m = m + 1
        r = (big * m) % small

    print(m * big)


v = input()
a = int(v.split(' ')[0])
b = int(v.split(' ')[1])
lcm(a, b)
