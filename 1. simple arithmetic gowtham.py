print("\t\tSIMPLE ARITHMETIC OPERATION")
print("\t\t*************************")
print("enter the two number")
a=int(input("enter the number 1:"))
b=int(input("enter the number 2:"))
print(" ")
add = a + b
sub = a - b
mul = a * b
div = a / b
mod = a // b
pow = a ** b
fp=open("pay.txt","w")
print("Addition of a and b is",add)
print("Subtraction of a and b is",sub)
print("Multiplication of a and b is",mul)
print("Division of a and b is",div)
print("Modulo of a and b is",mod)
print("value of a power of  b is",pow)
fp.write("Addition of a and b is:"+str(add)+"\nSubtraction of a and b is:"+str(sub)+"\nMultiplication of a and b is:"+str(mul)+"\nDivision of a and b is:"+str(div)+"\nModulo of a and b is"+str(mod)+"\nvalue of a power of  b is:"+str(pow))
fp.close()
fp=open("pay.txt","r")
print(fp.read())
fp.close()
