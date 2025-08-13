import random
#● ┌ ─ ┐ │ └ ┘

dice_art={1:(
           "┌──────────┐",
           "│          │",
           "│     ●    │",
           "│          │",
           "└──────────┘"),
 2:("┌──────────┐",
    "│  ●       │",
    "│          │",
    "│       ●  │",
    "└──────────┘"),
 3:("┌──────────┐",
    "│   ●      │",
    "│     ●    │",
    "│       ●  │",
    "└──────────┘"),
 4:("┌──────────┐",
    "│  ●     ● │",
    "│          │",
    "│  ●     ● │",
    "└──────────┘"),
 5:("┌──────────┐",
    "│  ●     ● │",
    "│     ●    │",
    "│  ●     ● │",
    "└──────────┘"),
  6:("┌──────────┐",
     "│  ●     ● │",
     "│  ●     ● │",
     "│  ●     ● │",
     "└──────────┘"),}

num=int(input("Enter a number: "))
dice=[]
total=0

for i in range(num):
    dice.append(random.randint(1,6))
print(dice)

for x in range(num):
    for die in dice_art.get(dice[x]):
        print(die)


for x in dice:
    total+=x
print(f"total:{total}")