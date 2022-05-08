#variables.py
a = 19245301
# a is the number of the total cases of COVID-19 in the UK utill 2022
b = 4218520
# b is the number of the total cases of COVID-19 in the UK utill 2021
c = 271
# c is the number of the total cases of COVID-19 in the UK utill 2020
#Now find the maximun cases in three years
#Because I need to print the year instead of number, the only way I knew is transferring to list to help
number = [a, b, c]
greatest = max(number)
year = [2022, 2021, 2020]
#Use the index correlation between two lists to print the year with the most cases we found
print("%d has the greatest number of cases of COVID-19" % (year[number.index(greatest)]))
#Make the number output formally
d = abs(c-b)
# d is the difference of the total cases of COVID-19 in the UK between 2021 and 2020
e = abs(b-a)
# e is the difference of the total cases of COVID-19 in the UK between 2022 and 2021
#Now compare the difference
if d > e:
    print("The difference of cases'amount between 2021 and 2020 is bigger than that between 2022 and 2021")
elif d == e:
    print("The difference of cases'amount between 2022 and 2021 is the same as that between 2021 and 2020")
elif d < e:
    print("The difference of cases'amount between 2022 and 2021 is bigger than that between 2021 and 2020")
#Now calculate the increasing rate for 2020-2021
rate1 = (b - c)/c
#Now calculate the increasing rate for 2021-2022
rate2 = (a - b)/b
#Now we can compare the difference between the increasing rates
if rate1 > rate2:
    print("The increasing rate of cases'amount for 2020-2021 is larger than that for 2021-2022")
elif d == e:
    print("The increasing rate of cases'amount for 2020-2021 is the same as that for 2021-2022")
elif d < e:
    print("The increasing rate of cases'amount for 2020-2021 is larger than that for 2021-2022")


#Booleans
X = True
Y = False
W = X or Y
print("W is", W)
W = X and Y
print("W is", W)


