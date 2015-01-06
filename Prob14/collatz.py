import time
# check the dictionary each time
# if the stored value isn't -1, then add that stored value to the current count

stored_lengths = {num: -1 for num in range(1, 1000000)}

def collatz():
    stored_lengths[1] = 4
    for i in range(2, 1000000):
        num = i
        total = 0
        while num != 1:
            if num < 1000000 and stored_lengths[num] != -1:
                total += stored_lengths[num]
                break
            else:
                if num % 2 == 0:
                    num = num/2
                else:
                    num = 3*num + 1
                total += 1
        stored_lengths[i] = total
    print max(stored_lengths, key=stored_lengths.get)

t0 = time.clock()
collatz()
print time.clock() - t0
