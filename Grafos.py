from Vertice import Vertice

class Grafo:
     def __init__(self):
          self.vertices = {} 
     
     def agregarVertice(self, index):
          if index not in self.vertices:
               self.vertices[index]=Vertice(index)

     def agregarArista(self, Vert1, Vert2, peso):
          if Vert1 in self.vertices and Vert2 in self.vertices:
               self.vertices[Vert1].agregarVecino(Vert2, peso)
               self.vertices[Vert2].agregarVecino(Vert1, peso)
     
     def camino(self, verticeDestino):
          camino=[]
          actual = verticeDestino
          while actual != None: #Mientras el vertice actual sea diferente de vacio
               camino.insert(0, actual) #Se inserta el vertice actual en el arreglo "camino"
               actual = self.vertices[actual].padre #actual es igual al vertice padre del vertice actual

          return "El camino mínimo es: "+ str(camino) + ", el peso del camino es: " + str(self.vertices[verticeDestino].peso)

     def minimo(self, lista):
          if len(lista) > 0:
               m = self.vertices[lista[0]].peso
               v = lista[0]
               for e in lista:
                    if m > self.vertices[e].peso:
                         m = self.vertices[e].peso
                         v = e
               return v

     def camino_minimo(self, VertInicial):
          if VertInicial in self.vertices:
               self.vertices[VertInicial].peso = 0
               actual = VertInicial
               noVisitados = []

               for v in self.vertices:
                    if v != actual:
                         self.vertices[v].peso = float('inf') #Se asigna un peso infinito a cada uno de los vertices
                    self.vertices[v].padre = None
                    noVisitados.append(v)

               while len(noVisitados)>0: #Mientras existan vertices no visitados
                    for vecino in self.vertices[actual].vecinos:
                         if self.vertices[vecino[0]].visitado == False:
                              if self.vertices[actual].peso + vecino[1]<self.vertices[vecino[0]].peso:
                                   self.vertices[vecino[0]].peso = self.vertices[actual].peso + vecino[1]
                                   self.vertices[vecino[0]].padre = actual
                    self.vertices[actual].visitado = True
                    noVisitados.remove(actual)
                    actual = self.minimo(noVisitados)
          else:
               print("\n\t\tPor favor introduce un vertice existente\n")
               
     def imprimirGrafo(self):
          print("\nDescripción del grafo: ")
          for vertice in self.vertices:
               if (self.vertices[vertice].padre == None):
                    padre = " sin llegar de alguna arista"
               else:
                    padre = str(" llegando de la arista "+str(self.vertices[vertice].padre))
               print("La ARISTA "+str(vertice) +" tiene un PESO de "+str(self.vertices[vertice].peso)+padre)

