#words in list
"""n = input("Enter words: ")
li = n.split()
print('List:',li)
print('tuple:',tuple(li))
file = open("list.txt", "w")"""



words_lists = input("Enter words (separated by space):").split()
words_tuple = tuple(words_lists)
print(f'list: {words_lists}')
print(f'tuple: {words_tuple}')
with open('qn01_data.txt','w') as data_file:
    data_file.write(f'List:{words_lists}\n')
    data_file.write(f'tuple:{words_tuple}')
with open('qn01_data.txt','r') as data_file:
    line_list = data_file.readline()
    line_tuple = data_file.readline()
    print(line_list)
    print(line_tuple)    



