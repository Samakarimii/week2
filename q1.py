def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_right_truncatable_primes(n):
    def generate_right_truncatable_primes(prefix, length):
        if length == 0:
            num = int(prefix)
            if is_prime(num):
                print(num)
        else:
            for digit in "123456789":
                new_prefix = prefix + digit
                num = int(new_prefix)
                if is_prime(num):
                    generate_right_truncatable_primes(new_prefix, length - 1)

    if n < 1:
        print("n must be a positive integer.")
        return

    generate_right_truncatable_primes("", n)

n = int(input("Please enter the value of n: "))
print_right_truncatable_primes(n)