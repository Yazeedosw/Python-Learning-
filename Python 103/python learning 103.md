# Object Oriented Programming:

| Term              | Definition                                                                                          |
|-------------------|-----------------------------------------------------------------------------------------------------|
| ***Class***       | A general plan or structure that we create objects through.                                         |
| ***Object***      | A real entity created from a Class structure.                                                       |
| ***Attributes***  | Features that describe a Class.                                                                     |
| ***Methods***     | Actions that a Class can perform.                                                                   |


## Create a Class:
```
class Student:
    def __init__(self,name,age,id,grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades

#Medthods:
    def talk(self):
        print('My names is: ',self.name)
#Object:
stud1 = Student('Khaled',18,1002345242,4.3)
print(stud1.name)
stud1.talk()
```
----------------------------------------------------------------------------------
## Self:
```
class Student:
    def talk(self):
        print(self)

stud1 = Student()
stud2 = Student()
stud3 = Student()

stud1.talk()
stud2.talk()
stud3.talk()
```
## Constructor:
```
class Student:
    def __init__(self,name,age,id,grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades


    def talk(self):
        print('My name is ',self.name)

stud1 = Student('Naif',19,10032347473,4.30)
print(stud1.name)

```

## Mini project on  Object Oriented Programming on python103:
```
class Bike:
    def __init__(self, description, cost, sale_price, condition):
        self.description = description
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition
        self.sold = False

    def update_sale_price(self, sale_price):
        if self.sold:
            print('Action not allowed, Bike has already been sold')
        else:
            self.sale_price = sale_price

    def sell(self):
        self.sold = True

# Create a Bike object
bike1 = Bike('Univega Alpina, orange', cost=100, sale_price=500, condition=0.5)

# Update selling price
bike1.update_sale_price(350)

# Sell bike
bike1.sell()
```


## dir Function: 
- wil return the attribute from the object

```
class Student:
    def __init__(self,name,age,id,grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades

    def talk(self):
        print('my name is ',self.name)

std1 = Student( 'Nouf', 21, 'xx00', [95, 98, 99])
std2 = Student( 'Hessah', 19, 'xx01', 86)

print(dir(std2))
```

-----------------------------------------------------------------------------
## Inheritance: 
- instead of type two type of class we can on one class and called paraent class
```
class Vehicle:
    def __init__(self,company,owner,color,current_speed):
        self.company = company
        self.owner = owner
        self.color = color
        self.current_speed = current_speed

    def move(self):
        print('The car has moved')
    def stop(self):
        print('The car has stopped')


#Class car consider as a child of calss vehicle
class Car(Vehicle):
    def display(self):
        print('This is a Car Class')

class Truck(Vehicle):
    def display(self):
        print('This is a Truck Class')

class Bicycle(Vehicle):
    def display(self):
        print('This is a Bicycle Class')

# create object
car1 = Car('Mercides','Khaled','Black',120)
truck = Truck('volove','Mohammed','white',80)
Bicycle1 = Bicycle('lone','fahad','sliver',30)
#to reach to the attribute
print(car1.company)
print(truck.company)
print(Bicycle1.company)
### to reach to the methods
car1.move()
truck.move()
Bicycle1.stop()
```

## Overriding concept :
```
class Animal:
    def __init__(self,name,color):...

    def run(speed):...


    def make_sound(self):
        print('sound ')


class Cat(Animal):
    def make_sound(self):
        print('Mew ')

cat1= Cat('nora','black ')
cat1.make_sound()
```
-----------------------------------------------------------------------------
## Multi-Level Inheritance: the class child take after the parents and the parents take from the grandparents
```
class Grandparent:
    def godisplay (self) :
        print('This is Grandparent class')
class Parent(Grandparent):
    def Podisplay(self):
        print( 'This is Parent class')
class Child(Parent):
    def Codisplay (self) :
        print('This is Child class')

child1 = Child()
child1.Codisplay()
child1.Podisplay()
child1.godisplay()
```
## MRO - Depth-First
```
class A:
    def do_this (self) :
        print( 'Doing this in class A')
class B(A):
    pass
class C:
    def do_this (self) :(
        print( 'Doing this in class C'))
class D(B, C):
    pass

obj = D()
obj.do_this()
```
- in this example the Inheritance will start from class D and by the child (b,c)
- Then he wll go first with (b) then move to A
- after that will see the second child which is (C)

## mro Function:
```
print(D.mro()) #### outcame [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]
```

