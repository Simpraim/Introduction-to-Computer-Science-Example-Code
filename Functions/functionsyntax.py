#The def keyword defines a function
#It is then followed by however you want to name your function
#If your program has parameters, 
# the number and name of parameters is wrapped in () 
#and followed by a :
#On an indented block, you have your function body
#Finally, if your function returns a value, you use the 
#return keyword followed by the value you want to return
def add(parameter1,parameter2):
    return_value = parameter1 + parameter2
    
    return return_value

my_return_value = add(1,22)
my_return_value2 = add(3,22)
my_return_value3 = add(1,32)
my_return_value4 = add(1,42)
print(my_return_value)