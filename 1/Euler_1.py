#Find the sum of all the multiples of 3 or 5 below 1000.
a = 0
for i in range(999):
    if (i+1) % 3==0:
        a+=(i+1)
    elif (i+1) % 5==0:
        a+=(i+1)
print(a)