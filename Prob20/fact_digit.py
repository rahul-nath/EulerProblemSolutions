import time
t0 = time.clock()
fact_arr = {0:1}
for i in range(1, 101):
    fact_arr[i] = i*fact_arr[i-1]
print sum(int(n) for n in str(fact_arr[100]))
print time.clock() - t0
