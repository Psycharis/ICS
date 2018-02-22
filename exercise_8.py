import random

num = random.sample(range(-30,31),30)
check = True

print "The Random numbers are:\n", num , "\n\n"

for i in range(30):
    for y in range(i+1,30):
	for z in range(y+1,30):
            if num[i] + num[y] + num[z] == 0:
		print "The combination is",num[i],',',num[y],',',num[z]
                check = False
if check:
    print "There is no such combination"
