#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
summ = 0
square_summ = 0
for i in range(101):
    summ += i
    square_summ += i**2
print(summ**2 - square_summ)