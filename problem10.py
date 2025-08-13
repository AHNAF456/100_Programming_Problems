#A sign in/Log in programm
user={"Abir":"1234","Maliha":"5678","Kamrul":"9012","Nargis":"3456"}
Name=input("Enter username:").capitalize()
while True:
    if Name in user.keys():
        password=input("Enter password:").capitalize()
        if password == user.get(Name):
            print("You are logged in")
            break
        elif password != user.get(Name):
             print("Wrong password")
    else:
        print("You have no valid account")
        ask=input("Do you want to creat an account?").capitalize()
        if ask=="Yes":
            name=input("Enter your name:").capitalize()
            newpassword=input("Enter a strong password:").capitalize()
            user.update({name:newpassword})
        else:
            print("Thank you!")
            break


