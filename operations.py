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
def dp_knapsack(C, items):
    n = len(items)
    dp = [[0] * (C + 1) for _ in range(n +1)]

    for i in range(1, n+1):
        p, w = items[i - 1]
        for cap in range(C + 1):
            if w <= cap:
                dp[i][cap] = max(dp[i -1][cap], dp[i - 1][cap - w] + p)
            else:
                dp[i][cap] = dp[i - 1][cap]
    
    cap = C
    selected = []
    for i in range(n, 0, -1):
        if dp[i][cap] != dp[i - 1][cap]:
            selected.append(i)
            cap -= items[i - 1][1]

    print(f"Max value: {dp[n][C]}")
    print(f"Selected items: {sorted(selected)}")

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
                current_comb.append(j+1)

                if current_c > C:
                    break

        if current_c <= C and current_value > best_value:
            best_value = current_value
            best_comb = current_comb

    print(f"Max value: {best_value}")
    print(f"Selected items: {sorted(best_comb)}")
