from _pi_approx import ffi, lib

n = int(input('Enter the amount of iterations (integer): '))

print(lib.pi(n))
