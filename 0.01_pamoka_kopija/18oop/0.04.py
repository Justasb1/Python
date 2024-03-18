class Robotai:
    name = None
    age = None
    enable = None

    def set_data(self, name, age, enable):
        self.name = name
        self.age = age
        self.enebale = enable

    def get_data(self):
        print(f'Cia Robotas {self.name}.\nJo duomenys:\nAmzius:{self.age}\nAr ijungas:{self.enable}')

languRobotas = Robotai('NoName', 3, False)
languRobotas.get_data()

print(languRobotas.__dict__)
