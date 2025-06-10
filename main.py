import sys
import threading
sys.setrecursionlimit(1000000000)

def main():
    # Command-line argument: python3 mainpy --knapsack
    if len(sys.argv) != 2 or (sys.argv[1] != "--knapsack"):
        print("Usage: python3 main.py --knapsack")
        sys.exit(1)

    #Variables
    capacity = 0
    n = 0

    #User input
    try:
        print("Input capacity of a knapsack")
        capacity = int(input("C> ").strip())
        if capacity <= 0:
            print(f"{capacity} isn't greater than 0")
            sys.exit(1)
        print("Input a number of items")
        n = int(input("n> ").strip())
        if (n < 0):
            print("Number of items must be greater than 0 and be an integer")
            sys.exit(1)
    except Exception as e:
        print(f"Invalid input: {e}")
        sys.exit(1) 


    #Reset terminal
    try:
        sys.stdin = open('/dev/tty')
    except Exception:
        print("Error returning to terminal. (dev/tty).")
        sys.exit(1)

if __name__ == "__main__":
    main()