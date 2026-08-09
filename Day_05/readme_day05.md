# Day 05 - Patient Management System

## Overview

Day 05 focused on Python collections and using them to build a small Patient Management System.

The project builds on the modular programming, input validation, and BMI calculation concepts learned in Day 04.

The application allows users to add, view, and search patient records while practicing lists, dictionaries, tuples, sets, loops, functions, and modular design.

---

## Topics Learned

- Lists
- Dictionaries
- Tuples
- Sets
- List of dictionaries
- Iterating through collections
- Dictionary access
- Collection methods
- Mutable vs immutable data
- Function design
- Modular programming
- Separation of Concerns
- Code reusability

---

## Project Features

The Patient Management System supports:

1. Add Patient
2. View Patients
3. Search Patient
4. Exit

Each patient record contains:

- Name
- Age
- Height
- Weight
- BMI

Patient records are stored as a list of dictionaries.

Example:

```python
patients = [
    {
        "Name": "John",
        "Age": 35,
        "Height": 1.75,
        "Weight": 72,
        "BMI": 23.51
    }
]
````

---

## Project Structure

```text
Day_05/
│
├── main.py
├── patient.py
├── validation.py
├── report.py
└── README.md
```

| Module          | Responsibility                     |
| --------------- | ---------------------------------- |
| `main.py`       | Controls application flow and menu |
| `patient.py`    | Handles patient-related operations |
| `validation.py` | Validates user input               |
| `report.py`     | Displays patient information       |

---

## Python Collections Practiced

### List

Used to store multiple patient records.

```python
patients = []
```

### Dictionary

Used to represent an individual patient's information.

```python
patient = {
    "Name": "John",
    "Age": 35,
    "Weight": 72
}
```

### Tuple

Used to understand fixed collections.

```python
BMI_CATEGORIES = (
    "Underweight",
    "Normal",
    "Overweight",
    "Obese"
)
```

### Set

Used to understand unique collections and duplicate handling.

```python
departments = {
    "Hip",
    "Knee",
    "Shoulder",
    "Hip",
    "CMF"
}
```

The duplicate `"Hip"` value is automatically removed.

---

## Key Learning

The main learning from Day 05 was understanding how different data structures solve different problems.

| Collection | Use                          |
| ---------- | ---------------------------- |
| List       | Store multiple ordered items |
| Dictionary | Store key-value data         |
| Tuple      | Store fixed/immutable data   |
| Set        | Store unique values          |

I also learned how collections can be combined to represent structured real-world data, such as a list of patient dictionaries.

---

## Challenges Faced

The main challenges during this project were:

* Looping through collections
* Deciding where validation should happen
* Connecting multiple modules
* Determining what inputs and outputs each function requires
* Deciding which functions belong in which module

These challenges helped me understand that writing working code and designing maintainable code are two different skills.

---

## Engineering Takeaway

A major lesson from this project was:

> Good automation code is not only about making the task work. It also requires choosing the right data structures and giving each function and module a clear responsibility.

The project reinforced:

* Separation of Concerns
* Reusable functions
* Modular design
* Data structure selection
* Maintainable code

---

## Connection to Automation Engineering

The concepts learned here can be applied to automation workflows that process multiple:

* Patient cases
* CAD files
* Parts
* Properties
* Validation results
* Reports

For example, a future automation workflow could represent cases using:

```python
cases = [
    {
        "case_id": "CASE001",
        "parts": ["Femur", "Tibia"],
        "status": "Validated"
    }
]
```

These concepts will later be extended to file handling, JSON/XML processing, CAD metadata, reporting, and automation workflows.

---

## Skills Demonstrated

* Python Programming
* Lists and Dictionaries
* Tuples and Sets
* Loops
* Functions
* Input Validation
* Exception Handling
* Modular Programming
* Separation of Concerns
* Code Reusability
* Problem Solving
* Git Version Control

---

## Future Improvements

* Add unique Patient ID
* Prevent duplicate records
* Update and delete patients
* Store data in JSON
* Export reports to CSV
* Add logging
* Add unit tests
* Introduce Object-Oriented Programming

---

## Learning Record

| Item            | Details                                |
| --------------- | -------------------------------------- |
| Study Hours     | 12 hours                               |
| Exercises       | All Day 05 exercises                   |
| Mini Project    | Patient Management System              |
| Status          | Completed                              |
| Main Challenges | Collections, validation, module design |
| GitHub          | `Python_Learning/Day_05`               |

```

### What goes where?

Think of it this way:

**GitHub README** → "Show me what you built."  
**Mentor Workbook** → "Show me how you learned."  
**Your code** → "Show me that you can actually do it."  
**Business Impact Log** → "Show me why the organisation should care."  

So don't stuff every detail into GitHub. Keep the README professional and readable.

And yes, I'll keep using your daily updates to help maintain the **mentor-side record** as we go through the 90 days. 
```
