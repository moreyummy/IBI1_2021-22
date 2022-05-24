all = input("Please input a DNA sequence:")
all = list(all.upper())
ohoh = ["A", "T", "C", "G"]

for m in range(len(all)):
    if not all[m] in ohoh:
        all = list(input("The DNA sequence is wrong, please input again:").upper())

def content_cal(x, l):
    count = 0
    for i in range(len(l)):
        if x == l[i]:
            count += 1
    return(format(count/len(l), ".2%"))

for n in range(len(ohoh)):
    print("The percentage of %s nucleotides in the DNA sequence is %s" % (ohoh[n],content_cal(ohoh[n], all)))
