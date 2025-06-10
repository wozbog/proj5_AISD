import math

#Help
def print_help():
    print("---------------------------------------------------------------------------------------")
    print("Help                         Show this message")
    print("Print                        Display the information about knapsack")
    print("Dynamic Programming | DP     Solve problem using Dynamic Programming")
    print("Brute Force         | BF     Solve problem using Brute Force method")
    print("Exit                         Exit the program (same as Ctrl+D)")
    print("---------------------------------------------------------------------------------------")

#Dynamic Programming
def dp_knapsack():
    print("Dynamic programming")

def brute_force(C, items):
    n = len(items)
    best_value = 0
    best_comb = []

    for i in range(1 << n):
        current_c = 0
        current_value = 0
        current_comb = []

        for j in range(n):
            if i & (1 << j):
                p, w = items[j]
                current_c += w
                current_value += p
                current_comb.append(j)

                if current_c > C:
                    break

        if current_c <= C and current_value > best_value:
            best_value = current_c
            best_comb = current_c

    return best_value, best_comb
