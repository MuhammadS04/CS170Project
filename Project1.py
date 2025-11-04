print("Welcome to 862302395 & 862489124 &mabid002 8 puzzle solver!")
print("Type \"1\" to solve the puzzle, or \"2\" to enter your own puzzle.")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("You have been given the default puzzle")
    print("1 2 3")
    print("4 5 6")
    print("7 8 0")
elif choice == 2:
    print("Enter your puzzle, use a zero to represent the blank")

else:
    int("Invalid choice. Please enter 1 or 2.")