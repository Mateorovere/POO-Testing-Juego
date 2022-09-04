from test_carta import Carta
from test_mazo import Mazo

#class Mano(Mazo):
#    def __init__(self, nombre, cant, *args , **kwargs):
#        super().__init__(*args, **kwargs)
#        self.nombre = nombre
#        self.cant = cant
#       self.mano = []
#    def que_cartas(self):
#        #self.mezclar()
#        for cartax in list(range(self.cant)):
#           self.mano.append(self.sacar_carta())
#       return f"{self.nombre} saco las cartas : {self.mano}"
#  def añadir(self, i):
#        return self.mano.append(i) #ej 11, falta (11,12,13,14,15,16)

#Mateo = Mano("Mateo", 4)
#Mateo.mezclar()
#print(Mateo.que_cartas())
#mano = Mateo.mano

class Mano:
    def __init__(self, nombre, cant):
        self.nombre = nombre 
        self.cant = cant
        self.mazo = Mazo()
        self.noma = []
    def que_cartas(self):
        for cartax in list(range(self.cant)):
          self.noma.append(str(self.mazo.sacar_carta()))
        return f"{self.nombre} saco las cartas : {self.noma}"
    def quitar(self,index):
        return self.noma.pop(index) # no me gusta lo del pop aca
    def añadir(self,carta):
        return self.noma.append(str(self.mazo.sacar_carta()))
        
Mateo2 = Mazo()
Mateo = Mano("Mateo", 4)
print(Mateo.que_cartas())
Mateo.añadir("Caballo de Espada")
Mateo.quitar(1)
print(Mateo.noma)