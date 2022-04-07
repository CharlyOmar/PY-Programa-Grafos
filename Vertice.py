class Vertice:
     def __init__(self, n):
          self.numero = n #Se refiere al numero de Vertice que es
          self.vecinos = []
          self.visitado = False
          self.padre = None
          self.peso = float('inf')

     def agregarVecino(self, vecino, p):
          if vecino not in self.vecinos:
               self.vecinos.append([vecino, p])
          