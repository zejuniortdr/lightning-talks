#!/usr/bin/env python


def divisors(number):
	return [n for n in range(1, number+1) if number % n == 0]


def is_prime(number):
	if number % 2 == 0 or number == 1:
		print(f"{number} is not prime")
	else:
		divisors_list = divisors(number)
		if len(divisors_list) > 2:
			print(f"{number} is not prime, here the divisors: {divisors_list}")
		else:
			print(f"{number} is prime, here the divisors: {divisors_list}")


if __name__ == '__main__':
	number = int(input("Number: "))
	is_prime(number)
