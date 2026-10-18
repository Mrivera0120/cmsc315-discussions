"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Keyboard:
    category = "Mechanical Keyboard"

    def __init__(self, brand, model, switch_type) :
        self.brand = brand
        self.model = model
        self.switch_type = switch_type

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Switches: {self.switch_type}")

    def change_switches(self, new_switches):
        if not new_switches.strip():
            print("Error: Switch type can't be empty.")
            return

        self.switch_type = new_switches
        print(f"Switches changed to: {self.switch_type}")

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class GamingKeyboard(Keyboard):
    def __init__(self, brand, model, switch_type, rgb_lighting):
        super().__init__(brand, model, switch_type)
        self.rgb_lighting = rgb_lighting

    def display_info(self):
        super().display_info()
        print(f"RGB Lighting: {self.rgb_lighting}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    keyboard1 = GamingKeyboard("Epomaker", "TH108", "Creamy Jade", True)
    keyboard2 = GamingKeyboard("Varmilo", "Minilo65", "Kaihl Prestige", False)

    print("\nClass variable through class: ")
    print(Keyboard.category)

    print("\nClass variable through object: ")
    print(keyboard1.category)

    keyboard1.connection = "Wireless"

    print("\nKeyboard 1 namespace: ")
    print(keyboard1.__dict__)

    print("\nKeyboard 2 namespace: ")
    print(keyboard2.__dict__)

    print("\nKeyboard Class Namespace: ")
    print(Keyboard.__dict__)
# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    keyboard_setup = {
        "keyboard": "Epomaker TH108",
        "accessories":  ["Wrist Rest", "Coiled Cable"]
    }

    shallow_copy = copy(keyboard_setup)
    deep_copy = deepcopy(keyboard_setup)

    keyboard_setup["accessories"].append("Keycap Puller")

    print("Original: ", keyboard_setup)
    print("Shallow Copy: ", shallow_copy)
    print("Deep Copy: ", deep_copy)

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Keyboard ===")
    keyboard1 = Keyboard("Epomaker", "TH108", "Creamy Jade")
    keyboard1.display_info()

    print("\n=== Gaming Keyboard ===")
    gaming_keyboard1 = GamingKeyboard("Redragon", "K762", "Creamy", True)
    gaming_keyboard1.change_switches("Akko Creamy Purple")
    gaming_keyboard1.display_info()

    print("\n=== Edge Case Test ===")
    gaming_keyboard1.change_switches("")
    print("Current switches: ", gaming_keyboard1.switch_type)

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()