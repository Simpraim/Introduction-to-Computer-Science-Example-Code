user_file = input("would you like to create a new file (please answer in yes/no): ")
while user_file == "yes":
    name_file = input("what would you like to like to name your file: ")
    text_ = input("type what you want in the note here: ")
    print(text_)
    with open(name_file,"x") as new_file:
        new_file.write(text_)
    new_user_file = input("would you like to create another new file: ")
    if new_user_file == "yes":
        user_file == "yes"
    else:
        break
name_read_file = input("would you like to read an existining file: ")
while name_read_file == "yes":
    read_file = input("what is the name of the file: ")
    import os 
    command = f"ls {read_file}"
    os.system(command)
    with open(read_file,"r") as openoldfile:
        read = openoldfile.read()
        print(read)
    new_question = input("would you like to read another existining file: ")
    if new_question == "yes":
        continue
    else:
        break