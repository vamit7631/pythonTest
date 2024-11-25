arr = ["Nancy", "Amit", "Ankit","Akhil", "Ankur", "Anu", "nikhil"]
arr = arr[-1:] + arr[:-1]
print(arr) # output  ['nikhil', 'Nancy', 'Amit', 'Ankit', 'Akhil', 'Ankur', 'Anu']


arr = arr[1:] + arr[:1]
print(arr) # output ['Amit', 'Ankit', 'Akhil', 'Ankur', 'Anu', 'nikhil', 'Nancy']