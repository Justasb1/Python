class Robotai:
    def __init__(self, name, age, enable):
        print(f'Kuriam objekta {self}')
        self.name = name
        self.age = age
        self.enable = enable

    def __del__(self):
        print(f'Objektas {self} sunaikintas')

languRobotas = Robotai('NoName', 3, False)
grinduRobotas = Robotai('Xiomi', 5, True)

print(type(languRobotas))
languRobotas = 5
print(type(languRobotas))