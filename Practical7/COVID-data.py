import os
import pandas as pd

os.chdir("C:/Users/LENOVO")
os.getcwd()
covid_data = pd.read_csv("full_data(2).csv")
print("The data in first and third columns from rows 10-20 are as follows:")
print(covid_data.iloc[10:21, [0, 2]])
total = [False, False, False, False, True, False]
afghanistan = covid_data[covid_data["location"].isin(["Afghanistan"])]
print("The data about total cases for all rows corresponding to Afghanistan are as follows:")
print(afghanistan.iloc[:, total])

china = covid_data[covid_data["location"].isin(["China"])]
china_new_data = china[['date', 'new_cases', 'new_deaths']]
import numpy as np
new_cases = np.array(china_new_data.new_cases)
mean1 = np.mean(new_cases)
print("The mean number of new cases corresponding to China is %d"%(mean1))
new_deaths = np.array(china_new_data.new_deaths)
mean2 = np.mean(new_deaths)
print("The mean number of new deaths corresponding to China vis %d"%(mean2))
from matplotlib import pyplot as plt
plt.subplot(221)
plt.boxplot(new_cases, vert = True, patch_artist = True, boxprops = {"color":"gray"}, flierprops={"marker":"*", "markerfacecolor":"red"}, showmeans = True)
plt.title("The distribution of new cases", color = "red")
plt.subplot(222)
plt.boxplot(new_deaths, vert = True, patch_artist = True, boxprops = {"color":"gray"}, showmeans = True, flierprops={"marker":"*", "markerfacecolor":"red"})
plt.title("The distribution of new deaths", color = "red")
china_dates = np.array(china[['date']])
plt.subplot(212)
plt.plot(range(len(china_dates)), new_cases, 'r+')
plt.plot(range(len(china_dates)), new_deaths, 'b+')
plt.title("New cases or deaths over time", color = "red")
plt.xticks(range(0, len(china_dates), 4), china_dates[0:len(china_dates):4], rotation = -90)
plt.xlabel("time")
plt.ylabel("the number of new cases or deaths")
plt.tick_params(labelsize=6)
plt.subplots_adjust(right=0.9, top=0.9, left=0.1, bottom=0.2,hspace = 0.5)
plt.show()

countryall = list(covid_data.iloc[:,1])
country = []
for i in range(len(countryall)):
    if countryall[i] not in country:
        country.append(countryall[i])
ls = []
for j in range(len(country)):
    a = list(covid_data.loc[covid_data["location"].isin([country[j]])].iloc[:,2])
    ls.append(a)
oh = np.array(ls, dtype = list)
lsmax = []
lsmean = []
for m in range(len(oh)):
    lsmax.append(np.amax(oh[m]))
    lsmean.append(np.mean(oh[m]))
plt.subplot(211)
plt.title("The mean number of new cases in each country", size = 7, color = "red")
plt.scatter(range(200), lsmean, marker = '.', color = 'green', s = 1)
plt.xticks(range(200), country, rotation = -90)
plt.tick_params(labelsize=3)
plt.subplot(212)
plt.title("The maximum number of new cases in each country", size = 7, color = "red")
plt.scatter(range(200), lsmax, marker = '.', color = 'blue', s = 1)
plt.xticks(range(200), country, rotation = -90)
plt.tick_params(labelsize=3)
plt.subplots_adjust(right=0.9, top=0.9, left=0.1, bottom=0.1,hspace = 0.6)
plt.show()
lsmean_little = []
for p in range(len(lsmean)):
    if lsmean[p] <= 5:
        lsmean_little.append(country[p])
print("There are %d countries whose mean number of new cases has not yet been larger than 5 before 31 March are %s"%(len(lsmean_little),lsmean_little))
lsmax_little = []
for q in range(len(lsmax)):
    if lsmax[q] <= 30:
        lsmax_little.append(country[q])
print("There are %d countries whose maximum number of new cases has not yet been larger than 30 before 31 March are %s"%(len(lsmax_little), lsmax_little))




