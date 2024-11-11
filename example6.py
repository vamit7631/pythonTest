arr = ["Nancy", "Amit", "Ankit","Akhil", "Nancy", "Ankur", "Amit", "Nancy"]

def userArr(arr):
    result = []
    obj = {}
    for i in range(len(arr)):
            name = arr[i]
            if name in obj:
                obj[name]["indexes"].append(i)
                obj[name]["duplicates"] += 1
            else:
                obj[name] = {
                    "name" : name,
                    "indexes" : [i],
                    "duplicates" : 1
                }
            
    return list(obj.values())



print(userArr(arr)) # output [
#    { "name" : "Nancy", "indexes" : [0, 4, 7], "duplicates" : 3}, 
#    { "name" : "Amit", "indexes" : [1, 6], "duplicates" : 2},
#    { "name" : "Ankit", "indexes" : [2], "duplicates" : 1},
#    { "name" : "Akhil", "indexes" : [3], "duplicates" : 1},
#     { "name" : "Ankur", "indexes" : [5], "duplicates" : 1}
#]