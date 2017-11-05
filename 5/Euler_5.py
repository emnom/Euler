#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
number = 1
one_to_twenty = [[1],[2],[3],[2,2],[5],[2,3],[7],[2,2,2],[3,3],[2,5],[11],[2,2,3],[13],[2,7],[3,5],[2,2,2,2],[17],[2,3,3],[19],[2,2,5]]
twos = 0
threes = 0
fives = 0
sevens = 0
twos_now = 0
threes_now = 0
fives_now = 0
sevens_now = 0
for a in range(20):
    twos_now = twos
    threes_now = threes
    fives_now = fives
    sevens_now = sevens
    for x in range(len(one_to_twenty[a])):    
        if one_to_twenty[a][x] == 2:
            if twos_now > 0:
                twos_now -= 1
            else:
                number *= 2
                twos += 1
        elif one_to_twenty[a][x] == 3:
            if threes_now > 0:
                threes_now -= 1
            else:
                number *= 3
                threes += 1 
        elif one_to_twenty[a][x] == 5:
            if fives_now > 0:
                fives_now -= 1
            else:
                number *= 5
                fives += 1
        elif one_to_twenty[a][x] == 7:
            if sevens_now > 0:
                sevens_now -= 1
            else:
                number *= 7
                sevens += 1
        else:
            number *= one_to_twenty[a][x]
print(number)