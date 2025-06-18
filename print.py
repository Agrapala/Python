print ("Helloo world");
print("Helloo \nworld");
print("Helloo \rworld");
print("Helloo \tworld");
print("Helloo\bworld");

name = "samitha";
age = 23;

print(name);
print(age);
print(name, end='-');
print(age, end='');

print("He is "+name+ " his age is "+ str(age))
print("He is %s,his age is %d" %(name,age))
print("He is {}.his age is {}".format(name, age))
print(f"He is {name}.his age is {age}")