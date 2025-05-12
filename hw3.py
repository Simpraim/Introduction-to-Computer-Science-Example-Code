<<<<<<< HEAD
import os
exit = False
while exit==False:
    answer = input("Welcome to the Notebook app \n" \
    "w - write a note \n" \
    "r - read a note \n" \
    "exit - leave the app")
    if answer == 'w':
        #ask for filename to create
        #create a filename (That doesn't already exist)
        #(In a loop) ask for a note, then ask if they want to add more to the note
        #Ask if they want to create another note
        pass
    elif answer == 'r':
        i_want_to_read = True
        while i_want_to_read == True:
            #ask for filename
            #check for filename
            #if it exists print it out
            ans = input("Do you want to read another file?")
            if ans == 'no':
                break
            pass
    elif answer == 'exit':
        exit = True
=======
answer = 'yes'
while answer == 'yes':
    age = int(input("enter your age: "))
    if age < 0:
        print('it\'s invalid response')
        continue
    elif age <= 25:
        print("youngin")
    elif age <= 55:
        print("You're getting up there")
    elif age >= 56:
        print("How was it going to school with the dinos??")
    answer = input("would you like to enter another age?")
    if answer == 'yes':
        continue
>>>>>>> 4ca46d12b8fe69e836be931704515a085a19ea69
    else:
        print("Invalid answer please enter either w,r, or exit")