#pizza_party.py
n = 0
p = (n*n+n+2)/2
while p < 64:
    n = n + 1
    p = (n*n+n+2)/2
    print(p)
print('''when we have enough pieces for each member of the class,
         the number of straight cuts
         is at least: ''' ,
         str(n))
