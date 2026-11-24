# Day 16: Introduction to pytest and Parameterized Testing

## Learning goals

Learn to test Python code with `pytest`, check expected results, test
validation errors, and reduce repeated test code with parameterization.
The exercises used the Patient Case Framework.

## Project structure

``` text
Patient_Case_Framework/
├── patients.py
├── validation.py
├── main.py
└── tests/
    ├── test_validation.py
    └── test_validation_1.py
```

Test files should start with `test_` so pytest can discover them.

## 1. Basic tests and assertions

A test creates the data it needs, calls the code being tested, and
checks the result.

``` python
from patients import Patient
from validation import PatientValidator


def test_valid_patient():
    patient = Patient(1001, "Aaron", 38, "Knee Replacement")
    assert PatientValidator.validate(patient) is True
```

`assert` checks whether an expression matches the expected result. If it
does not, the test fails.

## 2. Testing exceptions

For invalid input, the validator should raise an exception.

``` python
import pytest


def test_invalid_patient():
    patient = Patient(1002, "", 38, "Knee Replacement")

    with pytest.raises(ValueError):
        PatientValidator.validate(patient)
```

`pytest.raises(ValueError)` is a context manager. It checks that the
code inside the `with` block raises a `ValueError`. If the exception is
not raised, the test fails.

## 3. Parameterized tests

`@pytest.mark.parametrize` runs one test function with several sets of
input values.

``` python
@pytest.mark.parametrize("age", [23, 45, 1, 120])
def test_valid_age(age):
    patient = Patient(1002, "Kevin", age, "Hip Implant")
    assert PatientValidator.validate(patient) is True
```

This test runs four times, once for each age.

Invalid ages can be checked in the same way:

``` python
@pytest.mark.parametrize("age", [0, -1, 121, 150])
def test_invalid_age(age):
    patient = Patient(1006, "KK", age, "Knee Replacement")

    with pytest.raises(ValueError):
        PatientValidator.validate(patient)
```

You can parameterize multiple fields too:

``` python
@pytest.mark.parametrize(
    "patient_id, name, age, surgery",
    [
        (1001, "Aaron", 38, "Knee Replacement"),
        (1002, "Kevin", 23, "Hip Implant"),
        (1003, "Sam", 45, "Hip Replacement"),
    ],
)
def test_valid_patients(patient_id, name, age, surgery):
    patient = Patient(patient_id, name, age, surgery)
    assert PatientValidator.validate(patient) is True
```

## 4. Test cases written

  -----------------------------------------------------------------------
  Test area               Inputs or cases         Expected result
  ----------------------- ----------------------- -----------------------
  Valid ages              23, 45, 1, 120          Validation returns
                                                  `True`

  Invalid ages            0, -1, 121, 150         Raises `ValueError`

  Invalid patient IDs     `"1001"`, `10.5`, `""`  Raises `ValueError`

  Invalid names           `""`, `"     "`         Raises `ValueError`

  Multiple valid patients Three patient records   Validation returns
                                                  `True`
  -----------------------------------------------------------------------

The focused valid-age test was commented out after adding a broader test
for multiple valid patients. The broader test also checked valid ages,
but a separate focused test can make failures easier to identify.

An invalid surgery type test was identified as a useful addition, but it
was not part of the final test code shared for review.

## 5. Mistakes, debugging and lessons

### Mistake 1: Running pytest from the wrong folder

**Error:**

``` text
ModuleNotFoundError: No module named 'patients'
```

The first test run was started from the higher-level `Python_Learning`
folder, not from the `Patient_Case_Framework` project root. This meant
Python could not find `patients.py` through the import path used by that
run.

**Fix:** Change to the project root:

``` powershell
cd F:\Python_Git\Python_Learning\Day_16\Patient_Case_Framework
```

### Mistake 2: Launching pytest directly

This command failed to import `patients` when running
`test_validation_1.py`:

``` powershell
pytest tests/test_validation_1.py -v -p no:cacheprovider
```

This command worked:

``` powershell
python -m pytest tests/test_validation_1.py -v -p no:cacheprovider
```

The successful command ran pytest through the Python interpreter in the
active virtual environment:

``` text
F:\Python_Git\Python_Learning\myvenv\Scripts\python.exe
```

**Lesson:** Use `python -m pytest` consistently so pytest runs through
the active Python interpreter.

### Mistake 3: Expecting an exception for a valid age

A test used age `23` inside `pytest.raises(ValueError)`. But 23 is valid
under the current validation rule, so the validator should not raise an
exception.

**Fix for valid input:**

``` python
assert PatientValidator.validate(patient) is True
```

**Fix for invalid input, such as age 150:**

``` python
with pytest.raises(ValueError):
    PatientValidator.validate(patient)
```

**Lesson:** Match the expected test result to the input. Valid input
should pass; invalid input should raise the expected exception.

### Mistake 4: Understanding parameterized test counts

If eight values are passed to `pytest.mark.parametrize`, pytest runs the
test function eight times, once for each value.

### Note: Cache warnings on the F: drive

Cache-related warnings appeared during test runs. This option was used
to disable pytest's cache provider:

``` powershell
-p no:cacheprovider
```

It was useful in this environment, but it is not required for every
project.

## 6. Full test command

Run this from the project root:

``` powershell
python -m pytest tests -v -p no:cacheprovider
```

-   `tests` runs tests from the tests folder.
-   `-v` shows each test name and result.
-   `-p no:cacheprovider` disables pytest's cache provider.

## 7. Knowledge check

**1. If eight values are passed to `pytest.mark.parametrize`, how many
times does pytest run the test function?**

Answer: Eight times, once for each value.

**2. What is the purpose of `with pytest.raises(ValueError)`?**

Answer: It checks that the code inside the context manager raises a
`ValueError`.

**3. If age 150 is invalid, should the test use `assert result is True`
or `pytest.raises(ValueError)`?**

Answer: Use `pytest.raises(ValueError)` because the validator should
reject the invalid age by raising that exception. The input is invalid,
not simply a false value.

## Day 16 result

**Status: Completed.** The full test suite passed.

Skills practised:

-   Installing and running pytest in a virtual environment.
-   Creating test files and understanding test discovery.
-   Using `assert` to check results.
-   Using `pytest.raises()` to test exceptions.
-   Using `pytest.mark.parametrize` for multiple inputs.
-   Testing valid and invalid patient data.
-   Debugging an import issue caused by how pytest was launched.

## Key takeaways

-   Test both successful and failure paths.
-   Match the expected result to the input.
-   Parameterization makes it easy to test many inputs with one
    function.
-   Run tests from the project root.
-   Use `python -m pytest` to run pytest through the active interpreter.
-   Keep test setup and test logic clear.

## Next step

**Day 17: pytest fixtures.** Learn to reuse test data and reduce
repeated setup code.
