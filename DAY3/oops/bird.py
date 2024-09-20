class Bird:
    def fly(self):
        return 'Bird is flying...'
class Crow(Bird):
    def fly(self):
        return 'crow is flying...'
class Parrot(Bird):
    def fly(self):
        return 'parrot is flying...'
class Eagle(Bird):
    pass

def test_fly(bird):
    print(bird.fly())

Crow1 = Crow()
Parrot1 = Parrot()
Parrot2 = Parrot()
Eagle1 = Eagle()
test_fly(Crow1)
test_fly(Parrot1)
test_fly(Parrot2)
test_fly(Eagle1)