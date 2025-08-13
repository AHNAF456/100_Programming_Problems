#A concession programm
Menu={"Popcorn":1.00,"Chips":1.00,"Burger":2.50,
      "Sandwitch":3.20,"Pizza":5.50,"Mutton":6.20,
      "Mango juce":1.20}
cart=[]
total=0
print("-------Menu-------")
for key,value in Menu.items():
    print(f"{key:10} : {value:.2f}")
print("------------------")
while True:
    food=input("Choose an option to buy(q to quit):").capitalize()
    if food.lower() == "q":
        break
    elif Menu.get(food) is not None:
        cart.append(food)
        total=total+Menu.get(food)
    else:
        print(f"{food} is not available")
if len(cart)>0:
    print("----------YOUR ORDER------------")
    for item in cart:
        print(item)
    print(f"And your total is: {round(total,2)}")
else:
    print("You did't buy anything!")


