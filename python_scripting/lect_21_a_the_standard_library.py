import math

print("\n Demonstrate how to calculate factorial of an integer\n\n")
print("\n For now calculating factorial of each element in list [1, 2, 3, 4]")

num_list = [1, 2, 3, 4]
num_list_fact = []

for i in num_list:
    num_list_fact.append(math.factorial(i))

print(num_list_fact)
