#pizza_party.py
#First calculate at least how many pieces we can get for increasing straight cuts, then stop the loop when the pieces can satisfythe whole class' need
n = 0
#Make preparation for the loop
p = (n*n+n+2)/2
#Give the calculation function and also prepare for the loop
while p < 64:
#Give the condition when the loop continue
    n = n + 1
#Add cuts for the next calculation
    p = (n*n+n+2)/2
#Calculate the total pieces under the specific cuts
    print("%d pieces of a pizza can be made with %d straight cuts" % (p, n))
#Make the number output formal
#When we get enough pieces we will get out of the loop
print('''So, when we have enough pieces for each member of the class,
         the number of straight cuts is at least:''', str(n))
#Now we have found the least cuts that satisfy the condition and print the answer
        
