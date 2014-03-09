#-*- coding:utf-8 -*-

def bubble_sort(t):
    i = 0
    while i < (len(t) - 1):
        k = len(t) - 1
        while k > i:
            if (t[k-1]>t[k]):
                t[k-1], t[k] = t[k], t[k-1]
            k -= 1
        i += 1
    return t


def insert_sort_0(t):
    for i in range(1, len(t)):
        k = i - 1
        while k >= 0 and t[i] < t[k]:
            k -= 1
        t.insert(k+1, t[i])
        t.pop(i+1) # 插入后list多了一个元素
    return t


def insert_sort_1(arr):
    for i in range(1, len(arr)):
        x = arr[:i]
        t = arr[i]
        arr[:(i+1)] = m_inst(x, t)
    return arr

def m_inst(arr, t):
    if len(arr) == 1 and t > arr[0]:
        arr.insert(1, t)
    elif len(arr) == 1 and t <= arr[0]:
        arr.insert(0, t)
    else:
        m = (len(arr) / 2)
        if t < arr[m]:
            arr[:m] = m_inst(arr[:m], t)
        else:
            arr[m:] = m_inst(arr[m:], t)
    return arr
        

def shell_sort_0(arr):
    dist = len(arr)/2
    while dist > 0:
        for i in range(dist, len(arr)):
            j = i
            while j >= dist and arr[j] < arr[j-dist]:
                arr[j], arr[j-dist] = arr[j-dist], arr[j]
                j -= dist
        dist /= 2
    return arr

def shell_sort_1(arr):
    dist = len(arr)/2
    while dist > 0:
        for i in range(dist, len(arr)):
            tmp = arr[i]
            j = i
            while j >= dist and tmp < arr[j-dist]:
                arr[j] = arr[j-dist]
                j -= dist
            arr[j] = tmp
        dist /= 2
    return arr


