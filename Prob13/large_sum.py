import time
# read in each line
# take the last seven digits
# store the new seven-digit int in an array
# convert to a long
# once made, add each long together
# if the sum is greater than 1 billion at any point
#     convert the int to a string

with open('the_num.txt', 'rb') as f:
    nums = [num for num in f]

def some():
    total = long(0)
    for l in nums:
        print l
        total += long(l)
    print total
some()
