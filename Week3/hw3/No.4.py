class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)


class Employee(Person):
    def __init__(self,name , age, employID):
        super().__init__(name,age)
        self.name = name
        self.age = age
        self.employID = employID

    def getName(self,Name):
        print(self.name)

    def getAge(self,age):
        print(self.age)

    def getID(self,employID):
        print(self.employID)

#객체생성
em = Employee("IoT",65,2018)
print(em.name, em.age, em.employID)

