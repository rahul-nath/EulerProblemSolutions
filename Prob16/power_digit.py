import time
t0 = time.clock()
print sum(int(i) for i in str(2**1000))
print time.clock() - t0
