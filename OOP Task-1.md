***<span style="font-size: 25px">OOP:</span>***

`Object oriented programming  is a programming paradigm which is based on object and classes.`

---

***<span style="font-size: 25px">Class:</span>***

- `Class is a blueprint that defines properties and behavior of an object.`
- `With the help of class we can create multiple instances.`
- `We are using class to solve real world problems.`
- `It's following DRY(Don't Repeat Yourself) and Single Responsibility principle.`

  ```python
  Syntax:                 
  class ClassName:
      def __init__(self, parameters):
          # Constructor (initializes the object)
          self.attribute = parameters
  
      def method_name(self):
          # Method (function inside the class)
          print("This is a method inside the class")
  
  ```

  ---

  ***<span style="font-size: 25px">Object:</span>***.
- `Object is the instance of class.`
- `object have attributes and behavior that determine their functionality. `
- `Objects are stored in the heap memory and managed by Python's Garbage Collector.`

  ```python
  Syntax:
  class ClassName:
      def __init__(self, parameters):  # Constructor
          self.attribute1 = value1
          self.attribute2 = value2
  
  # Creating an instance or object of a class
  object_name = ClassName(arguments)
  
  ```

  ---

  ***<span style="font-size: 25px">Attributes:</span>***
- `Attributes means  variables which are present inside the class.`

  ```python
  example:
  class ClassName:
      # Class Attribute (Shared by all objects)
      class_attribute = value  
  
      def __init__(self, param1, param2):
          # Instance Attributes (Unique to each object)
          self.attribute1 = param1  
          self.attribute2 = param2  
  ```

  ---

  ***<span style="font-size: 25px">Methods / Behavior:</span>***
- `Method are those functions which are present inside the class.`

  ```python
  example:
  class Person:
      def __init__(self, name):  
          self.name = name  
  
      def greet(self):  # Method
          return f"Hello, my name is {self.name}!"
  
  # Creating an instance
  p1 = Person("Ram")
  
  # Calling the method
  print(p1.greet())  # Output: Hello, my name is Ram
  
  ```

  ---

  ***<span style="font-size: 25px">Constructor:</span>***
- `Constructor is a special method in a class which automatically executed when object is created.`
- `It is used for initialization of variables.`

  ```python
  synatx:
  class ClassName:
      def __init__(self, param1, param2):  # Constructor
          self.attribute1 = param1
          self.attribute2 = param2
  
  # Creating an object
  object_name = ClassName(value1, value2)
  
  ```

  ***<span style="font-size: 19px">Self in Constructor:</span>***
- `Self Keyword is used to refer the current object.`
- `It helps to access attributes and methods based on object.`
- `We can use different word but it is not best practices.`
- `If we are not using self, attributes won’t be stored in the object!`

  ---

  ### ***<span style="font-size: 25px">Types of Variables in Python:</span>***

  Python has four main types of variables based on their scope and usage:
- **Instance Variables**:

  ` Instance variable stored or defined inside the __init__() method using self.`

  `Each object gets its own copy of instance variables.`

  ```python
  class Student:
      def __init__(self, name, age):
          self.name = name  # Instance Variable
          self.age = age    # Instance Variable
  
  # Creating two objects
  s1 = Student("Alice", 20)
  s2 = Student("Bob", 22)
  
  print(s1.name, s1.age)  # Output: Alice 20
  print(s2.name, s2.age)  # Output: Bob 22
  
  ```
- **Class Variables**

  `It is defined outside of the __init__() method but inside the class`

  `Same value for all objects (shared variable).`

  ```python
  class Employee:
      company = "Google"  # Class Variable
  
      def __init__(self, name):
          self.name = name  # Instance Variable
  
  e1 = Employee("Alice")
  e2 = Employee("Bob")
  
  print(e1.name, e1.company)  # Output: Alice Google
  print(e2.name, e2.company)  # Output: Bob Google
  
  # Changing class variable
  Employee.company = "Microsoft"
  
  print(e1.company)  # Output: Microsoft
  print(e2.company)  # Output: Microsoft
  
  ```
- **Local Variables** 

  `It is declared inside a function and accessible only within that function.`\
  \
  `Cannot be accessed outside the function.`

```python
def my_function():
    x = 10  # Local Variable
    print(x)

my_function()  # Output: 10
# print(x)  # ❌ Error: x is not defined outside the function
```

- **Global Variables**

  `It is defined outside all the functions and classes.`

  `Accessible inside and outside functions using the global keyword.`

  ```python
  x = 100  # Global Variable
  
  def my_function():
      global x  # Using global variable inside function
      x = x + 10
      print("Inside function:", x)
  
  my_function()  # Output: Inside function: 110
  print("Outside function:", x)  # Output: Outside function: 110
  ```

  ---

  ***<span style="font-size: 25px">Some Important Questions:</span>***

  **<span style="font-size: 17px">Q1. Can we define a class without using class keyword in python ?</span>**

  Yes, it is possible to define a class without using class Keyword in python using t **type()** function **and  metaprogramming** technique

  **Metaprogramming:**  So, metaprogramming is when a program **modifies itself** or **creates new code dynamically**. Or **our code can write or change itself** dynamically!

  ```python
  Method 1 :
  ClassName = type("ClassName", (BaseClass,), {"attribute": value, "method": function})
  ```

  ```python
  Method 2 :
  import types
  ClassName = types.new_class("ClassName", (BaseClass,), {})
  ```

  ```python
  Method 3 :
  class Meta(type):
      def __new__(cls, name, bases, dct):
          dct["attribute"] = value
          return super().__new__(cls, name, bases, dct)
  
  ClassName = Meta("ClassName", (BaseClass,), {})
  ```

