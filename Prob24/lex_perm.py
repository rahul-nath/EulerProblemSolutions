import itertools
# store 0 - 9 in array
arr = ['0','1','2','3','4','5','6','7','8','9']
# use python permutations method to get all the possible permutations
iterations = [''.join(x) for x in itertools.permutations(arr)]
print iterations[999999]
# get millionth element
