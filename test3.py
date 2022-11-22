
measurements = [1, 5, -12, 4, 5, 645, 12, 456, -94, 123,
                7, 9, 0, 1, 456, -43, 38, -28, 0, 1, 6, 12, 4, 12, 54]

k = 50

count = 0
for i in measurements:
    if i > k:
        count = count + 1

print("the amount of numbers greater then 50 in this array is " + str(count))


for i in measurements:
    count = 0
    hundred = 100
    if i > hundred:
        amount = count + 1
print("the amount of numbers greater then 100 are " + str(amount))


for value in measurements:
    negatives = 0
    fifty = 0
    hundred = 0
    if value in measurements:
        if value < 0:
            negatives += 1
        if value > 50:
            fifty += 1
        if value > 100:
            hundred += 1

print("Amount of numbers greater then a negative: " + str(negatives))
print("Amount of numbers greater then 50: " + str(fifty))
print("Amount of numbers greater then 100: " + str(hundred))
