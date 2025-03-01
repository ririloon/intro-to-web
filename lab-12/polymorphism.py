class Bird:
    def fly(self):
        return "Flying high!"

class Airplane:
    def fly(self):
        return "Taking off into the sky!"

class Fish:
    def fly(self):
        return "I can't fly!"

for obj in [Bird(), Airplane(), Fish()]:
    print(obj.fly())