
def kadane(days_, cost, revenue):
    array = [i-cost for i in revenue]
    max_sum = array[0]
    sum_ = array[0]
    for i in range(1, len(array)):
        sum_ = (max(array[i], sum_ + array[i]))
        max_sum = (max(sum_, max_sum))

    return max_sum


def main():
    ans = []
    n = int(input())
    for _ in range(n):
        d = int(input())
        c = int(input())
        rev = []
        for i in range(d):
            rev.append(int(input()))
        ans.append(kadane(d,c,rev))
    return ans

for i in main():
    if i <0:
        print(0)
    else:
        print(i)