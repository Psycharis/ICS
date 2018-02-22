import random

#Append random values in list, where numbers can exist more than one
num = [random.randrange(-30,31,1) for _ in range(30)]
check = True

for i in range(30):
    for y in range(i+1,30):
	for z in range(y+1,30):
            if num[i] + num[y] + num[z] == 0:
		print "The combination is",num[i],',',num[y],',',num[z]
                check = False
if check:
    print "There is no such combination"
