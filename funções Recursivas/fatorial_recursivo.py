def fat(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fat(n-1)


n = int(input('digite um número:'))
res = fat(n)
print(res)