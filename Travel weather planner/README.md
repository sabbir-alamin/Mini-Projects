# 🚗 Transport Decision Simulator

A beginner-friendly Python project that determines whether travel is possible based on different transportation conditions.

---

## Overview

This project demonstrates the use of:

- Boolean variables
- Conditional statements
- Nested `if` statements
- Logical operators (`and`, `or`, `not`)
- Comparison operators

The program evaluates multiple factors such as:

- Distance
- Weather
- Bicycle availability
- Car ownership
- Ride-sharing availability

and determines whether traveling is possible.

---

## Decision Rules

| Condition | Result |
|-----------|--------|
| Distance ≤ 1 mile and not raining | ✅ Travel Possible |
| Distance ≤ 1 mile and raining | ❌ Travel Not Possible |
| Distance between 2–6 miles without a bike | ❌ Travel Not Possible |
| Distance between 2–6 miles with a bike and not raining | ✅ Travel Possible |
| Distance > 6 miles with ride-sharing | ✅ Travel Possible |
| Distance > 6 miles with a car | ✅ Travel Possible |
| Distance > 6 miles with neither a car nor ride-sharing | ❌ Travel Not Possible |

---

## Technologies Used

- Python 3

---

## Learning Objectives

This project was created to practice:

- Boolean Logic
- Conditional Programming
- Decision Trees
- Code Readability
- Python Syntax

---

## Project Structure

```
transport-decision-simulator/
│
├── index.py
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt
```

---

## Running the Project

Clone the repository.

```bash
git clone https://github.com/yourusername/transport-decision-simulator.git
```

Navigate into the project.

```bash
cd transport-decision-simulator
```

Run the program.

```bash
python index.py
```

---

## Future Improvements

- Accept user input instead of hard-coded values
- Refactor into reusable functions
- Add unit tests
- Improve decision logic
- Add command-line arguments

---

## License

This project is licensed under the MIT License.
