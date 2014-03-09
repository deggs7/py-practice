#!/usr/bin/python  
import random

def get_randata(num):
    a = []
    i = 0
    while i < num:
        a.append(random.randint(0, 20))
        i+=1
    return a

