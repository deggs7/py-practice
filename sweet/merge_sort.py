a = [8, 2, 7, 9, 1, 3 ]
b = [73, 23, 34, 34, 7, 8, 3, 5, 4]

a.extend(b)
print a 

print sorted(set(a), key=a.index)

