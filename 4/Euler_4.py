#Find the largest palindrome made from the product of two 3-digit numbers.
palindromes = []
for i in range(100,1000):
    for t in range(100,1000):
        k = i*t
        if k <100000:
            if (int(str(k)[0]) == int(str(k)[-1])) and (int(str(k)[1]) == int(str(k)[-2])):
                palindromes.append(k)
        elif (int(str(k)[0]) == int(str(k)[-1])) and (int(str(k)[1]) == int(str(k)[-2])) and (int(str(k)[2]) == int(str(k)[-3])):
            palindromes.append(k)
palindromes.sort()
print(palindromes[-1])