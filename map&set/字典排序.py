dict_num = {1:3,4:5,2:3}
dict_num = sorted(dict_num.items(), key=lambda x:x[0], reverse = True)
print(dict_num) #[(4, 5), (2, 3), (1, 3)]
