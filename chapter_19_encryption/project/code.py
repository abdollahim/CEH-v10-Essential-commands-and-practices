import datetime

# Iterative Python3 program
# to compute modular power
 
# Iterative Function to calculate
# (x^y)%p in O(log y)
# copyright: https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
def power(x, y, p) :
    res = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    x = x % p
     
    if (x == 0) :
        return 0
 
    while (y > 0) :
         
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
         
    return res

print("This is my Python program to calculate Diffie-Hellman")
print("Started at ", datetime.datetime.now())

# test numbers from the Project
# p = 541
# g = 10

# a = 5
# b = 7

# real numbers from the Project
p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919
g = 2

a = 1101001010019203192312312312435234234131235457686756554434232325365645342323243
b = 2343423432473984729384792837492837498273984739847982

# simple way to calculate small numbers ;)
# it doesn't work for large numbers because of occurring overflow
# A = ((pow(g, a)) % p)
# B = ((pow(g, b)) % p)

# Ka = ((pow(B, a)) % p)
# Kb = ((pow(A, b)) % p)

# modern way to calculate large numbers ;)
A = power(g, a, p)
B = power(g, b, p)

Ka = power(B, a, p)
Kb = power(A, b, p)

print("Finished at ", datetime.datetime.now())

print("The Secret key of A is : ", str(Ka))
print("The Secret key of B is : ", str(Kb))