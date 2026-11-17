# Day 11: Patient Data Validation System

A small Python project that creates patient objects, validates their details, calculates BMI on the fly, and shows a BMI category. Built to practise **classes, properties, validation, and connecting multiple files**.

## What it does

1. Creates patient objects
2. Validates name, age, height and weight
3. Rejects invalid age, height and weight with a `ValueError`
4. Calculates BMI dynamically (never stored, always computed from the current weight and height)
5. Displays patient details and BMI category
6. Updates a patient's weight and shows the new BMI

## Project structure

```
Day_11/
├── main.py       # the kitchen: creates patients, prints, handles errors
├── patient.py    # the tool room: defines what a Patient is
└── README.md     # this file
```

## How to run

Keep both files in the same folder, then run **only main**:

```
python main.py
```

Never run `patient.py` to test the project. It only describes the class and prints nothing.

## The story: how main and patient.py connect

Imagine a bakery with two rooms.

**The tool room (`patient.py`)** is where the cookie cutter is made. The cutter is the `Patient` class. It has a shape (name, age, weight, height) and rules ("no negative weight, no age above 120"). But a cutter is not a cookie. You cannot eat it, and you cannot ask it how old it is.

**The kitchen (`main.py`)** is where the cooking happens. The kitchen cannot use a tool that is still in the other room, so the first thing it does is carry the cutter in:

```python
from patient import Patient
```

Read it as: *"From the room called `patient`, bring me the tool called `Patient`."*

Now the kitchen presses the cutter into dough. That is the moment a real cookie (an object) exists:

```python
p1 = Patient("Arun", 31, 70, 175)
```

The cookie goes on a plate (`p1`). When a helper function needs a cookie, we hand it over:

```python
display_details(p1)
```

Inside the helper, the slot that receives the cookie is just a name:

```python
def display_details(patient):   # lowercase "patient" is an empty plate
    print(patient.name)         # works because a real cookie was placed on it
```

> **Import the class, create the object, use the object.**

### The golden rule

| Written as | What it is | Where you use it |
|---|---|---|
| `Patient` (capital P) | The blueprint (cookie cutter) | Only to create objects: `Patient(...)` |
| `patient`, `p1`, `x` | A real object, or a slot for one | Everywhere else, with a dot: `p1.bmi` |

## Mistakes I made (and what they taught me)

| # | Mistake | What went wrong | Fix |
|---|---|---|---|
| 1 | Wrote `lass Patient` | Typo, so the class never existed | `class Patient` |
| 2 | Used `Patient.age`, `Patient.bmi` in `main.py` | Asked the **cutter** instead of a **cookie** | Create an object first, then use `p1.age` |
| 3 | Wrote `p1 = ("Arun", 31, 70, 175)` | Made a **tuple**, not a Patient. Error: `'tuple' object has no attribute 'name'` | `p1 = Patient("Arun", 31, 70, 175)` |
| 4 | `self.__age = age` in `__init__` | Skipped the age validation entirely | Use `self.age = age` so the setter runs |
| 5 | Age setter only used `print` | Printed a message but did not actually reject | `raise ValueError(...)` like height and weight |
| 6 | `1 < new_age <= 120` | Rejected a valid age of 1 | `1 <= new_age <= 120` |
| 7 | `try/except` around a tuple | A tuple can never raise `ValueError`, so the protection did nothing | The `try` only works once `Patient(...)` is called |
| 8 | Printed `Name:` for the BMI category | Copy-paste slip | `BMI Category:` |
| 9 | Property named `get_bmi_category` | Misleading name for a property | Renamed to `bmi_category` |

### Quick debugging trick

When you see `'tuple' object has no attribute ...` or `'list' object has no attribute ...`, ask:

> *Did I actually write `Patient(` or just brackets?*

Brackets alone make a tuple. The class name in front makes an object.

## BMI categories

| BMI | Category |
|---|---|
| below 18.5 | Underweight |
| 18.5 to 24.9 | Normal weight |
| 25 to 29.9 | Overweight |
| 30 and above | Obesity |

Formula: `BMI = weight (kg) / height (m)²`. Height is stored in cm, so it is divided by 100 first.

## Sample output

```
--- Patient Record ---
Name: Arun
Age: 31
Weight: 70 kg
Height: 175 cm
BMI: 22.86
BMI Category: Normal weight

After weight update:

--- Patient Record ---
Name: Arun
Age: 31
Weight: 85 kg
Height: 175 cm
BMI: 27.76
BMI Category: Overweight
Skipped patient Ravi: Age must be a whole number between 1 and 120.
Skipped patient Sam: Weight must be a positive number (kg).
Skipped patient : Name cannot be empty.
```

## Key concepts practised

- **Classes and objects**: blueprint vs real instance
- **Imports**: `from patient import Patient`
- **Encapsulation**: private-style attributes with `@property` getters and setters
- **Validation**: raising `ValueError` to reject bad data
- **Read-only properties**: `bmi` and `bmi_category` are computed, never set
- **Exception handling**: `try/except` lets the program skip bad records and keep running
- **Tuple unpacking**: `Patient(*rec)` spreads a tuple into the four arguments

## Checklist before running

- [ ] `patient.py` and `main.py` are in the same folder
- [ ] The class is spelled `class Patient`
- [ ] `__init__` uses `self.age = age` (no double underscore)
- [ ] `main.py` creates patients with `Patient(...)`, not plain brackets
- [ ] I run `python main.py`, not `patient.py`