def add_numbers(*args):
    return sum(args)

user_input = input("Enter numbers separated by spaces: ")
numbers = map(int, user_input.split())

result = add_numbers(*numbers)
print("The sum is:", result)

