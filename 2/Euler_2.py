#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
fibonacci = [1,1]
fibonacci_even = []
while fibonacci[-1] <= 4000000:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if fibonacci[-1] % 2 == 0:
        fibonacci_even.append(fibonacci[-1])
sum = 0
for i in fibonacci_even:
    sum += i
print(sum)