import datetime

today = datetime.date.today()
year = today.year


class Company:
    def __init__(self, empname):
        self.empname = empname

    def display(self):
        print("employeename", self.empname)
        print("from parent class")#for inheritance
        #emid = empid
        #print("empid", emid)
    def Address(self):
        return "technopark"
c = Company("UST")
c.display()
class Employee(Company):
    count = 0  #class variable

    def __init__(self,fname, lname, yob,empname):
        self.empname=empname
        self._fname = fname  #instancevariable
        self._lname = lname
        self._age = year - yob
        Employee.count += 1

    def dispemp(self):
        self.display()
        print("fullname", self._fname, "", self._lname)
        print("Age", self._age)
    def Address(self):#polymorphism
        print(super().Address())
        print("Employee Address, santineketan")


e1 = Employee("kavya", "k", 1996,"parag")
e2 = Employee("kav", "ku", 1984,"kk")
e1.dispemp()
e1.Address()
print(Employee.count)  #class var can be calles using class name
