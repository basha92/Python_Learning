**1. What is abstraction?**

Abstraction means hiding the implementation details and exposing only what matters. You define *what* an object must be able to do, without saying *how* each type does it. In your CAD example, the caller only needs to know that every part can `calculate_volume()`. How a tibial or femoral part computes that is hidden inside each class.

**2. Why do we use `ABC`?**

`ABC` (from the `abc` module) marks a class as an abstract base class. Its job is to act as a blueprint: it cannot be instantiated directly, and it forces a contract on its subclasses.

```python
from abc import ABC, abstractmethod

class CADPart(ABC):
    @abstractmethod
    def calculate_volume(self):
        pass

part = CADPart()   # TypeError: Can't instantiate abstract class CADPart
```

Without `ABC`, nothing stops someone from creating a meaningless `CADPart()` object, or from writing a subclass and forgetting a required method.

**3. What does `@abstractmethod` do?**

It marks a method as required: every concrete subclass must override it. The method in the base class usually has no real body (`pass` or a docstring), because it only declares the contract. Python checks this when you try to create an object, not when you define the class.

```python
class TibialPart(CADPart):
    def calculate_volume(self):
        return 210

print(TibialPart().calculate_volume())   # 210
```

**4. Can an abstract class have a constructor and normal methods?**

Yes. An abstract class can have `__init__`, regular methods, class attributes, and even abstract methods with a body. Only the methods marked `@abstractmethod` are forced on subclasses. This lets you share common code while still enforcing the contract.

```python
class CADPart(ABC):
    def __init__(self, name):
        self.name = name

    def describe(self):                       # normal method, inherited as-is
        return f"{self.name}: {self.calculate_volume()} mm³"

    @abstractmethod
    def calculate_volume(self):               # must be overridden
        pass

class TibialPart(CADPart):
    def calculate_volume(self):
        return 210

print(TibialPart("Tibial").describe())        # Tibial: 210 mm³
```

This also fixes the earlier error in your first question: subclasses call the inherited constructor with the arguments it needs.

**5. What happens if a child class does not implement all abstract methods?**

The child is itself treated as abstract, so you cannot instantiate it. Python raises a `TypeError` at the moment you try to create an object.

```python
class FemoralPart(CADPart):
    pass                                      # forgot calculate_volume

FemoralPart("Femoral")
# TypeError: Can't instantiate abstract class FemoralPart
# without an implementation for abstract method 'calculate_volume'
```

This is the main benefit: the mistake is caught immediately and clearly, rather than surfacing later as a confusing bug or a silent `None` return from a `pass` method (like in your original `CADPart`).

**6. What is the difference between duck typing and abstract classes?**

Both support polymorphism, but they differ in how strictly the contract is enforced.

- **Duck typing** is informal and checked at the moment of use. Any object with a `calculate_volume()` method works, and if one is missing you only find out when the call fails with an `AttributeError`.
- **Abstract classes** are formal and checked at object creation. Subclasses must explicitly inherit from the base and implement every abstract method, or Python refuses to build them.

| | Duck typing | Abstract classes |
|---|---|---|
| Contract | Implicit, by convention | Explicit, declared in code |
| Needs inheritance | No | Yes |
| When errors appear | When the method is called | When the object is created |
| Flexibility | Very high | More structured |

Duck typing suits small scripts and loosely related objects. Abstract classes suit larger systems, like a CAD library with many part types, where you want guarantees that every part follows the same rules.