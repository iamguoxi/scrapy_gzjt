# -*- coding: utf-8 -*-
from query import QUERY

def get_first(l):
    for item in l:
        return item

item = get_first(QUERY)
length = len(item)
for i in range(length):
    print(i+1, '--------------')
    l = {}
    for j in range(10):
        l[j] = 0
    for k, v in(QUERY.items()):
        d = int(k[i])
        l[d] = l[d] + 1
    for k, v in(l.items()):
        print(k, v)
