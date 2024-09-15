#constants
bread_price = 3.49
discount = 0.6
discounted_price = bread_price * (1 - discount)


#user_input
total_bread_bought = float(input("Enter the ammount of bread bought: "))


#calculations
total_regular_price = round((total_bread_bought * bread_price),2)
total_cost = round((total_bread_bought * discounted_price),2)
price_deduction = round((total_regular_price - total_cost),2)
 


print (f"Regular price of bread: ${bread_price:.2f}")
print (f"Total in regular price: ${total_regular_price:.2f}")
print (f"Price deduction: ${price_deduction:.2f}")
print (f"Total cost of the amount of bread sold: ${total_cost:.2f}")












