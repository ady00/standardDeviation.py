
import math



import csv
with open('data.csv', newline='') as l:
    reader = csv.reader(l)
    file_data = list(reader)





data = file_data[0]


# mean
def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean




squared_list= []
for number in data:
    a = int(number) - mean(data)
    a= a ** 2
    squared_list.append(a)


sum = 0
for s in squared_list:
    sum = sum + s

#didvide
result = sum/ (len(data)-1)



std_deviation = math.sqrt(result)
print(std_deviation)


