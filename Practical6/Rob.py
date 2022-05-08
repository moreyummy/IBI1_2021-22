#Rob
#sort the marks
marks = [45, 36, 86, 57, 53, 92, 65, 45]
marks.sort()#sort the mark
print(marks)#print the sorted marks

#calculate the mean of marks
import numpy as np
a = np.array(marks)
b = np.mean(a)
if b < 60:
    print("His average score is %s so he failed the ICA"%(b))
else:
    print("His average score is %s so he passed the ICA"%(b))

#make boxplot
from matplotlib import pyplot as plt
plt.boxplot(a, vert = True, whis = 1.5,  patch_artist = True, boxprops = {"color" : "red"}, showmeans = True, showbox = True, showcaps = True, showfliers = True, notch = False)#make boxplot and give requirements to the plot
plt.title("Rob's score distribution", color = "green")#define the title
plt.xlabel("Rob", color = "purple")#define what will be shown in x axis
plt.ylabel("score", color = "purple")#define what will be shown in y axis
plt.show()#show the plot


