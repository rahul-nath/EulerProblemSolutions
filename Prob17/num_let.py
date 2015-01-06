# keep an array for the ones digits
# keep an array for the tens digits
# keep an array for the hundreds (including 'and')

# maybe just do len...
ones = [len("one"), len("two"), len("three"), len("four"), len("five"), len("six"), len("seven"), len('eight'), len('nine')] # 1...9
teens = [len('ten'), len('eleven'), len('twelve'), len('thirteen'), len('fourteen'), len('fifteen'), len('sixteen'), len('seventeen'), len('eighteen'), len('nineteen')] # 10...19
tens = [len('twenty'), len('thirty'), len('forty'), len('fifty'), len('sixty'), len('seventy'), len('eighty'), len('ninety')] # 20...90
hundreds = [len('onehundredand'), len('twohundredand'), len('threehundredand'), len('fourhundredand'), len('fivehundredand'), len('sixhundredand'), len('sevenhundredand'), len('eighthundredand'), len('ninehundredand')] # 100....900

total = sum(ones) + sum(teens) + sum(tens) + sum(hundreds) + len('onethousand') +  sum(x + y for x in tens for y in ones) + sum(x + y for x in hundreds for y in ones) + sum(x + y for x in hundreds for y in tens) + sum(x + y for x in hundreds for y in teens) + sum(x + y + z for x in hundreds for y in tens for z in ones) - 3*9
print total
