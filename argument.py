def details(name, age):
    print(f'My name is {name}. My age is {age}')

details("samitha", 23)

def total(*marks):
    total=0
    for i in marks :
        total += i
    print(total)

total(95,95,8,5,8,5,685)

def dic(**num):
    print(num)

dic(A=20,B=53)