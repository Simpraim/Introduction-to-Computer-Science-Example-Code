#Purpose: To add 3 pairs of numbers together
def add_pair():
   num1 = int(input("Give me a number"))
   num2 = int(input("Give me a number"))
   print(f"The sum of {num1} and {num2} is {num1+num2}") 

num_pairs = 0
while num_pairs < 3:
    add_pair()
    num_pairs+=1


