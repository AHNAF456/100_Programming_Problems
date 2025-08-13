#A calculator programm
First=int(input("Enter the first number: "))
Operator=input("Enter an Opetaron: ")
Second=int(input("Enter the second number: "))
if Operator=="+":
    result=First+Second
    print(result)
elif Operator=="-":
    result1=First-Second
    print(result1)
elif Operator=="*":
    result2=First*Second
    print(result2)
elif Operator=="/":
    result3=First/Second
    print(result3)
elif Operator=="%":
    result4=(First*Second)/100
    print(result4)
elif Operator=="**":
    result5=First**Second
    print(result5)
else:
    print("INVALID OPERATOR")
