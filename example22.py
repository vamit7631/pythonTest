# find unique numbers from list
input = [1, 2, 1, 1, 3, 4, 3, 3, 5]
output1 = []
for i in input:
    if i not in output1 :
        output1.append(i)
        

print(output1,"=========================1")

###########################################################

output2 = list(set(input))
print(output2,"=========================2")