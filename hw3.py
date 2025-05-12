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
    else:
        print("Invalid answer please enter either w,r, or exit")