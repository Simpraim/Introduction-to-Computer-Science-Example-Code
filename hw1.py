#Ask for input and store in a variable. This input will come in as a string
#Convert that string to a number
#Add 37 to that number
#Print the results (might need to convert again)
def get_future_age(age_parameter):
    new_age = age_parameter + 37
    return new_age
age = int(input("What is your age"))
bob = get_future_age(age)
with open('homework1output.txt','x') as my_file:
    my_file.write(f'You will be {age+37} years old in 37 years')
