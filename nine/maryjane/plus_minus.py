
array_element=[]
negative_values=[]
positive_values=[]
zero_values=[]
count =int(input("please enter number of elements in our array"))
for count in range(count):
    element=int(input('please enter number'))
    array_element.append(element)
# print(array_element)
for numbers in array_element:
    if numbers < 0:
        negative_values.append(numbers)
    if numbers > 0:
        positive_values.append(numbers)
    elif numbers == 0:
        zero_values.append(numbers)


print(negative_values, positive_values, zero_values)
print((len(negative_values)/len(array_element)), (len(positive_values)/len(array_element)), (len(zero_values)/len(array_element)))




