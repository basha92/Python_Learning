Today's learning goals
By the end of today, you should understand:
1. What inheritance is and why we use it.
2. Parent and child classes.
3. How to use super().
4. Method overriding.
5. Multilevel inheritance.
6. When inheritance is useful and when it is not.

Remember:
- Inheritance reuses parent functionality.
- Overriding changes or extends inherited behaviour.
- super() lets you call parent functionality without repeating its code.

Inheritance = Inherit attributes and methods from another class
Helps with code reusability and extensibility.
How to use: class Child(Parent)

super() = Function used in a child class to call methods from a parent class (superclass).
Allows you to extend the functionality of the inherited methods

multiple inheritance = inherit from more than one parent class
C(A, B)

multilevel inheritance = inherit from a parent which inherits from another parent
C(B) <- B(A) <- A

In exercise 3, called Person, Patient in the surgical class and got mro error. Below is the rule to avoid:
Rule of thumb: with multiple bases, list the most specific (lowest in the hierarchy) 
first and the most general last. 
Multiple inheritance like (A, B) is meant for unrelated classes, 
not for a class and its own parent.
for related inheritance, call the immediate parent and that should be enough.

Build a Medical Device Component Management System

Suggested folder structure:
Day_12/
│
├── main.py
├── person.py
├── patient.py
├── cad_part.py
└── README.md
Your program should:
1. Create a common Person class.
2. Create a Patient class that inherits from Person.
3. Create a SurgicalPatient class that inherits from Patient.
4. Create a CADPart class.
5. Create FemoralPart and TibialPart child classes.
6. Use super() for shared initialization.
7. Override at least one method.
8. Create and display at least two objects of different types.
You do not need to connect SolidWorks yet. Focus on the class structure.