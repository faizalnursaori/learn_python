class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive(self):
        print(f"You drive the {self.color} {self.model}")