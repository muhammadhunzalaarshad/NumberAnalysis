from functools import reduce
from typing import List

def is_prime(number: int) -> bool:
    """
    Determine if a given number is prime.
    Args:
        number (int): The number to evaluate for primality.
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Handle non-prime and edge cases
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    # Check odd divisors up to square root of number
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True

def find_factors(number: int) -> int:
    """
    Find all factors of a given number.
    Args:
        number: The integer to find factors for.
    Returns:
        List[int]: A sorted list of all factors of the number.
    """
    factors = []
    for divisor in range(1, int(number ** 0.5) + 1):
        if number % divisor == 0:
            factors.append(divisor)
            if number // divisor  != divisor:
                factors.append(number // divisor)            
    return factors

def lcm_func(number_1: int, number_2: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two integers using the Euclidean algorithm.
    Args:
        number_1: The first integer.
        number_2: The second integer.
    Returns:
        int: The LCM of the two numbers.
    """
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    return abs((number_1 * number_2) // gcd(number_1, number_2))

def main() -> None:
    """
    Read numbers from a file, analyze their primality and factors, and compute the LCM of all numbers.

    Reads integers from 'numbers.txt', writes primality, factors, and factor count for each number,
    and the LCM of all numbers to 'output.txt'. Handles errors for invalid or missing input.

    Raises:
        ValueError: If the file is empty, contains invalid numbers, or includes negative/zero values.
        FileNotFoundError: If 'numbers.txt' is not found.
    """
    try:
        with open("numbers.txt", "r") as file:         
            content = file.read().splitlines()
            numbers = [int(num.strip()) for num in content if num.strip()]

            if not numbers:
                raise ValueError("File is empty or contains no valid numbers")
            if any(num <= 0 for num in numbers):
                raise ValueError("File contains negative or zero numbers")

            with open("output.txt", "w") as file:
                for number in numbers:
                    prime_status = is_prime(number)
                    factors = find_factors(number)
                    file.write(f"Number: {number}, Prime: {'Yes' if prime_status else 'No'}, Factors: {factors}, Factor count: {len(factors)}\n")
                if len(numbers) == 1:
                    file.write(f"LCM of all numbers: {numbers[0]}")
                else:
                    file.write(f"LCM of all numbers: {reduce(lcm_func, numbers)}")

    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError as f:
        print("Error: numbers.txt file not found")

if __name__ == "__main__":
    main()
