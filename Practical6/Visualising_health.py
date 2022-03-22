#visualising the effect of paternal age on affspring health
#First make the lists into dictionary
paternal_age = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
chd = [1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94]#put in all the data
info = {}#this is the dictionary I want to make including all the data
for i in range(len(chd)):
    a = paternal_age[i]
    b = chd[i]
    info[a] = b#use a loop to add all the data in the dictionary accordingly
print(info)

#Make scatter plot
import matplotlib.pyplot as plt
x = paternal_age
y = chd#define x and y
plt.scatter(x, y, marker = "*", color = "green")#make plot
plt.title("the effect of paternal age on affspring health", color = "red")#define title
plt.xlabel("paternal age", color = "purple")
plt.ylabel("relative risk for congenital heart disease (CHD)", color = "purple")#define what will be shown for x axis and y axis
plt.xlim((25,80))
plt.ylim((1,2))#define the limitiation of x axis and y axis
plt.show()#show the plot

#For an input number of paternal_age, let us consider it as a random choice from paternal_age list
import random
m = random.choice(paternal_age)#choose a random age from paternal_age
n = chd[paternal_age.index(m)]#find the value in chd that has the same index as m in paternal_age
print("The relative data of congenital heart disease is %s for %d" %(n, m))#print the relative rate


