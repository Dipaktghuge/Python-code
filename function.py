from pydoc import describe


def greet_user():
    """ displays a simple greeting"""
    print("hello")
greet_user()
def greet_user(username):
    """ displays a simple greeting"""
    print(f"hello,{username.title()}")
    return
greet_user("ronaldo")
def describe_pet(animal_type,pet_name):
    print(f"i have a {animal_type} at home")
    print(f"My {animal_type}'s name is {pet_name}.")
    return
describe_pet('scrubbers','mouse')
describe_pet('Dog',pet_name='moti')
def describe_pet(animal_type,pet_name,age):
    print(f"{animal_type}'s name is {pet_name}.S/He is {age}year old.")
describe_pet('cat','Meouw',5)
describe_pet('cat','Meouw','')
def describe_pet(animal_type,pet_name,age=10):
    print(f"{animal_type}'s name is {pet_name}.S/He is {age}year old.")
describe_pet('cat','Meouw',5)
describe_pet('cat','Meouw')
describe_pet('Iguana',3.14159)
describe_pet('virus',['SARS','COV19','MAL'])
describe_pet('virus',['SARS','COV19','MAL'],1)
"happy holiday".index('y')
def describe_pet(animal_type,pet_name,age=10):
    print(f"{animal_type}'s name is {pet_name}.S/He is {age}year old.")
    for i, item in enumerate(pet_name):
        print(f"pet[{i}]-->{item}")
describe_pet('cat','Meouw',5)
describe_pet('cat','Meouw')
def describe_pet(pet_name,age=10,animal_type='puma'):
    print(f"{animal_type}'s name is {pet_name}.S/He is {age}year old.")
    for i, item in enumerate(pet_name):
        print(f"pet[{i}]-->{item}")
describe_pet('Amu',10)
describe_pet('Kha',75,'Blue Whale')
def do_add(num1,num2):
    return num1+num2
num1=10
num2=20
print(f"the sum {num1}and {num2} is {do_add(10,20)}")
def get_formated_name(first_name,middle_name,last_name):
    full_name=f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    return full_name
fn='kung'
mn='panda'
ln='fu'
print(f"The full name is {get_formated_name(fn ,mn ,ln)}")
def get_formatted_name(first_name,middle_name,last_name):
    if last_name==''and middle_name =='':
        full_name=f"{first_name.title()}"
    elif not middle_name==''and last_name=='':
        full_name=f"{first_name.title()} {middle_name.title()}"
    else:
        full_name=f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    return full_name
#print(f"The full name is {get_formatted_name('jackie', 'chan')}.")
print(f"The full name is {get_formatted_name('kung', 'fu', 'panda')}.")
#print(f"The full name is {get_formatted_name('ali')}.")
#print(f"The full name is {get_formatted_name('jimi', 'hendrix')}.")
print(f"The full name is {get_formatted_name('john', 'lee', 'hooker')}.")
def get_formatted_name3(name1, name2='', name3=''):
    if name2 == '' and name3 == '':
        full_name = f"{name1.title()}"
    elif not name2 == '' and name3 == '':
        full_name = f"{name1.title()} {name2.title()}"
    else:
        full_name = f"{name1.title()} {name2.title()} {name3.title()}"
    return full_name

print(f"The full name is {get_formatted_name3('jackie', 'chan')}.")
print(f"The full name is {get_formatted_name3('kung', 'fu', 'panda')}.")
print(f"The full name is {get_formatted_name3('ali')}.")
print(f"The full name is {get_formatted_name3('jimi', 'hendrix')}.")
print(f"The full name is {get_formatted_name3('john', 'lee', 'hooker')}.")
def get_formatted_name2(first_name, last_name, middle_name=''):
    if middle_name == '':
        full_name = f"{first_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    return full_name

print(f"The full name is {get_formatted_name2('jackie', 'chan')}.")
print(f"The full name is {get_formatted_name2('kung', 'fu', 'panda')}.")
print(f"The full name is {get_formatted_name2('kung', 'panda', 'fu')}.")
def make_pizza(*args):
    print(f"These are the pizza toppings:{args}")
    return
make_pizza('cheese')
make_pizza('cheese','pepperoni','paneer')
make_pizza('cheese','pepperoni','paneer','capsicum','onion','bell peppers')
def do_add(*args):
    print(len(args))
    print(type(args),args)
    print(f"Arguments:{args}")
    print(f"Index 0 of args :{args[0]}")
    # return sum ( args)
#do_add(10)
print(do_add(10,20))
print(do_add(10,20,30))
print(do_add([10,20,30,40]))
t1=10,
type(t1)
print(type(t1))
print(t1)
def make_pizza(size,*args):
    print(f"Make a {size} inch pizza wih these toppings:{args}")
    return
make_pizza('cheese')
make_pizza(8,'cheese','pepperoni','paneer')
def build_profile(fn,ln,** profile):
    pass
def contact_profile(**kwargs):
    print(len(kwargs))
    print(type(kwargs))
    print(kwargs)
contact_profile(
    first_name="Amar",
    last_name="Akbar",
    mobile=987654321,
    email="amar@akbar.com"
)
def contact_profile1(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
contact_profile1(
first_name = "Amar",
last_name = 'Akbar',
mobile=987654321,
email = "amar@akbar.com"
)
def build_profile(first_name, last_name, **profile):
    profile['fn'] = first_name
    profile['ln'] = last_name
    return profile

sr_profile = build_profile(
    'Srinivasan', 'Ramanujam',
    interests = 'Mathematics',
    friend = 'Hardy',
    number = 1729
)

print(sr_profile)
def f1(x=2):
    print(f"inside fuction:{x}")
f1(10)
# only keyword ags after *
def f2(*,x=2):
    print(f"Inside function f2 : {x}")
f2(x=10)
#f2(10)
def f2_1(x=3):
    print(f" Inside f2_1:{x}")
f2_1()
f2_1(10)
f2_1(x=100)
def f2_2(a,*,y=2,x=3):
    print(f" Inside f2_2:{x}")
f2_2(10,y=20,x=30)
f2_2(a=40,y=50,x=60)
def f2_3(*,y=2,x=2):
    print(f"Inside f2_3:{y},{x}")
#f2_3(10,20)
f2_3(y=10,x=20)
def f3(*, x):
    print(f"Inside f3: {x=}")

f3(x=10)
def f6(*args,x):
    print(f"inside f6:{args},{x=}")
f6('Violet', 'Indigo', 'Blue', 'Green', x=4)
def evaluate_quadratic(a,b,c):
    return lambda x: a*x**2+b*x+c
q1=evaluate_quadratic(1,2,3)
print(q1(0))
print(q1(2))
print(q1(1))
def build_quadratic(a,b,c):
    return lambda x: a*x**2+b*x+c
q1=build_quadratic(1,2,3)
print(q1(0))
def total(a,b):
    sum1=a+b
    return sum1
t= total(100,49)
print(f"sum of 100 and 49:{t}")
def f1(x):
    return 3*x+1
print(f1(10))
print(type(f1))
