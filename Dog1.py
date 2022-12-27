class Dog:
    def __init__(self,n,a):
        self.name= n
        self.age= a
    def show_dog_details(self):
        print(f"Hello! I,m {self.name} and I,m {self.age} year's old")
    def roll_over(self):
        print(f"{self.name} is now rolling over.")
    def sit_down (self):
        print(f"{self.name} is now sitting down.")
    def roll_over1(self,*,string1):
         print(f"{self.name} is now rolling overand {string1}.")
dog1= Dog('milo',7)
dog1.show_dog_details()
dog2=Dog('Tish',4)
dog2.show_dog_details()

dog1.roll_over()
dog1.sit_down()
dog1.roll_over1(string1='sit down')