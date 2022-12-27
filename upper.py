def print_upper(string1):
    for i,char in enumerate(string1):
        if char.isupper(string1):
            print(f"at{i}:{char}")
    return
print_upper("This Should Has Many Upper Case Letters")
