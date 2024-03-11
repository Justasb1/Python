class Robotai:
    '''Dokumentacija apie klase robotai'''
    name = None
    age = None
    enable = None

    def startRobot(self, val, min):
        self.val = val
        self.min = min

languRobotas = Robotai()
grinduRobotas = Robotai()

# Robotai.pasisveikinimas()

languRobotas.startRobot(15, 25)
grinduRobotas.startRobot(19, 28)

print(f'Langu robotas startavo {languRobotas.val} : {languRobotas.min}')
