#!/usr/bin/python3
import sys
import random
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    x = random.randint(1, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1

    while d == 1:
        x = (x * y + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)
    return d

def find_prime_factors(n):
    factors = []
    while n != 1:
        factor = pollards_rho(n)
        while n % factor == 0:
            n //=factor
        factors.append(factor)
    return factors

def main():
    with open(sys.argv[1], "r") as file:
        rsa_number_str = file.readline().strip()

    n = int(rsa_number_str)
    factors = find_prime_factors(n)
    print("{}={}*{}".format(rsa_number_str, factos[0], factors[1]))

if __name__== "__main__":
    main()
