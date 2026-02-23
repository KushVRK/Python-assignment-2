def is_prime(n):
    # 0 and 1 are not prime
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # even numbers are not prime
    if n % 2 == 0:
        return False
    # check divisibility up to square root
    for i in range(3, int(n**0.5) + 1, 2): #step 2 given because even numbers are already checked
        if n % i == 0:
            return False
    return True


# part 1 - check single number
print("---------------- Part 1: Prime Checker -----------------")
try:
    num = int(input("Enter a number: "))

    if num < 0:
        print(f"{num} is a negative number, not prime!")
    elif num == 0 or num == 1:
        print(f"{num} is NOT a prime number.")
    elif is_prime(num):
        print(f"{num} is a PRIME number")
    else:
        print(f"{num} is NOT a prime number")

except ValueError:
    print("Invalid input! Enter a whole number.")


# part 2 - primes in a range
print("\n-------------- Part 2: Prime numbers in a range --------------")
try:
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))

    if start > end:
        print("Start should be less than end!")
    else:
        prime_list = [] # a list to append the prime numbers
        for i in range(start, end+1):
            if is_prime(i):
                prime_list.append(i)

        if len(prime_list) == 0:
            print("No prime numbers found in this range.")
        else:
            # join all primes with comma to display nicely
            print("Prime numbers: " + ", ".join(str(p) for p in prime_list))

except ValueError:
    print("Invalid input! Enter whole numbers only.")