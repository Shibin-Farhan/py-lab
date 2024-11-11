def sum_of_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

user_input = input("Enter numbers separated by spaces : ")
numbers = list(map(int,user_input.split()))

print(f"Sum of the list is: {sum_of_list(numbers)}")
