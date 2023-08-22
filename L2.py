# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.
#def sum_digits(num):
#     # Функция для суммирования цифр числа
#     total = 0
#     while num > 0:
#         total += num % 10
#         num //= 10
#     return total
#
# def main():
#     cubes = [x ** 3 for x in range(1, 1001, 2)]
#
#     sum_divisible_by_7_before = 0
#     for num in cubes:
#         if sum_digits(num) % 7 == 0:
#             sum_divisible_by_7_before += num
#
#     for i in range(len(cubes)):
#         cubes[i] += 17
#
#     sum_divisible_by_7_after = 0
#     for num in cubes:
#         if sum_digits(num) % 7 == 0:
#             sum_divisible_by_7_after += num
#
#     print("Сумма кубов нечётных чисел, сумма цифр которых делится на 7 до добавления 17:", sum_divisible_by_7_before)
#     print("Сумма кубов нечётных чисел, сумма цифр которых делится на 7 после добавления 17:", sum_divisible_by_7_after)
#
# if __name__ == "__main__":
#     main()