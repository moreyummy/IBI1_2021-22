def many(a, b):
    piece = a//b
    change = a - piece*b
    return("The number of chorocter bars is %d \nthe change left over is %.2f"%(piece, change))

print(many(150, 7.8))