
class Editor:
    def __init__(self):
        self.matriz = [[0 for _ in range(60)] for _ in range(60)]
        self.creador = ("Steven Pérez", "Daniel Burguer")
        self.estado = "En proceso"
    
    def get_matriz(self):
        return self.matriz