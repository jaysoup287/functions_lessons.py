# *args  = allows you to pass multiple non key arguments
##Kwargs = allows you to pass multiple key word arguments
# *unpacking operator
# 1. positional 2. default 3. keyword 4. ARBITARY

# def add(*nums):
#    total = 0
#    for num in nums:
#        total += num
#    return total

# print(add(1, 2, 3, 4, 5, 6, 2000, 65000, 7000000))


# def display_name(*args):
#    print(f"Hello", end=" ")
#    for arg in args:
#        print(arg, end=" ")

# display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value, end=" ")

# print_address(street="123 Fake St.",
#               pobox="P.O Box 777",
#               city="Detroit",
#               state="MI",
#               zip="54321")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")


# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"