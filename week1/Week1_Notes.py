class Dog(object):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Bark!")

    def speak(self):
        print("Hello, my name is %s" % self.name)

coco_dog = Dog('CoCo')
fido_dog = Dog('Fido')
stupid_dog = Dog('Duh')
fido_dog.bark()
coco_dog.speak()
fido_dog.speak()
stupid_dog.speak()
