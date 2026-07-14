n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

prices = [float("inf")] * n
prices[src] = 0

for _ in range(k+1):
    tmpPrices = prices.copy()
    for s,d,w in flights:
        if prices[s] == float("inf"):
            continue
        if prices[s] + d < tmpPrices[d]:
            tmpPrices[d] = prices[s] + d
    prices = tmpPrices

print(-1 if prices[dst] == float("inf") else prices[dst])                   
