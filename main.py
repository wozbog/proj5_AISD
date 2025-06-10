import sys
import threading
from operations import print_help, dp_knapsack, brute_force
sys.setrecursionlimit(1000000000)

def main():
    # Command-line argument: python3 mainpy --knapsack
    if len(sys.argv) != 2 or (sys.argv[1] != "--knapsack"):
        print("Usage: python3 main.py --knapsack")
        sys.exit(1)

    #Variables
    capacity = 0
    n = 0
    items = []

    #User input
    try:
        
        #Capacity of knapsack
        print("Input capacity of a knapsack")
        capacity = int(input("C> ").strip())
        if capacity <= 0:
            print(f"{capacity} isn't greater than 0")
            sys.exit(1)
        
        #Number of items
        print("Input a number of items")
        n = int(input("n> ").strip())
        if (n <= 0):
            print("Number of items must be greater than 0 and be an integer")
            sys.exit(1)

        #Values of items    
        print(f"Input {n} items in the format: p(value) w(capacity) ")
        for i in range(n):
            while True:
                try:
                    print(f"\nItem {i+1}/{n}")
                    data = input("p w> ").split()
                    if len(data) < 2:
                        print("Enter both value and capacity")
                        continue

                    p = int(data[0].strip())
                    w = int(data[1].strip())

                    if p<=0 or w<=0:
                        print("Values of p and w must be greater than 0")
                        continue

                    items.append((p, w))
                    break

                except ValueError:
                    print("Invalid input. Please enter integers.")
    
    except Exception as e:
        print(f"Invalid input: {e}")
        sys.exit(1) 

    #Reset terminal
    try:
        sys.stdin = open('/dev/tty')
    except Exception:
        print("Error returning to terminal. (dev/tty).")
        sys.exit(1)

    #Commands and operations on knapsack
    while True:
        try:
            action = input("action> ").strip().lower()
        except EOFError:
            print("\nThe program has ended (EOF). ")
            break

        if action == "help":
            print_help()
        elif action == "print":
            print(f"Information about your knapsack: Capacity = {capacity}, Number of items = {n}, Items = {items}")
        elif action == "dynamic programming" or action == "dp":
            dp_knapsack()
        elif action == "brute force" or action == "bf":
            brute_force(capacity, items)
        elif action == "exit":
            print("The program has ended.")
            break

        else:
            print(f"Unknown command: {action}\n")
            print(f"Try one of these:")
            print_help()

if __name__ == "__main__":
    main()