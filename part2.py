names = ["Bob", "Stephen","Steben","George", "Dr. Doom", "Max","Ryan","Jericho","Abe", "Rainbow Dash"]
for child in names:
    if len(child) > 5:
        names.remove(child)
    elif len(child) < 5:
        print(child.capitalize())
    else:
        continue
print(names)