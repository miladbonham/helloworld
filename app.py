import random


class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("Woof!")
fido= Dog("Fido", "brown")
print(fido.name)
print(fido.color)
fido.bark()
fido.color


class Superhero:
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def attack(self):
        print("zzzzhoooppp, lazer beem attack !")
Superman= Superhero("Superman","kryptonian")
print(Superman.name)
print(Superman.power)
Superman.attack()
Superman.power


class Student:
    def __init__(self, name):
        self.name=name
    def sayHi(self):
        print("Hi from" +  self.name)
s1=Student( "Amy")
s1.sayHi()

class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    class Cat():
        def purr(self):
            print("Purr...")
    class Dog():
        def bark(self):
            print("Woof!")
fido=Dog("Fido","brown")
print(fido.color)
fido.bark()


class Wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark1(self):
        print("Grr...")
class Dog(Wolf):
    def bark(self):
        print("Woof!")
husky=Dog("Max","grey")
husky.bark()
husky.bark1()

class A:
    def method(self):
        print(1)
class B(A):
    def method(self):
        print(2)
B().method()

class A:
    def spam(self):
        print(1)
class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()


class Vector2D:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
first= (Vector2D(5,7))
second= (Vector2D(3,9))
result= first + second
print (int((result.x)))
print (int((result.y)))


class SpecialString:
    def __init__(self,cont):
        self.cont= cont
    def __truediv__(self, other):
        line= "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])
spam= SpecialString("spam")
hello= SpecialString("Hello World!")
print(spam/hello)

class SpecialString:
    def __init__(self,cont):
        self.cont= cont
    def __gt__(self, other):
        for index in range (len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result+= ">" + other.cont[index:]
            print(result)
spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs


class VagueList:
    def __init__(self,cont):
        self.cont= cont
    def __getitem__(self, index):
        return self.cont[index + random.randint(-1,1)]
    def __len__(self):
        return random.randint(0, len(self.cont)*2)
vague_list= VagueList(["A","B","C","D","E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])


class SpecialString2:
    def __init__(self,cont):
        self.cont=cont
    def __truediv__(self, other):
        line= "=" * len(other.cont)
        return "\n".join([self.cont,line,other.cont])
spam=SpecialString2("Hi there ")
hello=SpecialString2("Beat it")
print(spam/hello)


class Milad:
    def __init__(self,cont):
        self.cont=cont
    def __truediv__(self, other):
        txt= "=" * len(other.cont)
        return "\n".join([self.cont,txt,other.cont])
soop=Milad("Bishoor")
doop=Milad("Na baba")
print(soop/doop)



class Mahyar:
    def __init__(self,cont):
        self.cont=cont
    def __truediv__(self, other):
        bb= "=" * len(other.cont)
        return "\n".join([self.cont,bb,other.cont])
salam=Mahyar("baaaaah baaaah salammmmm")
ok= Mahyar("chetroiiii mashti bagheriiiiii")
print(salam/ok)


class Mili:
    def __init__(self,cont):
        self.cont= cont
    def __truediv__(self, other):
        f= "=" * len(other.cont)
        return "\n".join([self.cont,f,other.cont])
dd= Mili("ya khodaa ")
ff= Mili("chetorii")
print(dd/ff)


class Queue:
    def __init__(self, contents):
        self._hiddenlist= list(contents)
    def push(self,value):
        self._hiddenlist.insert(0, value)
    def pop(self):
        return self._hiddenlist.pop(-1)
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)
queue= Queue([1,2,3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

class Boss(object):
    def __init__(self,name,attitude,behavior,face):
        self.name= name
        self.attitude= attitude
        self.behavior= behavior
        self.face= face
    def get_attitude(self):
        print("Ohh fucking hell!!")
    def get_behavior(self):
        print("Fucked up behavior !! like no one likes him")
    def get_face(self):
        return self.face
b= Boss("name","attitude","behavior","face")
b.get_attitude()
b.get_behavior()


class x_men:
    def __init__(self,name,power,type):
        self.name= name
        self.power= power
        self.type= type
    def get_name(self):
        print("John Logan- AKA: Wolverine")
        return self.name
    def get_power(self):
        print("Atamantiom claws!!! and healing factor!")
        return self.power
    def get_type(self):
        print("Hight geen miutant")
        return self.type
w= x_men("name","power","type")
w.get_name()
w.get_power()
w.get_type()

class Mahi:
    def __init__(self,cont):
        self.cont= cont
    def __truediv__(self, other):
        txt= "="* len(other.cont)
        return "\n".join([self.cont,txt,other.cont])
g= Mahi("eyval")
h= Mahi("Mashalla")
print(g/h)

class Cool:
    def __init__(self,count):
        self.count= count
    def __truediv__(self, other):
        matn= "="* len(other.count)
        return "\n".join([self.count,matn,other.count])
l= Cool("Afarin Milad")
k= Cool("Damet garm Milad")
print(l/k)

class Spam:
    __egg= 7
    def print_egg(self):
        print(self.__egg)
s= Spam()
s.print_egg()
print(s._Spam__egg)

class Rectangle:
    def __init__(self,width,height):
        self.width= width
        self.height= height
    def calculate_area(self):
        return self.width * self.height
    @classmethod
    def new_square(cls,side_length):
        return cls(side_length,side_length)
square= Rectangle.new_square(5)
print(square.calculate_area())

class Person:
    def __init__(self,name):
        self.name= name
    def get_name(self):
        print("John")
        return self.name
    @classmethod
    def sayhi(cls):
     print("Hi")
s= Person("Hi")
s.sayhi()
s2= Person("John")
s.get_name()

class Pizza:
    def __init__(self,toppings):
        self.toppings= toppings
    @staticmethod
    def validate_topping(topping):
        if topping== "pineapple":
            raise ValueError("No pineapple!")
        else:
            return True
ingredients= ["chees","onion","spam"]
if all(Pizza.validate_topping(i)for i in ingredients):
    pizza=Pizza (ingredients)


class Pizza:
    def __init__(self,toppings):
        self.toppings= toppings
    @property
    def pineapple_allowed(self):
        return False
pizza=Pizza(["chees","tomato"])
print(pizza.pineapple_allowed)

class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.email= first + "." + last + "@email.com"
    def fullname(self):
        return "{} {}".format(self.first,self.last)
emp_1=Employee("Milad","Bonham")
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())


class Fakolo:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.gmail= first + "." + last + "@gmial.com"
    def full_name(self):
        return "{} {}".format(self.first,self.last)
p=Fakolo("Mahyar","Agha")
print(p.first)
print(p.last)
print(p.gmail)
print(p.full_name())

class Person:
    def __init__(self,age):
        self.age= int(age)
    @property
    def isAdult(self):
        if self.age>18:
            return True
        else:
            return False

a= Person(22)
print(a.age)


class Pizza:
    def __init__(self,toppings):
        self.toppings= toppings
        self._pineapple_allowed= False
    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed
    @pineapple_allowed.setter
    def pineapple_allowed(self,value):
        if value:
            password= input("Enter the password:")
            if password== "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")
pizza= Pizza(["chees","tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed=True
print(pizza.pineapple_allowed)


































