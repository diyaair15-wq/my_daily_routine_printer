class china:
    def capital(self):
        print("Beijing is the capital of China.")
    def language(self):
        print("The language of China is Mandarin.")
    def type(self):
        print("China is a country in East Asia.")
class japan:
    def capital(self):
        print("Tokyo is the capital of Japan.")
    def language(self):
        print("The language of Japan is Japanese.")
    def type(self):
        print("Japan is an island country in East Asia.")
obj_china = china()
obj_japan = japan()

for crountry in (obj_china, obj_japan):
    crountry.capital()
    crountry.language()
    crountry.type()