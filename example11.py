# Sort objects (string properties, Friend: name, grade) on property. Sort these objects on descending order of grade. 
#     Input: ------ 
#     Aima, A 
#     Arjun, A+ 
#     Iram, B+ 
#     Zia, C 
#     Reah, B 
#     Karan, A 
#     Mithum, B 
#     Ankur, B+ 
#     Output: ------- Arjun, A+ Aima, A Karan, A Ankur, B+ Iram, B+ Reah, B Mithum, B Zia, C


friends = [
    {
        "name": "Aima", 
        "grade": "A"
    },
    {
        "name": "Arjun", 
        "grade": "A+"
    },
    {
        "name": "Iram", 
        "grade": "B+"
    },
    {
        "name": "Zia", 
        "grade": "C"
    },
    {
        "name": "Reah", 
        "grade": "B"
    },
    {
        "name": "Karan", 
        "grade": "A"
    },
    {
        "name": "Mithum", 
        "grade": "B"
    },
    {
        "name": "Ankur", 
        "grade": "B+"
    }
]

# Define grade ranking order
grades = {"A+": 0, "A": 1, "B+": 2, "B": 3, "C": 4}

friends.sort(key=lambda x: grades[x["grade"]])

# Print sorted output
for friend in friends:
    print(f"{friend['name']}, {friend['grade']}")