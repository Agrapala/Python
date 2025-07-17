for i in range(5):
    for j in range(i+1):
        print("*",end='')
    print()

for i in range(5):
    for j in range(5-i):
        print("*", end='')
    print()

for i in range(5):
    for j in range(4-i):
        print(" ", end='')
    for k in range(2*i+1):
        print("*", end='')
    print()

for row in range(6):
    for column in range(7):
        if row==0 and column%3!=0 :
            print("* ", end='')
        elif row==1 and column%3==0:
            print("* ", end='')
        elif row-column==2 :
            print("* ", end='')
        elif row+column==8:
            print("* ", end='')
        else:
            print("  ", end='')
    print()