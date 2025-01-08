# def check_3_digits(number):
#     return number in range(100,1000)

# result= check_3_digits(673)
# print(result)

# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100,1000):
#             return True
#     else:
#      pass

# result= check_3_digits([55,99,6000])
# print(result)

# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100,1000):
#             return True
#     else:
#      return False

# result= check_3_digits([55,99,600])
# print(result)


# def check_3_digits(list1):
    
#     three_digits_list =[]
    
#     for n in list1:
#         if n in range(100,1000):
#            three_digits_list.append(n)
#     else:
#         pass
#         return False
# result= check_3_digits([555,99,600])
# print(result)



coffee_prices=[('cappuccino', 1.5),
                ('espresso', 1.2),
                ('mocha',1.9)]

def most_expensive_coffee(list_of_prices):
    highest_price = 0
    my_most_expensive_coffee =''
    for coffee, price in list_of_prices:
        if price> highest_price:
            highest_price= price
            my_most_expensive_coffee= coffee
        else:
            pass
    return (my_most_expensive_coffee, highest_price)
print(most_expensive_coffee(coffee_prices))
# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

def all_positives(numbers):
    for num in numbers:
        if num < 0:
            return False
    return True

numbers = [17, -9, 1, 6]

# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

def sum_less(numbers):
    total_sum = 0
    
    for num in numbers:
        if 0 < num < 1000:
            total_sum += num
    
    return total_sum

numbers = [54, 1300, 240, -19, 727]

# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.

def count_even(numbers):
    even_count = 0
    
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
    
    return even_count

numbers = [1, 2, 3, 4, 5, 6, 7, 8]