# A timer programm
import time
t=int(input("Enter time in seconds:"))
for x in range(t,-1,-1):
    second=x%60
    minute=int(x/60)%60
    hour=int(x/3600)
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)
print("Thank you")