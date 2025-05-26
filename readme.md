# GIAIC Q3 – Assignment 6: Python OOP Concepts

This repository contains solutions to **Assignment 6** of Quarter 3 in the GIAIC (Governor Initiative for AI and Computing) program. The focus of this assignment is to explore core **Object-Oriented Programming (OOP)** concepts in **Python** through practical examples.

## Table of Contents

1. [Using `self`](#1-using-self)
2. [Using `cls`](#2-using-cls)
3. [Public Variables and Methods](#3-public-variables-and-methods)
4. [Class Variables and Class Methods](#4-class-variables-and-class-methods)
5. [Static Variables and Static Methods](#5-static-variables-and-static-methods)
6. [Constructors and Destructors](#6-constructors-and-destructors)
7. [Access Modifiers](#7-access-modifiers-public-private-and-protected)
8. [The `super()` Function](#8-the-super-function)
9. [Abstract Classes and Methods](#9-abstract-classes-and-methods)
10. [Instance Methods](#10-instance-methods)
11. [Class Methods](#11-class-methods)
12. [Static Methods](#12-static-methods)
13. [Composition](#13-composition)
14. [Aggregation](#14-aggregation)
15. [Method Resolution Order (MRO)](#15-method-resolution-order-mro-and-diamond-inheritance)
16. [Function Decorators](#16-function-decorators)
17. [Class Decorators](#17-class-decorators)
18. [Property Decorators](#18-property-decorators-property-setter-and-deleter)
19. [Callable Classes](#19-callable-and-__call__)
20. [Custom Exceptions](#20-creating-a-custom-exception)
21. [Making a Custom Class Iterable](#21-make-a-custom-class-iterable)

---

### 1. Using `self`
A `Student` class with attributes initialized using `self` and a method to display details.

### 2. Using `cls`
A `Counter` class using a class variable to count instances, managed by a `cls` method.

### 3. Public Variables and Methods
A `Car` class demonstrating public access to variables and methods from outside the class.

### 4. Class Variables and Class Methods
A `Bank` class demonstrating class-level variable updates via class methods.

### 5. Static Variables and Static Methods
A `MathUtils` class using a static method to add two numbers without any instance or class variables.

### 6. Constructors and Destructors
A `Logger` class demonstrating the constructor and destructor with print statements.

### 7. Access Modifiers: Public, Private, and Protected
An `Employee` class showing different levels of access to its variables.

### 8. The `super()` Function
A `Teacher` class inheriting from `Person` and using `super()` to initialize the parent class.

### 9. Abstract Classes and Methods
A `Shape` abstract class with an abstract `area()` method implemented by the `Rectangle` class.

### 10. Instance Methods
A `Dog` class with instance variables and a method to bark using the dog's name.

### 11. Class Methods
A `Book` class maintaining a total count using a class method.

### 12. Static Methods
A `TemperatureConverter` class with a static method to convert Celsius to Fahrenheit.

### 13. Composition
An `Engine` object is passed to a `Car` class to demonstrate composition.

### 14. Aggregation
A `Department` class holding a reference to an external `Employee` object.

### 15. Method Resolution Order (MRO) and Diamond Inheritance
Demonstrates MRO using multiple inheritance (A → B, C → D).

### 16. Function Decorators
A decorator `log_function_call` that logs before calling the wrapped function.

### 17. Class Decorators
A decorator `add_greeting` that adds a `greet()` method to the target class.

### 18. Property Decorators: `@property`, `@setter`, and `@deleter`
A `Product` class using property decorators to manage the `_price` attribute.

### 19. `callable()` and `__call__()`
A `Multiplier` class that behaves like a function using the `__call__` method.

### 20. Creating a Custom Exception
Defines an `InvalidAgeError` and raises it in a function checking age validity.

### 21. Make a Custom Class Iterable
A `Countdown` class that can be iterated from a given number down to 0 using `__iter__()` and `__next__()`.

---

## How to Run

Make sure you have Python 3 installed. Clone the repository and run any `.py` file directly using:

```bash
python filename.py
```
## Author

**Hassan** – Web Developer & GIAIC Student

## License

This project is licensed under the [MIT License](LICENSE).
