#소수의 판별: 기본적인 알고리즘
def is_prime_number(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))