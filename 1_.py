# # functions are ways to wrap your code 
# #into reuseable units
# # function = a block of resuable code
#                 #place() after the function name to invoke it
# def happy_birthday(name, age):  #parameter, placeholders to make the function                  #define the function
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print(f"Happy birthday to {name}!")        
#     print()

# happy_birthday("bro", 20) 
# happy_birthday("steve", 30)
# happy_birthday("joe", 40 ) #argument when you call the function         #invoke the function 

# def display_invoice(username, amount, due_date):
#    print(f"Hello {username}")
#    print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("BroCode", 42.50, "01/02")
# display_invoice("JoeSchmo", 100.99, "02/03")


def add (x,y):
   z=x+y
   return z

def subtract (x,y):
   z=x-y
   return z

def multiply (x,y):
   z=x-y
   return z

def divide (x,y):
   z=x/y
   return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")
print(full_name)
