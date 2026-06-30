def bestRunning(slots,runlen,adition):
    time = 0
    benefit = []
    for i in slots:
        time += 1/i
        benefit.append((1/i) -  1/(adition + i))
    benefit.sort(reverse=True)

    for i in range(runlen):
        time -= benefit[i]
    return f"{time:.2f}"

def main():
    data=[]
    n = int(input(''))
    for i in range(n):
        scr = list(map(int, input('').split()))
        slots = list(map(int, input('').split()))
        res = bestRunning(slots, scr[1], scr[2])
        data.append(res)
    return data

for i in main():
    print(i)
