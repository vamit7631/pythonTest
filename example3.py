sampleString = "testString data"

# Convert to lowercase and remove spaces
sample_string = sampleString.lower().replace(" ", "")
print(len(sample_string))

# Count character occurrences
count = {}
for element in sample_string:
    count[element] = count[element] + 1 if element in count else 1

print(count)
