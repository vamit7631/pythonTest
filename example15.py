arr = [1,2,3,4,5,6]
# list comprehension
result1 = ["Even" if x % 2 == 0 else x for x in arr]
# Lambda
result2 = [(lambda x : "Even" if x % 2 == 0 else x)(x) for x in arr]

# map function
result3 = list(map(lambda x: "Even" if x % 2 == 0 else x, arr))

print(result3)










#output final_list = [1, "Even",3,"Even",5,"Even"]
#using lambda , map , list comprehension



# a,b,c  = (0,1,2,3,(4,5,6),7,8)[::3]

# print(a)
# print(b)
# print(c)
# please find value of abc






#input provided by the user not in function
# a = input("Please enter the number")

# def printvalues(a,b,c):
#     sum = a + b + c
#     print(sum)

# print(printvalues(3, 5, 6))






# please write generator function to print 1 to 10 number