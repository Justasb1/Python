class Robotai:
    def __init__(self, name=None, age=None, enable=None):
        self.name = None
        self.age = None
        self.enable = None

        self.get_data()
    def get_data(self):
        print(f'Cia Robotas {self.name}.\nJo duomenys:\nAmzius:{self.age}\nAr ijungas:{self.enable}')

languRobotas = Robotai('NoName', 3, False)
grinduRobotas = Robotai('Xiomi', 5, True)
virtuvesRobotas = Robotai("Kopustas")
kazkoksRobotas = Robotai(age = 7, enable=True, name='Gerutis')

print(languRobotas.__dict__)
