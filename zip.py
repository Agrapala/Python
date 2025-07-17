name = ['kamal', 'kamal2', 'kamal3']
age = [20, 21, 22]
marks = [100, 99, 98]
details = zip(name, age, marks)
print(details)
print(list(details)) 
print(tuple(details))  # This will raise an error because the iterator is exhausted
print(set(details))  # This will also raise an error for the same rea

unzip = list(zip(*details))
print(unzip)