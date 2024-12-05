# Домашнее задание по теме "Декораторы"

# декоратор - проверка числа на "простоту"
def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res <= 1:
            print("Сумма чисел должна быть > 1")
        else:
            is_primes = True
            for i in range(2, res // 2 + 1):
                if res % i == 0:
                    is_primes = False
                    break
            if is_primes:
                print("Простое")
            else:
                print("Составное")
        return res

    return wrapper


# сумма трех(!) чисел c декоратором
@is_prime  # декоратор - проверка числа на "простоту"
def sum_three(*args):
    res = 0
    i = 0  # счетчик количества чисел
    for ia in args:
        res += ia
        i += 1
        if i == 3: # если количество чисел больше 3, то остальные игнорируются
            break
    return res


if __name__ == "__main__":
    result = sum_three(2, 3, 6)
    print(result)
