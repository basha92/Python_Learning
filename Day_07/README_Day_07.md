# Day 07 - JSON & File Automation

## Overview

Day 07 focused on using JSON with `pathlib` and Python modules to build
a small automation workflow. The main goal was to move from working with
individual functions to connecting multiple modules and processing
multiple patient JSON files.

## Study Time

**Total study time: 8 hours**

## Topics Completed

-   JSON basics
-   `json.load()` and `json.dump()`
-   JSON objects and Python dictionaries
-   JSON arrays and Python lists
-   Accessing nested JSON data
-   Updating JSON data
-   Writing processed JSON to files
-   Combining `pathlib` with JSON processing
-   Iterating through multiple JSON files
-   Connecting multiple Python modules
-   Understanding function arguments and return values
-   Debugging data-type and argument-order errors

## Mini Project

### Patient JSON Processor

The project was designed around this workflow:

``` text
data/
   ↓
find JSON files
   ↓
read one JSON file
   ↓
process patient data
   ↓
calculate BMI
   ↓
add BMI to patient data
   ↓
write processed JSON
```

The project uses separate modules for different responsibilities:

-   `file_handler.py` - finds, reads, and writes files
-   `patient_processor.py` - processes patient data and calculates BMI
-   `validation.py` - intended for data validation
-   `main.py` - coordinates the workflow

## Key Learning

One of the most important lessons was understanding the difference
between a **list of files** and **one file**.

`find_json_files()` returns a list:

``` python
files = find_json_files("data")
```

The program then processes one file at a time:

``` python
for file in files:
    patient = read_json(file)
```

This helped clarify the general automation pattern:

``` text
Get a collection
    ↓
Loop through the collection
    ↓
Process one item
    ↓
Move to the next item
```

## Debugging Lessons

### 1. List vs Dictionary

An error occurred when the patient JSON was created as a list containing
a dictionary:

``` text
TypeError: list indices must be integers or slices, not str
```

The issue was that code such as:

``` python
patient["weight"]
```

expects `patient` to be a dictionary, while the loaded JSON was a list.

This reinforced the importance of checking the actual data type before
accessing it.

### 2. Function Argument Order

The height and weight arguments were initially passed in the wrong
order.

The intended interface is:

``` python
calculate_bmi(height, weight)
```

with the formula:

``` text
BMI = weight / height²
```

### 3. `write_json()` Argument Order

The file path and data arguments were initially passed in the wrong
order.

The function interface should make the expected inputs clear, for
example:

``` python
write_json(file_path, data)
```

The function call must follow the same order.

## What I Understood Well

-   Basic JSON structure
-   Reading JSON into Python
-   Writing Python data back to JSON
-   Basic `pathlib` usage
-   Finding files with a loop
-   Passing data between functions
-   The difference between a list and a dictionary
-   The purpose of separating file handling from data processing

## What I Need to Improve

-   Connecting multiple modules confidently
-   Understanding how data moves between functions
-   Designing clean function interfaces
-   Processing nested collections
-   Error handling for invalid JSON and invalid patient data
-   Avoiding dependence on Copilot when designing the first version of a
    solution

## Mentor Feedback

The most valuable part of Day 07 was not simply getting the program to
run. The debugging process exposed how data moves between modules.

The project now follows a useful separation of responsibility:

``` text
main.py
  ↓
file_handler.py
  ↓
patient_processor.py
  ↓
file_handler.py
```

This is a foundation for larger automation projects.

The next focus should be to make the Day 07 project more robust by
adding validation, exception handling, and automated tests rather than
adding unnecessary features.

## Portfolio Evidence

**GitHub Repository:**

https://github.com/basha92/Python_Learning/tree/main/Day_07

Suggested portfolio points:

-   Built a Python utility to process patient JSON files in batch.
-   Used `pathlib` for file discovery and JSON for structured data
    processing.
-   Separated file handling and patient-processing responsibilities into
    reusable modules.
-   Implemented BMI calculation and wrote processed results to JSON.
-   Debugged and resolved list/dictionary type errors and function
    argument-order issues.

## Interview Preparation

Questions to be able to answer:

1.  What is JSON?
2.  What does `json.load()` do?
3.  What does `json.dump()` do?
4.  What is the difference between a JSON object and JSON array?
5.  How does a JSON object map to a Python dictionary?
6.  How would you process 1,000 JSON files?
7.  Why should file handling and business logic be separated?
8.  How would you handle invalid JSON?
9.  How would you handle a missing patient field?
10. What happens when a list is accessed using a string key?

## Day 07 Status

-   **Study Hours:** 8
-   **Exercises:** Completed
-   **Mini Project:** Completed
-   **GitHub:** Day 07 repository
-   **Main Challenge:** Connecting modules and understanding the data
    type passed between functions
-   **Overall Focus:** JSON + pathlib + modular automation
