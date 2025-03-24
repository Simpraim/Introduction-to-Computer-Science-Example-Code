def is_palindrome(my_string):
    reverse_string_list = list(my_string).reverse()
    reverse_string = str(reverse_string_list)
    if reverse_string == my_string:
        print(f"The string {my_string} is a palindrome")
    elif reverse_string != my_string:
        print(f"The string {my_string} is not a palindrome")

user_string = input("Give me a string")
is_palindrome(user_string)