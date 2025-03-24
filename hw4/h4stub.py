#Do something 10 times
a = 1
num_list = []
even_list = []
while a < 11: 
    num = input("Enter a number")
    num = int(num)
    num_list.append(num)  
    a = a + 1

for item in num_list:
    if item%2 == 0:
        num_list.remove(item)
        even_list.append(item)
print(f'The sum of the even numbers is: {sum(even_list)}')
print(f'The sum of the odd numbers is: {sum(num_list)}')