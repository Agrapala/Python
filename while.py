i = 0 
sum = 0 
while(i<2):
    number = int(input("Enter number: "))
    sum = sum + number 
    i +=  1 
print("Total: "+ str(sum))

for x in range(1,6):
    if (x == 3):
        continue
    print(x)

print(" ")

y= 0 
while(y < 5):
    y +=1
    if (y == 3):
        continue
    print(y)
print(" ")
v= 0
while(v < 5):
    v +=1
    if (v ==3):
        break
    print(v)