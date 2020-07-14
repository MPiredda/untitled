# dictionaries
d = {"a":0,
     "b":0,
     "c":0
     }

print('This is the initial dictionary: ', d)

d['dummy'] = 100  # add new key-value pair
print("... after adding new item: ", d)

# removing the dummy-100 pair
del d['dummy']

items = d.items()  # this is a special class dict_items
print("Items:\n", items)

# cast it to a list
item_list = list(items)
print("Items_list :\n", item_list)

# access the first key-value pair from the list
print("Items element [0]:\n",item_list[0])

# access the first value from the first key-value pair
print("Items [1] value :\n",item_list[0][1])
print("Items [1] key :\n",item_list[0][0])

print("Keys:\n",d.keys())

element = 0
for key in d.keys():
    element = element+1
    print(element, key, ",", d[key])

