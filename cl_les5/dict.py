# Напишите программу, которая принимает на вход строку, и
# отслеживает, сколько раз каждый символ уже встречался


#my_dict={}
#data = input()

#for i in range(len(data):
 #   my_dict =

test_str = input()
my_dict={}
for l in test_str:

    if l in my_dict:  #буква уже в словаре
        my_dict[l] = my_dict[l] + 1
    else:
        my_dict[l] = 1  #буква не в словаре

print(my_dict)

