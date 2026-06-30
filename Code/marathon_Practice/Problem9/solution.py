# def validPosition(x, h):
#     valid = True
#     if x-1 < 0:
#         valid = False
#     if  x+1 > h:
#         valid = False
#     return valid


# def add(i,j, grid):
#     alpha = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
#     for letter in alpha:
#         #arriba
#         if validPosition(i, len(grid)-1) and :
            

# def check(middle, x):
#    return (2**middle)-1 >= x

# def binatySearch(x):
#     bottom = 1
#     top = 26
#     while(bottom < top):
#         middle = (bottom + top) //2
#         if check(middle, x):
#           top = middle
#         else:
#            bottom = middle + 1  
#     return top

# def fill(n):
#     alpha = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
#     res = []
#     m = binatySearch(n)
#     for i in range(n**2):
#         limit = i % m
#         res.append(alpha[limit])
#     return res

# print(fill(3))