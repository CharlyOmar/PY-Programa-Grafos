from Grafos import Grafo

class main:
     
     g = Grafo()
  
     g.agregarVertice(1)
     g.agregarVertice(2)
     g.agregarVertice(3)
     g.agregarVertice(4)
     g.agregarVertice(5)

     g.agregarArista(1, 2, 3)
     g.agregarArista(1, 3, 1)
     g.agregarArista(2, 3, 7)
     g.agregarArista(2, 4, 5)
     g.agregarArista(2, 5, 1)
     g.agregarArista(3, 4, 2)
     g.agregarArista(4, 5, 7)

     g.camino_minimo(3)
     print(g.camino(5))
     g.imprimirGrafo()
