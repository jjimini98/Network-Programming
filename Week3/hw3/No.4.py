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
        self.name = name
        self.age = age
        self.employID = employID

    def getName(self,Name):
        print("제 이름은 "+self.name)

    def getAge(self,age):
        print("제 나이는 ", self.age)

    def getID(self,employID):
        print("제 ID는 ", self.employID)


#객체생성
em = Employee("IoT",65,2018)
print(em.name, em.age, em.employID)
em.getName("IoT")
em.getAge(65)
em.getID(2018)
