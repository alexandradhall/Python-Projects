largest = None
smallest = None
fval = 0.0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fval = int(num)
    except:
        print('Invalid input')
    if largest is None:
        largest = fval
    elif fval > largest:
        largest = fval
    if smallest is None:
        smallest = fval
    elif fval < smallest:
        smallest = fval
    

print("Maximum is", largest)
print("Minimum is", smallest)