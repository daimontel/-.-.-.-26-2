def check_positive(number):
    if number > 0:
        return "Число положительное"
    else:
        return "Число не положительное"

def find_greater(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def is_in_range(x, a, b):
    if x >= a and x <= b:
        return "Точка попадает в отрезок [a, b]"
    else:
        return "Точка не попадает в отрезок [a, b]"

if __name__ == "__main__":
    num = float(input("Введите число: "))
    result = check_positive(num)
    print(f"Результат: {result}")

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    greater_num = find_greater(num1, num2)
    print(f"Большее число: {greater_num}")

    a = float(input("Введите начало отрезка (a): "))
    b = float(input("Введите конец отрезка (b): "))
    x = float(input("Введите координату точки (x): "))
    is_in_range_result = is_in_range(x, a, b)
    print(f"Результат: {is_in_range_result}")
