class Parent:
    def __init__(self, last_name, eye_color):
        print("Init Parent")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name: " + self.last_name)
        print("Eye color: " + self.eye_color)


class Child(Parent):
    def __init__(self, last_name, eye_color, toys_number):
        print("Init Child")
        super().__init__(last_name, eye_color)
        self.toys_number = toys_number

    def show_info(self):
        super().show_info()
        print("Toys number: " + str(self.toys_number))


billy_cyrus = Parent("cyrus", "blue")
billy_cyrus.show_info()
print("==========")
miley_cyrus = Child("cyrus", "blue", 5)
miley_cyrus.show_info()