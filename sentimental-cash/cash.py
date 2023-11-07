# TODO

while True:
        try:
            # used to get input from user
            money = float(input("Enter an amount: "))

            # users values can only be positive
            if money > 0 :
               break
            
            money = round(money *100)

            print(money)
            
        except ValueError:
                print("Not an Integer")



count = 0

# calculates quarters
while money >= 25:
      money = money - 25
      count += 1
      
# calculates dimes
while  money >= 10:
       money = money - 10 
       count += 1

# calculates nickels
while  money >= 5:
        money = money - 5
        count += 1

#  calculates pennies
while money >= 1:
     money = money - 1
     count += 1 



print("Amount :" , count)