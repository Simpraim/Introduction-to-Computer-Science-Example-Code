def add(num1,num2):
    print(f'The sum of {num1} and {num2} is: {num1 + num2}')
counter = 0
while counter < 3:
    a = int(input("Give me a number"))
    b = int(input("Give me another number"))
    add(a,b)
    counter+=1