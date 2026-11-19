**1. What is polymorphism?**

Polymorphism means "many forms." It lets different classes provide their own version of the same method, so you can call that method on any of them without caring which specific type you have. In your code, `calculate_volume()` is one method name with two different behaviors, one in `TibialPart` and one in `FemoralPart`.

**2. How does Python decide which overridden method to execute?**

Python looks at the actual type of the object at runtime, not at the variable name or the base class. It follows the method resolution order (MRO): first the object's own class, then its parent, then the parent's parent, and so on, and it runs the first matching method it finds.

```python
part = TibialPart()
part.calculate_volume()   # finds TibialPart.calculate_volume first, so returns 210
```

If `TibialPart` did not define `calculate_volume`, Python would move up to `CADPart` and use that version. You can inspect the order with `TibialPart.__mro__`.

**3. Why is polymorphism useful when processing a list of different CAD parts?**

You can write one loop that works for every part type, with no `if/elif` chain checking what kind of part each one is:

```python
for part in parts:
    print(part.calculate_volume())
```

Without polymorphism you would need something like `if isinstance(part, TibialPart): ... elif isinstance(part, FemoralPart): ...`. With it, adding a new `PatellarPart` class requires no change to the loop. You just define the new class with its own `calculate_volume()`. This makes code shorter, easier to extend, and less error-prone.

**4. What is duck typing?**

Duck typing is Python's approach of judging an object by what it can do rather than what it is. The saying goes: "If it walks like a duck and quacks like a duck, it's a duck." If an object has a `calculate_volume()` method, Python will let you call it, regardless of its class or inheritance.

```python
class Screw:
    def calculate_volume(self):
        return 5

parts = [TibialPart(), FemoralPart(), Screw()]   # Screw doesn't inherit from CADPart
for part in parts:
    print(part.calculate_volume())               # still works
```

**5. What is the main difference between inheritance and polymorphism?**

Inheritance is a way of **sharing and reusing code**: a child class gets the attributes and methods of a parent class (an "is-a" relationship). Polymorphism is a way of **using different objects through the same interface**: the same method call behaves differently depending on the object.

They often work together, since inheritance gives you a common parent with a shared method name, and polymorphism is what happens when the children override it. But they are separate ideas. Inheritance is about how classes are structured, while polymorphism is about how objects behave when you call methods on them. Duck typing shows they are independent, because you can have polymorphism with no inheritance at all.