#!/usr/bin/python -tt

P = 59 # prime
M = 6 # primitive root modulo p

def read_seed():
    while True:
        x = raw_input('Seed? ')
        try:
            x = int(x)
        except ValueError:
            continue
        return x

def extract_digit(x, n):
    return x // pow(10, n) % 10 # zero-indexed

def main():
    x = read_seed()
    while True:
        x = M * x % P
        raw_input(extract_digit(x, 0))

if __name__ == '__main__':
    main()
