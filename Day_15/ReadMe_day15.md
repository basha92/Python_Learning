Here are the answers, using your CAD project for examples. I'll keep the Lego picture going.

## 1. What is the Single Responsibility Principle (SRP)?

**A class should have only one reason to change.** It does one job.

In your project, `Patient` only holds patient data. `PatientValidator` only checks it. `Report` only builds text. `FileManager` only writes files. If the report format changes, you touch `Report` and nothing else.

A violation would be a `Patient` class that also validates itself, formats the report and saves to a file. Four jobs, so four reasons to change.

## 2. SRP vs Separation of Concerns (SoC)

They're cousins, not twins.

| | Separation of Concerns | Single Responsibility Principle |
|---|---|---|
| **Scale** | Big picture: how you split the whole program into areas | Small picture: what one class or function does |
| **Question it asks** | "Are validation, formatting and storage kept in different places?" | "Does this class have only one reason to change?" |
| **Your project** | Separate files: `validation.py`, `report.py`, `file_manager.py` | Inside `report.py`, `Report` only formats and never writes files |

Lego version: SoC is sorting your Lego into boxes (wheels, arms, heads). SRP is making sure each brick has one job. You usually do SoC first, then check SRP inside each box.

## 3. DRY with an example from your CAD project

**DRY = Don't Repeat Yourself.** Every piece of knowledge should live in one place.

Your original `cad_part.py` had this in all three subclasses:

```python
def __init__(self, part_number, material, file_path):
    super().__init__(part_number, material, file_path)

def part(self):
    print("\nTibial Part Details")
    super().part()
```

The same `__init__` and the same print pattern were copied three times. If you wanted to change the layout, you'd edit it in three places and might forget one.

The DRY fix was a `label` attribute:

```python
class CadPart:
    label = "CAD Part Details"
    def describe(self): ...

class TibialPart(CadPart):
    label = "Tibial Part Details"
```

Now the layout lives in one place, and each subclass only says what is different.

One caution: DRY is about repeated *knowledge*, not just similar-looking code. Your three processors look alike now, but if they will behave differently later, leave them separate until the real pattern shows up.

## 4. What is the Open/Closed Principle (OCP)?

**Code should be open for extension but closed for modification.** You add new behavior by adding new code, not by editing working code.

Example: you want a new `PatellaPart`. You add `PatellaPart` and `PatellaProcessor`, then register them with one line in `main.py`. `CadService`, `Report` and `PatientService` don't change.

The opposite (a violation) is an `if/elif` chain inside the service:

```python
if part_type == "tibial": ...
elif part_type == "femoral": ...
elif part_type == "insert": ...   # editing old code every time
```

Every new part means opening and risking working code.

## 5. What is Dependency Injection (DI)?

**A class receives the helpers it needs from outside instead of creating them itself.**

Without DI (glued-on hand):
```python
class PatientService:
    def __init__(self):
        self.writer = FileWriter("report.txt")   # builds its own helper
```

With DI (a socket):
```python
class PatientService:
    def __init__(self, validator, writer):
        self.validator = validator
        self.writer = writer                      # handed in from outside
```

Now `main.py` decides what to plug in: `FileWriter`, `ConsoleWriter`, or a fake writer for tests. `PatientService` never changes.

Related term: **Dependency Inversion (the D in SOLID)** is the principle ("depend on abstractions, not concrete classes"). **Dependency Injection** is the technique you use to achieve it.

## 6. Why should `main.py` coordinate instead of containing the logic?

Think of `main.py` as the **person who snaps the Lego together**, not the Lego bricks themselves.

1. **Testability.** Logic in classes can be tested alone with fake helpers. Logic in `main.py` can only be tested by running the whole program.
2. **Reusability.** A `PatientService` can later be used by a web app or a GUI. Code stuck in `main.py` can't be.
3. **Changeability.** Switching from a text file to JSON should mean editing one line in `main.py`, not hunting through 100 lines of mixed logic.
4. **Readability.** `main.py` should read like a table of contents: build the pieces, plug them together, run. Your current `main.py` has seven numbered steps of real work, and that's the clue that logic has leaked into it.
5. **SRP applies to files too.** If `main.py` validates, formats and writes, it has many reasons to change.

A good `main.py` is short:

```python
def main():
    service = PatientService(PatientValidator(), CadService(...), FileManager())
    service.run(records, parts)
```

## Quick self-check

Try answering these without looking:
- Which of your current classes has more than one reason to change?
- What would you edit to add a `PatellaPart`? If the answer is more than "add classes and one line in main," something is closed that should be open.

Want me to turn your current `main.py` (steps 2 to 7) into a `CaseService` so you can see the before and after? Typing it out yourself is the best way to make these six answers stick.