def factorial(n):
    memo = {
        0: 1,
        1: 1
    }
    def helper(n):
        if n <= 1:
            return 1
        if n in memo:
            return memo[n]
        toMemo = n*helper(n-1)
        memo[n] = toMemo
        return toMemo
    helper(n)
    return memo[n]

def countElements(n):
    elements = {}
    fribNum = factorial(n)
    str_ = str(fribNum)
    for i in range(10):
        index = str(i)
        elements[index] = 0
    for i in str_:
        elements[i] = elements[i] + 1
    return elements 

def formatprint(dict_):
    response = ""
    for key, value in dict_.items():
        response = response + f"({key}) \t {value}"
    return response


def main():
    n = int(input(''))
    ans = []
    for i in range(n):
        m = int(input(''))
        sub_ans = countElements(m)
        ans.append(sub_ans)
    return ans


for i in main():
    print(formatprint(i))

