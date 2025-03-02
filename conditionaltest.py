this_string = 'hello world'

if this_string == 'Hello World':
    this_string = 'beans'
elif this_string == 'hELLO wORLD':
    this_string = 'potatoes'
elif this_string == 'hello world':
    this_string = 'ground beef'
else:
    this_string = 'corn'
print(this_string)