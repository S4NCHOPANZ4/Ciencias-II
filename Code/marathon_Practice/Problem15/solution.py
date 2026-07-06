def gapList(queue, groups):
    queue = [0] + queue
    cuts = groups - 1
    total = queue[-1] - queue[0]
    gaps = []
    for i in range(len(queue)-1):
        gap = queue[i+1] - queue[i]
        gaps.append(gap)
    gaps.sort(reverse=True)
    for i in range(cuts):
        total -= gaps[i]
    return total

def main():
    ans = []
    while True:
        try:
            n = list(map(int, input('').split()))
        except EOFError:
            break
        people = list(map(int, input('').split()))
        ans.append(gapList(people, n[1]))
    return ans
for ans in main():
    print(ans)

