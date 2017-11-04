#What is the largest prime factor of the number 600851475143
a = 600851475143
x = 4
prime = [2,3]
wanted = ['banana']
while x <= (a):
    b = 0
    for m in prime:
        if x % m == 0:
            b = 1
    if b == 0:
        prime.append(x)
        while a % x == 0:
            wanted.append(x)
            a = (a/x)
    x += 1
print(wanted[-1])