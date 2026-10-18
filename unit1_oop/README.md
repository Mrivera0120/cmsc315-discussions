# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives![img.png](img.png)

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

##  Implementation Documentation
### Parent Class
I created a parent class named `Keyboard` to represent mechanical keyboards. The class included a shared class variable, `category`, and three instance variables: `brand, model,` and `switch_type`.
I used the `__init__()` constructor to initialize each keyboard's attributes and created a `display_info()` method to display its information. 

### Child CLass and Inheritance
I also created a child class named `GamingKeyboard` that inherited from `Keyboard`. I used `super()` to initialize the inherited attributes and added an `rgb_lighting` attribute.
I also overrode the `display_info()` method to display the gaming keyboard's additional information while reusing the parent's method. 

### Class and Instance Namespaces 
I created two `GamingKeyboard` objects to demonstrate class and instance namespaces. I accessed the `category` class variable through both the class and an object. 
I add a `connection` attribute to only one keyboard and used `__dict__` to examine the objects' individual namespaces and the class namespace.

### Shallow and Deep Copying
I created a dictionary representing a keyboard setup with a nested list of accessories. I used `copy()` and `deepcopy()` to create shallow and deep copies. 
After modifying the original accessories list, I displayed all three dictionaries to demonstrate that the shallow copy shared the nested list while the deep copy remained independent. 

### Testing
I complete the `main()` function by creating objects from both the parent and child classes and calling their methods. I also called the namespace and copying demonstration functions. 
I ran the program in IntelliJ and verified that it completed successfully without errors. 

### Student-Created Extension
I further added a `change_switches()` method to the `Keyboard` class to allow an existing keyboard object's switch type to be updated. 
Because `GamingKeyboard` inherited from `Keyboard`, the child class could also use this method. I demonstrated the extension by chaning a gaming keyboard's switches and displaying the updated information.

### Edge Case Testing
I tested the `change_swtiches()` method by passing an empty string as the new switch type. I added an input validation to prevent empty switch names from replacing the keyboard's existing switch type. 
When I ran the test, the program displayed an error message and preserved the previously assigned switch type, `Akko Creamy Purple`. 

### Real-World Application
This program demonstrated how object-oriented programming could be used in a keyboard inventory or customization application. Inheritance allowed different keyboard types to share common attributes and methods, 
whiel individual objects maintained their own configurations. The switch-swapping feature demonstrated how an existing keyboard's configuration could be updated without creating a new object. 
