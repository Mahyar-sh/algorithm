def gcd(a, b):
    big = 0
    small = 0
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a

    residue = big % small
    if residue > 0:
        gcd(small, residue)
    else:
        print(small)


v = input()
a = int(v.split(' ')[0])
b = int(v.split(' ')[1])
gcd(a, b)
