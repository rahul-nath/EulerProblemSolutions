import math
# find divisible nums, sum as you go, store in array
# go through each num in array and sum if a == d[d[a]]

d = { i:0 for i in range(1, 100001) }

def nice_num():
    global d
    for i in range(1, 100001):
        for x in range(1, int(math.sqrt(i)) + 1):
            if i % x == 0:
                d[i] += (x + i/x)
            if x*x == i:
                d[i] -= x
    print sum(k for k,v in d.items() if k <= 10000 and k == d[d[k]])

nice_num()
    
