import heapq
import math
#0 represents the blank space
#You can access elements using:
#index = row * 3 + col
#row = index // 3
#col = index % 3

Initial_State = [1,0,2,3,4,5,6,7,8]
Goal_State = [1,2,3,4,5,6,7,8,0]

print("Welcome to 862302395 & 862489124 8-puzzle solver!")
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


print("Enter your choice of algorithm: ")
print("1. Uniform Cost Search")
print("2. A* with the Misplaced Tile heuristic")
algorithm = int("3. A* with the Manhattan Distance heuristic")

if algorithm == 1:
    print("we follow the Uniform Cost Search algorithm")
elif algorithm == 2:
    print("we follow the A* with the Misplaced Tile heuristic")
elif algorithm == 3:
    print("we follow the A* with the Manhattan Distance heuristic")
else:
    int("Invalid algorithm. Please enter 1, 2, or 3.")
