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



# coffee_prices=[('cappuccino', 1.5),
#                 ('espresso', 1.2),
#                 ('mocha',1.9)]

# def most_expensive_coffee(list_of_prices):
#     highest_price = 0
#     my_most_expensive_coffee =''
#     for coffee, price in list_of_prices:
#         if price> highest_price:
#             highest_price= price
#             my_most_expensive_coffee= coffee
#         else:
#             pass
#     return (my_most_expensive_coffee, highest_price)
# print(most_expensive_coffee(coffee_prices))
# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive,
# and False if at least one of the values is negative. 
# Create a list named numbers with positive and negative values.

def all_positives(numbers):
                            # Loop through each number in the provided list numbers
    for num in numbers:
                         # Check if the current number is negative
        if num < 0:
                              # If any number is negative, return False
            return False
                                    # If no negative number is found, return True
    return True


numbers = [17, -9, 1, 6]


# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 
# and less than 1000, and returns the result of said sum. 
# Create a numbers variable, storing a list of numbers so we can test it.

def sum_less(numbers):
  
    total_sum = 0
    
                        # Loop through each number in the provided list numbers
    for num in numbers:
                         # Only add numbers that are between 0 and 1000 
        if 0 < num < 1000:
            total_sum += num
    
                     # Return the final sum after going through all numbers
    return total_sum

#                                list to test the function
numbers = [54, 1300, 240, -19, 727]


# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers),
# and returns the result of said count.

def count_even(numbers):
     #variable to keep track of the even number count
    even_count = 0
    
                                      # Loop through each number in the list 
    for num in numbers:
        # Check if the current number is even (divisible by 2)
        if num % 2 == 0:
            even_count += 1
    
                             # Return the count of even numbers 
    return even_count

# Example list to test the function to see if it is working properly
numbers = [1, 2, 3, 4, 5, 6, 7, 8]