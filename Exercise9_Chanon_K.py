usernameInput = input("Username : ")
passwordInput = input("Password : ")

while usernameInput != "Admin" or passwordInput != "123456":
    print("Username or Password invalid ,please try again")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
print("Welcome!!")
    