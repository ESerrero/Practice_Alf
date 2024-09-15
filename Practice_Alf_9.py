

money=float(input("Enter an ammount of money to invest: "))
y=int(input("Enter the ammount of years you want to invest: "))
interest=float(input("Enter ther ammount of annual iunterest: "))




result=float(round((money*(interest/100+1)** y) , 2))




print("Your fixed investment after those years is:" ,result)





