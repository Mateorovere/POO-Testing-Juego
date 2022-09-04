import random 
from test_carta import Carta
class Mazo:
  def __init__(self):
    self.palos = ["Espada", "Basto" , "Copas", "Oro"]
    self.valores = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
    self.comodin = 2
    self.cartas = []
    self.mezclado = []
    for numero in self.valores:
      for palo in self.palos:
        self.cartas.append(str(Carta(numero,palo)))
    self.cartas.append("Comodin")
    self.cartas.append("Comodin")
  def cant_cartas(self):
    return len(self.cartas) + self.comodin
  def mezclar(self):                 #aca es el ej 6
    self.mezclado = random.sample(self.cartas,50)
    return self.mezclado
  def Sacar(self, cart):
    if cart not in self.cartas:
      return False
    if cart in self.cartas:
      self.cartas.remove(cart)
      return True
  def sacar_carta(self):
    return str(self.cartas.pop(0))
  def vacio(self):
    if len(self.cartas) == 0:
      print("No hay cartas")
    if len(self.cartas) > 0:
      print(f"todavia hay {len(self.cartas)} cartas")
    if len(self.cartas) < 0:
      print("Cantidad negativa, Error")

mazoesp = Mazo()
print(mazoesp.sacar_carta())
#def test_cant_carta():
#  assert mazoesp.cant_cartas() == 50
#def test_verif_carta():
#  assert "Rey de Espada" in mazoesp.cartas
#def test_sacar_carta():
#  assert "Rey de Espada" in mazoesp.cartas
#  assert mazoesp.Sacar("Rey de Espada") 
#  assert not "Rey de Espada" in mazoesp.cartas
#  assert not mazoesp.Sacar("Rey de Espada")