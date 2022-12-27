def convert(number):
    if number<0 :
        raise ValueError(f" input is invalid : {number}")
    string1=" "
    if number % 2==0:
        string1=f"{string1} rim jhim"
    if number%3==0:
        string1=f"{string1} jai tarang"
    if number % 5==0:
        string1=f"{string1}baadal"
    if number % 7==0:
        string1=f"{string1} chate hain"
    if number % 2 and number % 3 and number % 5 and number % 7 :
        string1=str(number)
    return string1.strip()
print(convert(7))
print(convert(13))
print(convert(15))
print(convert(210))
print(convert(34))
print(convert(-1))