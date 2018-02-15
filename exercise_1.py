import random

avg = 0

#Loop for 1000 tries
for z in range(1000):
    #Define the lists
    matrix = [[0 for x in range(5)] for y in range(100)]
    ranums = [0 for x in range(5)]

    #Append random values for 2 dimention list
    for x in range(100):
        ranums = random.sample(xrange(1,81),5)
        for y in range(5):
            matrix[x][y] = ranums[y]

    selected = [0 for x in range(80)]
    #Append all numbers in random position on list 
    selected = random.sample(xrange(1,81),80)

    final = [0 for x in range(80)]

    #Append 5 numbers in array
    for w in range(5):
        final[w] = selected[w]

    check = True
    lenght = 0

    #Loop stops when is bingo, either check more numbers
    while check:
        for x in range(100):
            for y in range(5):
                ranums[y] = matrix[x][y]
            if set(ranums).issubset(final):
                check = False 
             #   print ranums , final
        lenght = lenght + 1
        final[lenght] = selected[lenght]

    avg = avg + (lenght+1)
print "Average for bingo(1000 tries) is: " , avg/1000