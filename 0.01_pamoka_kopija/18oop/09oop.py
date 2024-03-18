#__del__
#__new__

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Jungiames prie db {self.user} {self.psw} {self.port}')

    def __del__(self):
        DataBase.__instance = None
        print(f'{self} istrintas')

db1 = DataBase('root','123',8000)
db2 = DataBase('root2','456',9898)

print(id(db1), id(db2))
db = 5
print(id(db1), id(db2))
db2 = 8
db3 = DataBase('root3','456', 8008)
