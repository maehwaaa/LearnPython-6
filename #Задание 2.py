#Задание 2
n = int(input("Введите кол-во чисел - "))
arr = list(map(int, input("Введите числа через пробел - ").split()))

result = [arr[-1]] + arr[:-1]
print("Результат -", *result)
