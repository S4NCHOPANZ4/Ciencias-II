def knapsack(n,amo,cap,res):
    memo={}
    def helper(element, load):
        if element < 0:
            return 0
        if (element, load) in memo:
            return memo[(element, load)]
        not_take = helper(element-1, load)
        take_ = 0
        if load + amo[element][1] <= cap:
            newLoad = load + amo[element][1]
            take_ =  amo[element][0] + helper(element-1, newLoad)
        memo[(element,load)] = max(take_, not_take)
        return memo[(element,load)]
    max_load = helper(n-1, 0)
    if max_load < res:
        return "Falha na missao"
    return "Missao completada com sucesso"

def main():
    m = int(input())
    ans = []
    for i in range(m):
        n = int(input())
        amo = []
        for j in range(n):
            amo.append(list(map(int, input().split())))
        cap = int(input())
        res = int(input())
        ans.append(knapsack(n,amo,cap,res))
    return ans

for i in main():
    print(i)

        