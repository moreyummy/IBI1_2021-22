def many(a, b):
    piece = a//b
    change = a - piece*b
    return("The number of chorocter bars is %d \nthe change left over is %.2f"%(piece, change))

#give an example: the first parameter is the total money and the second parameter is the price of one chocolate	bar
print(many(100, 7.6))