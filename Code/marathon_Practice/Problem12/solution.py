def kadane(days, cost):
    profits = []
    for i in days:
        profits.append(i - cost)
    current = profits[0]
    maxSum = profits[0]

    for i in range(1, len(profits)-1):
        current = max(profits[i], profits[i] + current)
        maxSum = max(current, maxSum)
    if maxSum < 0:
        return 0
    return maxSum

def main():
    results = []

    while True:
        try:
            d = int(input())
        except EOFError:
            break

        cost = int(input())

        days = []
        for _ in range(d):
            days.append(int(input()))

        results.append(kadane(days, cost))

    return results


for ans in main():
    print(ans)
# print(kadane([18,35,6,80,15,21], 20))




# def dp(days, cost, n):
#     memo = []
#     def helper(index, profit):
#         if index == n:
#             return profit 
#         ir = helper(index+1, profit+days[index]-cost)
#         no_ir = helper(index+1, profit)
#         return(max(ir, no_ir))
#     print(helper(0, 0))

        
         
