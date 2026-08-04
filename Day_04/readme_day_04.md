# Day 04 - Patient Registration System (Python)

## Overview

Today's focus was on writing maintainable and modular Python code by building a simple Patient Registration System.

The project collects patient information, validates user input, calculates Body Mass Index (BMI), and displays a formatted patient summary.

The primary objective was not just to make the program work, but to design it using good software engineering practices such as modular programming, reusable functions, and separation of responsibilities.

---

## Topics Learned

- if / elif / else
- while loops
- Exception handling (try / except)
- Raising custom exceptions
- Input validation
- Modular programming
- Explicit module imports
- Function design
- Reusable utility functions
- Tuple unpacking
- First-class functions
- Separation of Concerns (SoC)
- DRY (Don't Repeat Yourself) principle

---

## Project Structure

```
Day_04/
│
├── main.py
├── patient.py
├── validation.py
├── report.py
└── README.md
```

### Responsibilities

| File | Responsibility |
|------|----------------|
| main.py | Coordinates the application workflow |
| patient.py | Collects patient information |
| validation.py | Performs reusable input validation |
| report.py | Displays patient summary |

---

## Features

- Collect patient details
- Validate all user inputs
- Prevent invalid data entry
- Calculate BMI
- Display formatted patient report
- Reusable validation function for different input types

---

## Key Learning

The biggest improvement today was understanding how to write reusable code.

Instead of writing separate validation loops for every input, I created a generic `get_valid_input()` function that accepts:

- Prompt
- Data type
- Validation function

This reduced duplicate code and made the application easier to maintain.

Example:

```python
age = get_valid_input(
    "Enter Age: ",
    int,
    validate_age
)
```

---

## Challenges Faced

- Understanding module responsibilities
- Connecting multiple Python files
- Difference between function references and function calls
- Tuple unpacking
- Designing reusable validation logic
- Understanding how functions can be passed as arguments

---

## Lessons Learned

Today I learned that:

- Functions are first-class objects in Python.
- A function name (`validate_age`) is different from calling the function (`validate_age()`).
- Multiple values returned from a function are automatically packed into a tuple.
- Python can unpack tuples directly into multiple variables.
- Good software design is as important as writing correct code.

---

## Future Improvements

- Add continuous patient registration
- Store multiple patient records
- Export reports to CSV
- Save patient data to JSON
- Add logging
- Add unit tests
- Convert patient information into a Python class

---

## Git Commits

- Created modular patient registration system
- Implemented reusable validation framework
- Added BMI calculation
- Refactored project architecture
- Improved exception handling

---

## Reflection

This project helped me move beyond writing Python syntax and start thinking about software architecture.

I learned how to separate responsibilities across modules, design reusable functions, and understand how Python treats functions as first-class objects.

These concepts form the foundation for building larger automation applications, which directly align with my goal of transitioning into a Patient Specific Design Automation Engineer role.

## Engineering Takeaway

Today's project reinforced an important software engineering principle:

> "Code should be designed for reuse, not just to solve the current problem."

By creating a generic validation function instead of four separate validation loops, I reduced duplicate code and made the application easier to extend. This approach is commonly used in automation frameworks and production software.

## Skills Demonstrated

- Python Programming
- Modular Design
- Input Validation
- Exception Handling
- Software Architecture
- Debugging
- Code Reusability
- Git Version Control