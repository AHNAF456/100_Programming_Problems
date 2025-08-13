# A shopping Cart Programm
foods=[]
price=[]
total=0
while True:
    food=input("Enter food name to buy(q to quit):")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price=int(input(f"Enter price of a {food}: "))
        total=total+price
print("--------YOUR CART---------")
for food in foods:
     print(food, end="\n")

print(f"The total price is {total}Tk")
