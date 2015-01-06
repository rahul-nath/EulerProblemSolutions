fibs ={0:0, 1:1}
for i in range(2, 100000):
    fibs[i] = fibs[i-1] + fibs[i-2]
    if len(str(fibs[i])) >= 1000:
        print i
        break
# probably could do it using a reduce function coupled with a list comprehension, but who cares, it's 3am
