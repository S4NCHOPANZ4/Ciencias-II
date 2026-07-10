def knapsack(val,wt,cap):
    n = len(wt)
    dp = [[-1 for _ in range(cap + 1)] for _ in range(n)]
    def helper(remaining_cap, index):
        if index == n:
            return 0
        if dp[index][remaining_cap] != -1:
            return dp[index][remaining_cap]
        not_take = helper(remaining_cap, index+1)
        take = 0
        if wt[index] <= remaining_cap:
            take =  val[index] + helper(remaining_cap-wt[index], index+1)
        dp[index][remaining_cap] = max(not_take,take)
        return dp[index][remaining_cap]
    return helper(cap,0)

def main():
    res = []
    while True:
        n = int(input(''))
        if n == 0: 
            break
        cap = int(input(''))
        wt = []
        val = []
        for i in range(n):
            ind = list(map(int, input('').split()))
            val.append(ind[0])
            wt.append(ind[1])
        res.append(knapsack(val, wt, cap))
    return res 


for ans in main():
    print(f"{ans} min.")