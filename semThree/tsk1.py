import time

lst = []
for _ in range(100):
    lst.append(time.time_ns())

tmp = set(lst)