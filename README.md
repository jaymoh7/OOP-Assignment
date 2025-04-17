# Object-Oriented Programming Assignments

This repository contains two Python assignments demonstrating core Object-Oriented Programming (OOP) concepts.

## Assignment 1: Book Class Hierarchy

This assignment implements a book classification system with inheritance and polymorphism.

### Features

- **Base `Book` class** with common attributes and functionality:
  - Basic properties (title, author, pages, publish year)
  - Reading tracking (current page, bookmarks)
  - Progress calculation

- **Derived classes** with specialized behavior:
  - `Fiction`: Tracks genre and characters
  - `NonFiction`: Handles subject matter and note-taking

### Usage Example

```python
# Create different types of books
novel = Fiction("The Great Gatsby", "F. Scott Fitzgerald", 180, 1925, "Classic")
novel.add_character("Jay Gatsby")

textbook = NonFiction("Python Crash Course", "Eric Matthes", 544, 2019, "Programming")
textbook.add_note(42, "Important section on lists!")

# Demonstrate reading
novel.read(50)  # Read 50 pages
novel.bookmark()  # Bookmark current position

# Show progress
print(f"Reading progress: {novel.get_reading_progress():.1f}%")

# Access notes
print(textbook.get_notes())
```

## Assignment 2: Vehicle Polymorphism Challenge

This assignment demonstrates polymorphism through different vehicle implementations.

### Features

- **Base `Vehicle` class** with common functionality:
  - Movement tracking
  - Speed control
  - Basic operations (start, stop)

- **Specialized vehicles** with unique behavior:
  - `Car`: Road-based transportation with honking capability
  - `Boat`: Water-based transportation with anchoring
  - `Plane`: Air-based transportation with altitude control

### Polymorphism Example

```python
# Create different vehicle objects
sedan = Car("Toyota Camry", 120, "Hybrid")
yacht = Boat("Sea Breeze", 35, "Sailing Yacht")
jet = Plane("Boeing 737", 550, 41000)

# Store in a common list
vehicles = [sedan, yacht, jet]

# Each vehicle moves differently despite the same method call
for vehicle in vehicles:
    print(vehicle.move())
```

## Key OOP Concepts Demonstrated

1. **Encapsulation**: Data and methods bundled together in classes
2. **Inheritance**: Child classes extend parent functionality
3. **Polymorphism**: Same method behaves differently in different classes
4. **Constructors**: Special methods to initialize objects
5. **Method Overriding**: Child classes implement parent methods differently

## Running the Code

Each assignment includes a demonstration section that runs when the file is executed directly. To run these examples:

```
python book_class_hierarchy.py
python vehicle_polymorphism.py
```

## Project Structure

```
.
├── README.md
├── book_class_hierarchy.py    # Assignment 1 implementation
└── vehicle_polymorphism.py    # Assignment 2 implementation
```
