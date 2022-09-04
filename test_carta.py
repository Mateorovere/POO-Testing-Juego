class Carta:
  def __init__(self,numero,palo):
    self.numero = numero
    self.palo = palo
  def __str__(self):
    if self.numero in [1,2,3,4,5,6,7,8,9,10,11,12] and self.palo in ["Espada", "Basto" , "Copas", "Oro"]:
      if self.palo != "Comodin":
        if self.numero == 1:
          self.numero = "As"
        elif self.numero == 10:
          self.numero = "Sota"
        elif self.numero == 11:
          self.numero = "Caballo"
        elif self.numero == 12:
          self.numero = "Rey"
        return f"{self.numero} de {self.palo}"
    elif self.palo == "Comodin":
      return "Comodin"
    else:
      return "valor no valido"
  def __eq__(self,other):
    return self.palo == other.palo and self.numero == other.numero