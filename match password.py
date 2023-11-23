# Here is some match password
password_1 = input("Enter password 1: ")
password_2 = input("Enter password 2: ")

while password_1 != password_2:
    print(" password doesn't match !")
    break
password_1 = input("Enter password 1: ")
password_2 = input("Enter password 2: ")
while password_1 == password_2 :
    print ( " Password is match" )
    break