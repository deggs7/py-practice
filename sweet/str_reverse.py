s = 'abcdefg'

def r1(s):
    return s[::-1]

print "r1"
print r1(s)



def r2(s):
    r = list(s)
    r.reverse()
    return "".join(r)

print "r2"
print r2(s)



def r3(s):
    return reduce(lambda x, y : y + x, s)

print "r3"
print r3(s)


