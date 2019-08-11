numbers = input("Type in: ")
odd_list = [i for i in numbers.split(',') if (int(i) % 2 != 0)]
print((" ").join(odd_list))
