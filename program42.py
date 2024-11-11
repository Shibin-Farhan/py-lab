def is_even(num):
    return num % 2 == 0

def check_number(num):
    if is_even(num):
        return "number is Even"
    else:
        return "number is Odd"

number = int(input("Enter a number: "))
result = check_number(number)
print(result)

