class employee:
    def __init__(self,name, age, work,salary):
        self.name= name
        self.age= age
        self.work = work 
        self.salary = salary

person1 = employee("Silver",20,"Coding","Currenty no salary")
print(person1.name)
print(person1.age)
print(person1.work)
print(person1.salary)