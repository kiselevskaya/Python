largest = None
smallest = None
sum = 0
count = 0
while True:
    num = raw_input("Enter a number: ")

    if num == "done" : break
    if len(num) < 1 : continue

    try:
        num = int(num)
    except:
        print "Invalid input"
        continue

    sum = sum + num
    count = count + 1

    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print sum, count, 'average', float(sum) / count
print "Maximum is", largest
print "Minimum is", smallest
