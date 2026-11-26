# Day 17: pytest Fixtures

## Learning goals

Day 17 focused on using pytest fixtures to prepare reusable test data, reduce repeated setup code, and make test functions easier to read. The examples use the Patient Case Framework.

## 1. What is a pytest fixture?

A fixture is a function that prepares and provides something a test needs.

```python
import pytest
from patients import Patient


@pytest.fixture
def valid_patient():
    return Patient(1001, "Aaron", 38, "Knee Replacement")
```

A test requests the fixture by adding its name as an argument:

```python
def test_patient_name(valid_patient):
    assert valid_patient.name == "Aaron"
```

Pytest finds the fixture and passes its returned object to the test. The test does not call `valid_patient()` directly.

## 2. Reusing a fixture across tests

The same fixture can be requested by several test functions:

```python
def test_patient_name(valid_patient):
    assert valid_patient.name == "Aaron"


def test_patient_age(valid_patient):
    assert valid_patient.age == 38
```

This keeps setup code in one place and lets each test focus on one behaviour. By default, pytest uses `function` scope, so it creates a fresh fixture result for each test function that requests it.

## 3. Using `conftest.py`

When multiple test files need the same fixture, place it in a file named `conftest.py`.

```text
Patient_Case_Framework/
├── patients.py
├── validation.py
├── main.py
└── tests/
    ├── conftest.py
    ├── test_validation.py
    ├── test_invalid.py
    └── test_patient.py
```

Example `tests/conftest.py`:

```python
import pytest
from patients import Patient


@pytest.fixture
def valid_patient():
    return Patient(1001, "Aaron", 38, "Knee Replacement")
```

Pytest discovers fixtures in `conftest.py` for test files in that directory and its subfolders. Test files can request the fixture by name without importing it.

## 4. Passing multiple invalid values to a test

I got stuck on how to pass multiple invalid values to a test function. I looked it up online and found that I could use `pytest.mark.parametrize` to pass a list of values to the test function.

```python
import pytest


@pytest.mark.parametrize("age", [0, -1, 121, 150])
def test_invalid_age(age):
    patient = Patient(1006, "KK", age, "Knee Replacement")

    with pytest.raises(ValueError):
        PatientValidator.validate(patient)
```

The `"age"` name in the decorator matches the `age` argument in `test_invalid_age(age)`. Pytest runs the test once for each value and passes that value into the function. This avoids writing a separate test function for every invalid age.

## 5. Avoid duplicate or confusing function names

Another learning was to avoid using the same function name for a fixture in `conftest.py` and a test function in a test file. Keep their names distinct so their roles are clear.

For example:

```python
# conftest.py
@pytest.fixture
def invalid_patient():
    return Patient(1002, "", 38, "Knee Replacement")
```

```python
# test_invalid.py
def test_rejects_invalid_patient(invalid_patient):
    with pytest.raises(ValueError):
        PatientValidator.validate(invalid_patient)
```

Here, `invalid_patient` is the fixture name and `test_rejects_invalid_patient` is the test function name. The test requests the fixture through its argument. Distinct names avoid duplicate naming and make the code easier to understand.

## 6. Fixture scope

Pytest supports several fixture scopes:

| Scope | When the fixture is created |
|---|---|
| `function` | Once for each test function that requests it |
| `class` | Once for each test class that requests it |
| `module` | Once for each test module that requests it |
| `session` | Once for the whole test session |

The default is `function`. For patient validation tests, this is a useful starting point because each test receives a fresh fixture result.

```python
@pytest.fixture(scope="function")
def valid_patient():
    return Patient(1001, "Aaron", 38, "Knee Replacement")
```

## 7. Running the tests

Run the tests from the `Patient_Case_Framework` project root:

```powershell
python -m pytest tests -v -p no:cacheprovider
```

- `python -m pytest` runs pytest through the active Python interpreter.
- `tests` tells pytest where to find the tests.
- `-v` displays each test name and result.
- `-p no:cacheprovider` disables pytest's cache provider. This option was useful in the current development environment.

## 8. Key learnings

- A fixture prepares data or resources needed by a test.
- A test requests a fixture by adding its name as a function argument.
- Pytest provides the fixture result to the test.
- `conftest.py` makes shared fixtures available to test files in its directory tree.
- `pytest.mark.parametrize` passes multiple values to a test function and runs it once for each value.
- Keep fixture names and test function names distinct so their roles are clear.
- The default fixture scope is `function`, which gives each test a fresh fixture result.

## Day 17 progress

Topics covered in this README:
- Creating and using pytest fixtures.
- Reusing test data across test functions.
- Using `conftest.py` for shared fixtures.
- Passing multiple invalid values with parameterization.
- Avoiding duplicate or confusing function names.
- Understanding fixture scope.


**1. Fixture vs. a normal function**

A normal function runs only when you call it explicitly inside your test. A fixture is declared with `@pytest.fixture`, and pytest calls it for you when a test lists the fixture's name as a parameter.

The differences that matter:

- **Dependency injection:** pytest matches parameter names to fixture names and passes the return value in. You never call `my_fixture()` yourself (pytest actually raises an error if you try).
- **Lifecycle management:** a fixture can use `yield` to split setup from teardown. Code after the `yield` runs after the test finishes, even if the test fails. A plain function has no such hook.
- **Scope and caching:** pytest controls how often the fixture runs (per test, per module, per session) and can reuse the result. A normal function runs every time you call it.
- **Composition:** fixtures can request other fixtures, and pytest builds the dependency graph and orders setup correctly.
- **Reporting and tooling:** fixtures show up in `pytest --fixtures`, and setup/teardown errors are reported separately from test failures.

```python
import pytest

@pytest.fixture
def db():
    conn = connect()
    yield conn        # test runs here
    conn.close()      # teardown, always runs

def test_query(db):   # pytest injects the connection
    assert db.query("SELECT 1")
```

**2. Three tests, default scope**

The default scope is `function`, so the fixture runs **three times**, once per test that uses it. Each test gets a fresh instance, which keeps tests isolated from each other. If you wanted it to run once for all three, you'd set a wider scope, e.g. `@pytest.fixture(scope="module")` (or `"class"`, `"package"`, `"session"`).

**3. Why `conftest.py`**

- **No duplication:** define the fixture once instead of copy-pasting it into every test file, so a fix or change happens in one place.
- **Automatic discovery:** pytest loads `conftest.py` on its own, so test files can use the fixtures without importing them. (Importing fixtures from a regular module is fragile and can cause confusing behavior.)
- **Directory-based sharing:** fixtures in a `conftest.py` are available to all tests in that directory and its subdirectories. You can have multiple `conftest.py` files, and a fixture in a deeper one overrides a same-named fixture from a higher level. That lets you share broadly but customize locally.
- **Shared setup for hooks and plugins too:** `conftest.py` is also where you put custom pytest hooks and configuration that apply across your test suite.

A good rule of thumb: if only one file uses a fixture, keep it in that file; once two or more files need it, move it to `conftest.py`.

## Next step

Continue practising fixtures in the Patient Case Framework. Use shared fixtures for common patient data and parameterization for groups of valid or invalid input values.
