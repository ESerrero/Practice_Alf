
#user_input
name = input("Enter your name: ")


try:
    repetition = int(input("Enter a number: "))
    
except ValueError:
    repetition = 0
    print ("Error: You must give an integer number for the number of repetitions.")
    

#calculations
result = (name + '\n') * repetition


#output
print(result)


