passwordSave = ""
passwordLabel = ""
#Accepting input
import random
passwordRange = int(input("Enter your password size: "))
#Looping and printing
for i in range(passwordRange):
password = chr(random.randint(33,122))
print(password,end="")
passwordSave += password
#Option of saving the password to a file
userChoice = str(input("\nWould you like to save your password? "))
if userChoice == "Yes" or userChoice == "yes":
with open("C:\\Users\\athit\\Documents\\passwords.txt","a") as file1:
file1.write("\n")
#Offering a label choice
userChoice = str(input("Would you like to label your password? "))
if userChoice == "Yes" or userChoice == "yes":
passwordLabel = str(input("Enter your label "))
file1.write(passwordLabel)
file1.write(" : ")
file1.write(passwordSave)
file1.close()
else :
file1.write(passwordSave)
file1.close()
print("Your password has been successfully saved."
