"""
TSP
"""

class mundo:
    def __init__(self, lugares):
        self.lugares = []
        with open(lugares, 'r') as lugares:
            posicion = lugares.read()
            self.lugares.append(lugar(*lugar))

class lugar:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Posición: ({self.x}, {self.y})"

class ruta:
    def __init__(self):
        self.lugares = []

    @property
    def costo(self):
        pass

    def __repr__(self):
        return f"Ruta: {self.lugares} (Costo: {self.costo})"

class optimizador:
    def optimizar_ruta(self, lugares, algoritmo='greedy'):
        mundo = mundo(lugares)
        algoritmo = algoritmo()
        ruta = algoritmo.ejecutar()
        return ruta

