answer = 'yes'
while answer == 'yes':
    age = int(input("enter your age: "))
    if age < 0:
        print("invalid response")
        continue
    elif age <= 25:
        print("youngin")
    elif age <= 55:
        print("You're getting up there")
    elif age <= 56:
        print("How was it going to school with the dinos??")
    answer = input("would you like to enter another age?")
    if answer == 'yes':
        continue
    else:
        break