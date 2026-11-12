Day 10: Object-Oriented Programming (OOP) in Python
Overview
Day 10 focused on the core ideas of Object-Oriented Programming (OOP)
and how to use them to organize patient-related data and operations in
Python.

The exercises used a patient-management example to practise creating
classes and objects, working with instance data, and using different
types of methods.
Topics Covered
1. Classes and Objects
- Created a patient class to define the structure and behaviour of a
  patient record.
- Created multiple patient objects from the same class.
- Used __init__() to set up each object's initial data.
- Used self to access and store data belonging to an object.
2. Instance Attributes and Methods
- Stored patient details such as name, age, height, and weight as
  instance attributes.
- Calculated and stored BMI for each patient.
- Used an instance method to return the patient's BMI category.
- Used an instance method to display a patient report.
- Explored how changing an object's attribute affects that object.
3. Instance, Class, and Static Methods
- Instance methods: Use self to work with data belonging to a
  specific object.
- Class methods: Use @classmethod and cls to work with
  class-level data or create objects through alternative constructors.
- Static methods: Use @staticmethod for utility logic that does
  not need instance or class data.
4. Alternative Constructor
- Practised using a class method such as from_dictionary() to create
  a patient object from dictionary data.
Exercises Completed
1. Update patient weight: Created an instance method to update a
   patient's weight and recalculate BMI.
2. Track patient count: Used a class attribute and class method to
   track the number of patient objects created.
3. Validate patient age: Used a static method to check whether an
   age is within the accepted range of 1 to 120.
4. Create a patient from a dictionary: Used an alternative
   constructor to build a patient object from dictionary data.
5. OOP concept checks: Reviewed the differences between instance
   methods, class methods, and static methods.
Key Learning Points
- A class defines a structure; an object is an instance of that class.
- Each object has its own instance attributes.
- self refers to the current object.
- cls refers to the class itself.
- Instance methods work with object data.
- Class methods work with class-level data and can provide alternative
  ways to create objects.
- Static methods group related utility logic inside a class without
  using object or class state.
- If a calculated value is stored, changing its source data does not
  update that value automatically. The program must recalculate it, or
  use a property that calculates it when accessed.
Practical Context
The patient example helped connect OOP concepts to a structured data
workflow. The same ideas can be applied to larger automation projects,
where classes can represent patients, cases, CAD parts, test results, or
processing tasks.
Day 10 Outcome
Completed the Day 10 OOP exercises covering classes, objects,
constructors, instance attributes, BMI calculations, and instance,
class, and static methods.
Next Step
Continue building on OOP by learning how to organize code into
maintainable components and how to design classes that work together in
a small automation project.