#x = int(input("How many candies you want?"))

#i = 1
#while(i<=x):
#  print("Candy")
#   i+=1


for i in range(1,101):
    if(i % 3 == 0):
        continue
    print(i)

print("bye")