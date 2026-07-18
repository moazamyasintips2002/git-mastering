student_name = "moazam yasin"
ag_no = 2024-ag-9343



name_input = input("Student Name: ")
ag_input = input("Enter Your Ag: ")
class_input = input("Enter Your Class Name: ")

if name_input == student_name:
    
    print("Login Successful")
else:
    print("Login Unsuccessful")

print("welcome to", student_name,"in our paradise")

print("Let's play a game!")

while True:
    user = input("Guess the number from 1 to 4: ")

    if user == "1":
        print("You are intelligent!")
    elif user == "2":
        print("Nice try! You are improving.")
    elif user == "3":
        print("Good choice! You are learning fast.")
    elif user == "4":
        print("Almost there! Keep going.")
    else:
        print("Invalid number, please choose between 1 and 4.")

    # Ask if the user wants to play again
    choice = input("Do you want to play again? (yes/no): ").lower()

    if choice != "yes":
        print("Thanks for playing! See you next time.")
        break

