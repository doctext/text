
#Encapsulation
class hero:
    def __init__(self,nama,darah,kekuatan):
        self.__nama = nama
        self.__darah = darah
        self.__kekuatan = kekuatan
rizkybillar = hero("rizkybillar",5000,2500)
print(rizkybillar.__dict__)
    

#Polymorphism
class tank:
    def ulti(self):
        return "tank melakukan ulti kepada musuh"
class core:
    def ulti(self):
        return "core melakukan ulti kepada musuh"
obj_tank = tank()
obj_core = core()

for obj in [obj_tank, obj_core]:
    print(obj.ulti())