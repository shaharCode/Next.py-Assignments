
import functools
import operator

with open("names.txt", 'r') as file: names = file.read().split()
# 1
print(max(names, key=len))
# 2
print(functools.reduce(operator.add, map(len, names)))
# 3
print('\n'.join([name for name in names if len(name) == min(map(len, names))]))
# 4
new_file = open("name_length.txt", "w")
[new_file.write(str(len(name))+"\n") for name in names]
# 5
len_input = int(input("Enter name length: "))
print('\n'.join([name for name in names if len(name) == len_input]))

