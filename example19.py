input_list = [2, 4, 6, 8, 6]
result1 = []
for x in input_list:
    if input_list.count(x) == 1:
        result1.append(x)
print(result1,"============================1")

############################ With list comphrension ###############################

result2 = [num for num in input_list if input_list.count(num) == 1]
print(result2,"============================2")

############################ Without loop and set ###############################


result3 = list(filter(lambda x: input_list.count(x) == 1, input_list))
print(result3,"============================3")