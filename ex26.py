#Username and password

print("Sing up")
username = input("Chose your username: ")
password = input("Chose your password: ")
attempts = 0

while attempts < 3 :
        print("Login")
        user = input("Enter your username: ")
        pas = input("Enter your password: ")
        if user == username and pas == password:
            print("Welcome")
            break
        else:
            print("Wrong user name or password")
            attempts = attempts + 1
