#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            result += char
    return result
if _name_ == "_main_":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
