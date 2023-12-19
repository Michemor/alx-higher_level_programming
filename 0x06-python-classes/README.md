# 0x06. Python - Classes and Objects
###### Python OOP
## Learning Objectives
1. Why Python programming is awesome
2. What is OOP
OOP refers to a paradigm in programming known as Object Oriented Programming <br> where we can create objects that model real world entities such as car, person, bank account etc
3. “first-class everything”

4. What is a class
A class is a blueprint we use to create objects. It contains properties and methods we use to create an object.
5. What is an object and an instance
An object is an instance of a class; the same way the logical representation of<br> a house started with a plan, we create objects modelled from a class. <br>
An instance is a term used to refer to an object, more like a synonymn
6. What is the difference between a class and an object or instance
A class is the model or layout of our object. An example case is a person object.<br> A person has properties name, age, gender, nationality and methods, run, walk, speak, eat etc. <br> A class shall contain properties and methods related to a person and we shall create a Person from a class and assign properties to it. <br> A person object cannot exist without a class.
7. What is an attribute
An attribute is a property of an object. As described in the example above, any<br> object has properties which are characteristic to it.
8. What are and how to use public, protected and private attributes
For any class all its members are explicitly public.<br>
To declare an attribute as protected we preceed the atttribute name with one underscore i.e ._attributename
9. What is self
Self is a keyword used to refer to member of the class. i.e for a class Person object,<br> instance attributes are distinguished from class attributes using <br> the self keyword 
10. What is a method
Methods are functions declared within a class
11. What is the special __init__ method and how to use it
Used to initialize properties of a class upon declaring an object
12. What is Data Abstraction, Data Encapsulation, and Information Hiding
Data Abstraction is a technique in OOP and is achieved through a combination of Data Encapsulation and Information Hiding 
Data Encapsulation is the wrapping up of data fields and methods within classes
Information hiding refers to a way of showing the necessary details while hiding some meaning.
Data Abstraction is achieved through use of getters, setters and declaration of properties as private and protected <br>
hence they cannot be accessed from outside the class directly.
13. What is a property
A property is a variable used to represent data or attributes within a class.
14. What is the difference between an attribute and a property in Python
15. What is the Pythonic way to write getters and setters in Python
We use decorators @property @attributename.setter to create getter and setters respectively
16. How to dynamically create arbitrary new attributes for existing instances of a class
17. How to bind attributes to object and classes
18. What is the __dict__ of a class and/or instance of a class and what does it contain
19. How does Python find the attributes of an object or class
20. How to use the getattr function
