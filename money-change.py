def change_money(m):
    cn = 0
    s = [10, 5, 1]
    while m > s[len(s) - 1]:
        i = 0
        while i <= len(s) - 1:

            while  m / s[i] >= 1:
                m = m - s[i]
                cn = cn + 1

            i = i + 1

    return cn


p = input()

print(change_money(int(p)))
