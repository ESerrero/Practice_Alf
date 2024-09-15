interest=4/100
money=float(input("Enter the ammount of money in the account: "))

result_1=(money* (1 + interest))
result_2=(result_1* (1 + interest))
result_3=(result_2* (1 + interest))




print("In the first year you will have: ",str (round((result_1), 2)))
print("In the second year you will have: ",str (round((result_2), 2)))
print("In the third year you will have: ",str (round((result_3), 2)))