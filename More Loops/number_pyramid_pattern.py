# N = 5
# 12345
#  2345
#   345
#    45
#     5
#    45
#   345
#  2345
# 12345

n = int(input())
for i in range(1 , n + 1):
    count = 1
    for j in range(1 , i):
        print(" ",end = "")
        count = count + 1
    num = i 
    for j in range(count, n + 1):
        print(num, end = "") 
        num = num + 1
    print()
for i in range(n - 1, 0 , -1):
    count = 1
    for j in range(1 , i):
        print(" ",end = "") 
        count = count + 1
    num = i 
    for j in range(count, n + 1): 
        print(num, end = "")
        num = num + 1 
    print()