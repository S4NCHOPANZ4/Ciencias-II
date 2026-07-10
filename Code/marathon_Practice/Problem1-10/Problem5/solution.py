def check(limit, data, n):
    load = 0
    trucks = 1

    for i in data:
        if load + i <= limit:
            load += i
        else: 
            trucks += 1
            load = i
    return trucks <= n

def binarySearch(bottom,top, data, n):
    while bottom < top:
        middle = int((bottom + top)/2)
        if check(middle, data, n):
            top = middle
        else:
            bottom = middle + 1
    return top

def dayResult(ptf,weights):
    trucks = int(ptf[1])
    freight = int(ptf[2]) #value for each kg transported
    mostLoadedTruck = binarySearch(max(weights), sum(weights), weights, trucks) 
    return mostLoadedTruck,  freight*trucks*mostLoadedTruck

def main():
    n = int(input(''))
    data = []
    for i in range(n):
        ptf = input('').split()
        weights = list(map(int, input('').split()))
        data.append(dayResult(ptf, weights))
    return data

for i in main():
    print(f"{i[0]} ${i[1]}")
