import randata

def bubblesort(a):
    i = 0
    j = len(a) - 2
    while i < j:
        k = len(a) - 1
        while k > i:
            if (a[k] < a[k-1]):
                a[k-1], a[k] = a[k], a[k-1]
            k -= 1

        i += 1
    return a

print bubblesort(randata.get_randata(20))