**<span style="font-size: 17px">Q2. we know \_\_</span>*<span style="font-size: 17px">init_\_()</span>*<span style="font-size: 17px"> constructor used for initialize the object attributes and what happens when we don't use this \__init</span>**<span style="font-size: 17px">\_\_()</span> **<span style="font-size: 17px">constructor?</span>**

If we don't define a constructor in a class then python automatically  provides a **default constructor.**

we must manually assign variables or after after creating an object.

***<span style="font-size: 17px">Q3. What will happen when we assign one object to another object?</span>***

When we assign one object to another, both variables refer to the same memory location. Python does not create a new copy of the object; instead, it creates a new reference to the same object.

**Warning:** Modifying one object affects both, which can cause unexpected bugs.

```python
class Car:
    def __init__(self, model):
        self.model = model

car1 = Car("Tesla")
car2 = car1  # Assigning car1 to car2

print(car1.model)  # Output: Tesla
print(car2.model)  # Output: Tesla
car2.model = "BMW"
print(car1.model)  # Output: BMW (Changed!)
print(car2.model)  # Output: BMW
```

**<span style="font-size: 17px">Q4. Does a class get stored in memory even before we create an object?</span>**

Yes, a class get stored in memory even before we create an object.

Python stores metadata of the class (like method names and variables) in a hidden dictionary called `__dict__`. You can check it using:

```python
class Sample:
    x = 10

print(Sample.__dict__)  # Shows internal storage of the class
```

\
**<span style="font-size: 17px">Q5. What is instance dictionary?</span>**

In Python, each object (instance) has its own dictionary, which stores instance attributes

This dictionary is called the **Instance Dictionary** and is stored in `__dict__`.

```python
class Car:
    def __init__(self, model, color):
        self.model = model  # Instance attribute
        self.color = color  # Instance attribute

car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Blue")

# Printing instance dictionaries
print(car1.__dict__)  # {'model': 'Tesla', 'color': 'Red'}
print(car2.__dict__)  # {'model': 'BMW', 'color': 'Blue'}
```

**<span style="font-size: 17px">Q6. What happen when we create  an object of class  inside \__init_\_() and then, define the same object  outside the class?</span>**

This will cause infinite recursion because each time an object is created, it creates another object inside itself, leading to an endless loop.

```python
class Test:
    def __init__(self):
        print("Inside __init__()")
        self.inner_obj = Test()  # Creating an object inside __init__()

# Creating an object outside
obj1 = Test()
```

**<span style="font-size: 17px">Q7. Why do we use the dot operator (.) to call an object in Python? Is it possible to call an object like this: variables_module(display_info())?</span>**

No!, You cannot call an object's method like variables_module(display_info()).

In Python, the dot (.) operator is used to access attributes (variables) and methods (functions) of a class or module. It helps in object-oriented programming (OOP) to define and access object properties.

It follow the oop structure.

**<span style="font-size: 17px">Q8. Can we create a class with no attribute but only methods? If yes, then how is it useful?</span>**

Yes we can create a class with no attribute but only methods in case we want to display fixed messages to the user.

```python
class Greetings:
    def say_hello(self):
        return "Hello! Hope you have a great day! 😊"

    def say_good_morning(self):
        return "Good morning! Have a wonderful start to your day! ☀️"

# Creating an object
greet = Greetings()

# Calling methods using the object
print(greet.say_hello())         # Output: Hello! Hope you have a great day! 😊
```

\
Q9. How can we ensure that an attribute can only be accessed within the class?

We can make the attribute with the help of private access modifier.

For making private we can use double underscore before attribute name.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (name mangling applied)

    def get_balance(self):
        return self.__balance  # Accessible within the class

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount}. New balance: {self.__balance}"

# Creating an object
account = BankAccount(1000)

# Accessing private attribute directly (❌ This will fail)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Accessing via method (✅ Correct way)
print(account.get_balance())  # Output: 1000

# Depositing money
print(account.deposit(500))  # Output: Deposited 500. New balance: 1500
```

\
A better approach is using **property decorators** to restrict modification but allow controlled read which means that we can only read but not make changes.

```python
class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute

    @property
    def name(self):
        return self.__name  # Read-only access

# Creating an object
p = Person("Alice")

# Accessing name (Allowed ✅)
print(p.name)  # Output: Alice

# Modifying name (Not Allowed ❌)
# p.name = "Bob"  # AttributeError: can't set attribute
```

**<span style="font-size: 17px">Q10. Does a Class really Reduce Lines of Code?</span>**

Not Really because when we define the class  it will consume multiple lines for code but it allow us to follow DRY principle and single responsibility principle.

```python
# Using a class (Object-Oriented Programming)
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Creating multiple student objects
student1 = Student("Alice", 20, "A")
student2 = Student("Bob", 21, "B")

# Displaying student details
student1.display()
student2.display()
```