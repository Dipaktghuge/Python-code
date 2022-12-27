
def remove_odd(s1):
    str_s1=str(s1)
    return str_s1[1::2]
input="abcdef"
print(f"original:{input}")
print(f"odd character removed:{remove_odd(input)}")
def remove_odd(s1):
    str_s1=str(s1)
    return str_s1[::2]
input="Hello Evryone"
print(f"original:{input}")
print(f"odd character removed:{remove_odd(input)}")
def fifth_next(a):
    eng_ab="abcdefghijklmnopqrstuvwxyz"
    pos= eng_ab.index(a)
    pos=(pos+1)%len(eng_ab)
    return eng_ab[pos]
a="a"
a="x"
a="z"
print(f"next charter to {a} in the english alphabet is:{fifth_next(a)}")
def fifth_next(a):
    eng_ab="abcdefghijklmnopqrstuvwxyz"
    pos= eng_ab.index(a)
    pos=(pos+5)%len(eng_ab)
    return eng_ab[pos]
a="a"
# a="x"
# a="z"
print(f"next charter to {a} in the english alphabet is:{fifth_next(a)}")
def fifth_next(a,n):
    eng_ab="abcdefghijklmnopqrstuvwxyz"
    pos= eng_ab.index(a)
    pos=(pos+n)%len(eng_ab)
    return eng_ab[pos]
a="a"
n=13
# a="x"
# a="z"
print(f"{n}next charter to {a} in the english alphabet is:{fifth_next(a,13)}")
def html_tags(input_string,tag):
    return f"<{tag}>{input_string}</{tag}>"
tag='i'
input_string="good morning"
print(f"{tag} {input_string} : {html_tags(input_string,tag)}")
def insert(string1,string2):
    mid=len(string1)//2
    part1=string1[:mid]
    part2=string1[mid:]
    new_string=f"{part1}{string2}{part2}"
    return new_string
string1="HelloWorld"
string2=", "
print(f"{insert(string1,string2)}")
def magic_number():
  for i in range (1,9999999):
    str_i=str(i)
    rot_i=int(str_i[1:]+str_i[0])
    if rot_i/i==3.5:
        return i
print(f"magic number is: {magic_number()}")
