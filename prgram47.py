numbers = list(map(int, input("Enter number : ").split(',')))
powers_of_2 = list(map(lambda x: 2 ** x, numbers))
print("power of 2 =",powers_of_2)

