#variables.py
a = 19245301
b = 4218520
c = 271
d = abs(c-b)
e = abs(b-a)
if d > e:
    print('''The greater one is d
             The rate of new cases is greater in 2020.''')
elif d == e:
    print('''d is equal to e
             The rates in 2020 and 2021 are the same.''')
elif d < e:
    print('''The greater one is d
             The rate of new cases is greater in 2020.''')

#Booleans
X = "I am Smiling! Tell me I am pretty and happy!"
Y = "Of course you are pretty and happy!"
W = X+ Y*5
print(W)
