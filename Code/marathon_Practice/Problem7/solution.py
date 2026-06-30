mem = []
def climbStair(x):
    a,b = 1,1
    for i in range(x - 1):
        temp = a
        a = a + b
        b = temp
    return a

def main():
    n = int(input(' '))
    return climbStair(n)

print(main())