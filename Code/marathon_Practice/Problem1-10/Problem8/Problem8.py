def check(middle ,n):
    return n <= (2**middle) - 1

def binarySearch(x):
    bottom = 1
    top = 30
    while(bottom < top):
        middle = (bottom + top)//2
        if check(middle, x):
            top = middle
        else: 
            bottom = middle + 1
    return top

def main():
    n = int(input())
    print(binarySearch(n))

main()    




    