#Задание 1
N = int(input())        
nums = [int(input()) for i in range(N)]
print(*nums[::-1])
