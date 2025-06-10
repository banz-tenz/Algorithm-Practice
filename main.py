numbers=[1,2,3,4,5,6,7,8,9]
sum = 0
for num in numbers:
    sum += num
print("Find the average value of the array:",sum/len(numbers))

numbers=[1,2,3,4,5,6,7,8,9]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = 0
print("Replace every even number in the array with 0",numbers)

numbers=[1,2,3,4,5,6,7,8,9]
for num in numbers:
    if num % 2 == 1 :
        numbers.remove(num)
print("Remove every odd number from the array",numbers)

numbers=[1,2,3,4,5,6,7,8,9]
count_even = 0
count_odd = 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("Count even number in array",count_even)
print("Count odd number in array",count_odd)


max = numbers[0]
min = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
    if numbers[i] < min:
        min = numbers[i]
print("Maximum in array",max)
print("Minimum in array",min)