#use_input
n=float(input("Enter a number to be divided: "))
m=float(input("Enter the divisor: "))



#calculations
if m==0:
    print("Error division by 0 is undefined")

x=n//m #division with integer result
reminder=n%m #reminder of the division
      
#output
print(f"The result of the division of {n} and {m} is: {x}")
print(f"The reminder of the division is: {reminder}")   




