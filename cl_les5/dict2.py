
my_dict ={}
test_str = "Hi my name hi hi"
for l in test_str.split():
    if l in my_dict: 
        my_dict[l] = my_dict[l] + 1
    else:
        my_dict[l] = 1

print(my_dict)
