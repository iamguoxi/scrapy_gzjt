# -*- coding: utf-8 -*-
from date import TOTAL_NUMS
from query import QUERY

total_num = 0
for k, v in(TOTAL_NUMS.items()):
    total_num = total_num + v
total_num2 = 0
for k, v in(QUERY.items()):
    total_num2 = total_num2 + 1
if total_num == total_num2:
    print("match: ", total_num)
else:
    print("not match: ", total_num, total_num2)