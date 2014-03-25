
def b(n):
    rt = ''
    rt = []
    if n == 0:
        return '0'
    while n > 0:
        rt.append(str(n % 2))
        n = n/2
    rt.reverse()
    return ''.join(rt)

print b(4)
print b(5)
print b(3)
print b(1024)
print b(1)
print b(0)


