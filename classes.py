##################################
class Person:
      def __init__(self, _name, _age):
          self.name= _name
          self.age= _age
      def sayHi(self):
          print("hello my name is " + str(self.name) +  " i am " + str(self.age) + " years old")
Person1 = Person("Mathew",19)
Person1.sayHi()


Person2 = Person("Crystal",19)
Person2.sayHi()

class employee:
      def __init__(self,_name,_salary):
          self.name = _name
          self.salary = _salary
      def sayHi(self):
          print("employee name is "  + str(self.name) ,"into computer science/IT"  ,"working with Microsoft" , "and he earns " , int(self.salary))
employee = employee("Mathew",200000)
employee.sayHi()



class Vehicle :
      def __init__(self, mileage,max_speed):
         self.mileage = mileage
         self.max_speed = max_speed
      def sayHi(self):
          print("The vehicles mileage is "  , str(self.mileage) ,  "max speeed is" , str(self.max_speed))
Vehicle = Vehicle(23000,64000)
Vehicle.sayHi()


   
