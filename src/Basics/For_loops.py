# for loops

li = ['a', 'b', 'c', 'd']

for elem in li:
    print(elem)

# C-style recovering of element indexes
idx = 0
for elem in li:
    print(idx, elem)
    idx = idx + 1

print("Index, value:")
# Python style
for idx, elem in enumerate(li):
    print(idx,"   ", elem)

