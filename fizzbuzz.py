import sys

inputs = sys.argv
inputs.pop(0)

for i, item in enumerate(inputs, start=1):
    check = int(item)
    if check % 3 == 0 and check % 5 == 0:
        print("fizzbuzz")
    elif check % 3 == 0:
        print("fizz")
    elif check % 5 == 0:
        print("buzz")
    else:
        print(item)
