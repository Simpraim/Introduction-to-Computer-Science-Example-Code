#The def keyword defines a function
#It is then followed by however you want to name your function
#If your program has parameters, 
# the number and name of parameters is wrapped in () 
#and followed by a :
#On an indented block, you have your function body
#Finally, if your function returns a value, you use the 
#return keyword followed by the value you want to return
def function_name(parameter1,parameter2):
    parameter1 = parameter1 + parameter2
    parameter2 = parameter1 - parameter2
    return_value = parameter1 * parameter2
    return return_value

my_return_value = function_name(5,4)
print(my_return_value)