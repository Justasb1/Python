class Robotai:
    def __init__(self, name, age, enable, force):
        self.__name = name
        self._age = age
        self._enable = enable
        self._force = force

class DulkiuSiurbliaiRobotai(Robotai):
    def __init__(self,name, age, enable, force, ratai, siurbimoGalia, talpaDulkiu, plovimas):
        super().__init__(name, age, enable, force)
        self.ratai = ratai
        self.siurbimoGalia = siurbimoGalia
        self.talpaDulkiu = talpaDulkiu
        self.plovimas = plovimas

class languRobotai(Robotai):
    def __init__(self, name, age, enable, force,  plovimoForma, skyscioPurskimoFunkcija, valdymoPultelis):
        self.plovimoForma = plovimoForma
        self.skyscioPurskimoFunkcija = skyscioPurskimoFunkcija
        self.valdymoPultelis = valdymoPultelis

kazkoksRobotas = Robotai('Alexis', 2, True, 1.1)
kazkoksSiurblys = DulkiuSiurbliaiRobotai('Xiomi', 4, True, 1.1, 3, 0.25, 0.5, False)
kazkoksLangu = languRobotai('Noname', False, 1.1, 3, 0.25, 0.5, False)