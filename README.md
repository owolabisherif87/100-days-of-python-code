# 🧮 Basic Calculator — 100 Days of Python

A simple command-line calculator built with **Python** as part of my **100 Days of Python Code** journey.

The calculator allows users to perform the four basic arithmetic operations:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)

The project uses Python's built-in **`eval()` function** to evaluate the arithmetic expression entered by the user.

## 📌 Project Overview

The purpose of this project is to create a straightforward calculator while practicing fundamental Python concepts such as:

- User input
- Variables
- Strings
- Functions
- Arithmetic operators
- The `eval()` function
- Exception handling
- Loops and program flow

The user enters an arithmetic expression, and the program evaluates it and displays the result.

For example:

```text
Enter a calculation: 10 + 5
Result: 15
```

Or:

```text
Enter a calculation: 20 / 4
Result: 5.0
```

## ✨ Features

- Perform addition
- Perform subtraction
- Perform multiplication
- Perform division
- Accept arithmetic expressions directly from the user
- Use Python's `eval()` function to calculate expressions
- Handle invalid expressions
- Provide results directly in the terminal
- Simple and beginner-friendly implementation

## 🛠️ Technologies Used

- **Python 3**
- Python's built-in `eval()` function
- Command-line interface

No external libraries or dependencies are required.

## 📂 Project Structure

```text
basic-calculator/
│
├── calculator.py
└── README.md
```

### `calculator.py`

Contains the calculator's Python code, including user input, expression evaluation, and error handling.

### `README.md`

Contains the documentation for the project.

## 🚀 Getting Started

### Prerequisites

You need **Python 3** installed on your computer.

Check your Python installation with:

```bash
python --version
```

or:

```bash
python3 --version
```

### Running the Program

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate into the project directory:

```bash
cd basic-calculator
```

Run the program:

```bash
python calculator.py
```

Depending on your system, you may need:

```bash
python3 calculator.py
```

## 💻 How It Works

The calculator takes an arithmetic expression as input from the user.

A simplified version of the core functionality looks like this:

```python
calculation = input("Enter a calculation: ")
result = eval(calculation)
print(f"Result: {result}")
```

If the user enters:

```text
10 + 5
```

Python evaluates the expression:

```python
eval("10 + 5")
```

and returns:

```text
15
```

This means the calculator can work with different arithmetic expressions without needing a separate `if` statement for every operation.

### Examples

#### Addition

```text
Enter a calculation: 15 + 7
Result: 22
```

#### Subtraction

```text
Enter a calculation: 15 - 7
Result: 8
```

#### Multiplication

```text
Enter a calculation: 15 * 7
Result: 105
```

#### Division

```text
Enter a calculation: 15 / 3
Result: 5.0
```

## 🧠 Understanding `eval()`

The most important Python concept introduced by this project is `eval()`.

`eval()` evaluates a Python expression provided as a string and returns the resulting value.

For example:

```python
eval("5 + 3")
```

returns:

```text
8
```

Similarly:

```python
eval("10 * 4")
```

returns:

```text
40
```

This makes `eval()` convenient for creating a very small calculator because the user can enter an expression containing different arithmetic operators.

### Why Use `eval()`?

Using `eval()` keeps the calculator implementation simple.

Instead of writing separate logic for every operation:

```python
if operation == "+":
    ...
elif operation == "-":
    ...
elif operation == "*":
    ...
elif operation == "/":
    ...
```

the program can pass the expression directly to Python:

```python
result = eval(calculation)
```

This is particularly useful for a small learning project where the goal is to experiment with Python functionality and understand how expressions can be evaluated dynamically.

## ⚠️ Security Consideration

It is important to understand that **`eval()` should not normally be used on untrusted user input**.

The reason is that `eval()` evaluates Python code, not just mathematical calculations. If arbitrary input is passed directly to `eval()`, a malicious user could potentially execute Python code.

For example, this is potentially dangerous:

```python
eval(user_input)
```

when `user_input` comes directly from an untrusted source.

For this reason, this project is intended as a **learning exercise and local beginner project**, rather than a calculator that should be deployed publicly or used to process untrusted input.

A production-ready calculator would typically validate the input or use a safer expression parser instead of directly evaluating arbitrary Python code.

## 🧯 Error Handling

Invalid expressions can cause Python exceptions.

For example, entering:

```text
10 /
```

does not represent a valid Python expression.

A `try`/`except` block can be used to prevent the program from crashing:

```python
try:
    result = eval(calculation)
    print(f"Result: {result}")
except Exception:
    print("Invalid calculation.")
```

This provides a better experience when the user enters an invalid expression.

Division by zero should also be considered:

```text
Enter a calculation: 10 / 0
```

Python will raise a `ZeroDivisionError`.

Handling these situations is an important part of making the calculator more robust.

## 🧩 Python Concepts Practiced

### User Input

The `input()` function allows the program to receive an expression from the user:

```python
calculation = input("Enter a calculation: ")
```

### Strings

The user's calculation is initially stored as a string:

```python
"10 + 5"
```

`eval()` then evaluates that string as a Python expression.

### Arithmetic Operators

The calculator supports Python's standard arithmetic operators:

| Operator | Operation      | Example |
| -------- | -------------- | ------- |
| `+`      | Addition       | `5 + 2` |
| `-`      | Subtraction    | `5 - 2` |
| `*`      | Multiplication | `5 * 2` |
| `/`      | Division       | `5 / 2` |

### Functions

The calculator can be organized into functions to make the code easier to understand and reuse.

### Exception Handling

`try` and `except` can be used to handle invalid expressions and prevent unexpected program termination.

### `eval()`

The project introduces dynamic expression evaluation and demonstrates one of Python's built-in functions.

## 🎯 Learning Objectives

The main goal of this project is to strengthen my understanding of Python through a small, practical application.

By completing this project, I am practicing how to:

- Accept input from a user
- Work with strings and expressions
- Use Python arithmetic operators
- Use built-in Python functions
- Understand how `eval()` works
- Handle exceptions
- Build a simple command-line application
- Think about security when processing user input
- Improve and extend an existing program

## 🔮 Possible Future Improvements

As part of my continued Python learning, the calculator could be improved by adding:

- [ ] A continuous calculation loop
- [ ] A quit option
- [ ] Calculation history
- [ ] Better input validation
- [ ] Support for additional mathematical operations
- [ ] A safer alternative to `eval()`
- [ ] Automated tests
- [ ] A graphical user interface
- [ ] Better error messages
- [ ] Improved result formatting

## 📚 What I Learned

This project demonstrates how a relatively small amount of Python code can be used to create an interactive application.

One of the main lessons from this project is understanding how `eval()` can evaluate an expression stored as a string. At the same time, it highlights an important programming principle: **a function being convenient does not necessarily mean it is appropriate for every situation**.

Using `eval()` directly on user input is acceptable for this small, controlled learning exercise, but understanding its security implications is an important part of learning Python.

## 🐍 100 Days of Python Code

This calculator is part of my **100 Days of Python Code** journey.

The challenge focuses on consistently writing Python, building projects, learning programming concepts, and improving problem-solving skills through hands-on practice.

This project represents another step toward becoming more comfortable with Python and turning programming concepts into working applications.

## 📄 License

This project is intended for educational and learning purposes. Feel free to use it as a reference, experiment with the code, and extend it with your own features.

---

**Project:** Basic Calculator
**Language:** Python 3
**Challenge:** 100 Days of Python Code
**Level:** Beginner
**Operations:** Addition, Subtraction, Multiplication, Division
**Main Python Feature:** `eval()`

> One small Python project at a time. 🐍
