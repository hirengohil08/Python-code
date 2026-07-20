# split() bina kisi argument ke space ko auto-detect kar leta hai
var1, var2, var3 = [int(x) for x in input("Enter three numbers : ").split(",")]
print("sum = ", var1 + var2 + var3)
