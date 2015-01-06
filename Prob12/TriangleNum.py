import math, time

t0 = time.clock()
def make_tris():
    t = 1
    for d in range(2, 100000):
        total = 0
        for i in range(1, int(math.sqrt(t))+1):
            if t % i == 0:
                total += 2
        if math.sqrt(t) * math.sqrt(t) == t:
            total -= 1
        if total >= 500:
            print t
            print time.clock() - t0
            return
        t += d

make_tris()
