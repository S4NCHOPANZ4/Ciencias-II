def knesack(weights, values, cap, res):
    n = len(weights)
    memo = [[-1 for _ in range(cap + 1)] for _ in range(n)]
    def helper(index, remaining_cap):
        if index == n:
            return 0
        if memo[index][remaining_cap] != -1:
            return memo[index][remaining_cap]
        not_take = helper(index + 1, remaining_cap)

        take = 0
        if weights[index] <= remaining_cap:
            take = values[index] + helper(index+1, remaining_cap - weights[index])
        memo[index][remaining_cap] = max(not_take, take)
        return memo[index][remaining_cap]
    resp = helper(0, cap)
    if resp >= res:
        return "Missao completada com sucesso"
    return "Falha na missao"


def main():
    n = int(input(""))
    ans = [] 
    for i in range(n):
        m = int(input(""))
        weights = []
        values = []
        for i in range(m):
            w = list(map(int, input('').split()))
            weights.append(w[1])
            values.append(w[0])
        cap = int(input(''))
        res = int(input(''))  
        ans.append(knesack(weights, values, cap, res))
    return ans
for i in main():
    print(i)










# def runSimulation(data, resistance, cap) -> str:
#     data_ = data
#     dmg =  0
#     load = 0
#     while dmg < resistance:
#         if len(data_) == 0:
#             return "Falha na missao"
#         toLoad = max(data_, key=lambda x: x[0]/ x[1])
#         if load+toLoad[1] < cap:
#             dmg += toLoad[0]
#             load += toLoad[1]
#         data_.remove(toLoad)
#     return "Missao completada com sucesso" 

# def main():
#     n = int(input(""))
#     ans = [] 
#     for i in range(n):
#         m = int(input(""))
#         cannonBalls = []
#         for i in range(m):
#             w = list(map(int, input('').split()))
#             cannonBalls.append((w[0], w[1]))
#         cap = int(input(''))
#         res = int(input(''))  
#         ans.append(runSimulation(cannonBalls, res, cap))
#     return ans
# for i in main():
#     print()
        