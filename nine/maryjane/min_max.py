array_elements=[]
min_sum=0
max_sum=0

for index in range (5):
    elements = int(input("please enter elements of array"))
    array_elements.append(elements)
array_elements.sort()
print(array_elements)

for i in range (4):
    min_sum+=array_elements[i]
for i in range (1, 5):
    max_sum+=array_elements[i]
print(min_sum, max_sum)