class Robotai:
    def __init__(self, name, age, enable, force):
        self.__name = name
        self._age = age
        self._enable = enable
        self._force = force

class DulkiuSiurbliaiRobotai:
    def __init__(self, ratai, siurbimoGalia, talpaDulkiu, plovimas):
        self.ratai = ratai
        self.siurbimoGalia = siurbimoGalia
        self.talpaDulkiu = talpaDulkiu
        self.plovimas = plovimas

class languRobotai:
    def __init__(self, plovimoForma, skyscioPurskimoFunkcija, valdymoPultelis):
        self.plovimoForma = plovimoForma
        self.skyscioPurskimoFunkcija = skyscioPurskimoFunkcija
        self.valdymoPultelis = valdymoPultelis

kazkoksRobotas = Robotai('Alexis', 2, True, 1.1)
kazkoksSiurblys = DulkiuSiurbliaiRobotai(3, 0.25, 0.5)
kazkoksLangu = languRobotai('Square', False, True)