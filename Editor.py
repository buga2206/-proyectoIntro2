
class Editor:
    def __init__(self):
        self.matriz = [[0 for _ in range(60)] for _ in range(60)]
        self.creador = ("Steven Pérez", "Daniel Burguer")
        self.estado = "En proceso"
    
    def get_matriz(self):
        return self.matriz

    def cargarImagen(self, filename):
        pass
    
    def editarImagen(self):
        pass

    def verImagen(self):
        pass

    def verMatrizNumerica(self):
        pass

    def cerrarImagen(self):
        pass

    def mostrarImagen(self):
        pass

    def zoomIn(self):
        pass

    def zoomOut(self):
        pass

    def rotarDerecha(self):
        pass

    def rotarIzquierda(self):
        pass

    def reflejoHorizontal(self):
        pass

    def reflejoVertical(self):
        pass

    def altoContraste(self):
        pass
    
    def negativo(self):
        pass

    def ascciArt(self):
        pass

"""
• Cargar imagen: se pide el nombre de un archivo en disco, se valida su existencia y se carga la 
imagen digitalizada en una matriz, las imágenes cargadas serán únicamente las ya creadas 
anteriormente por el programa.   

• Ver matriz: muestra la imagen creada en el archivo subido. 

• Ver matriz numérica: muestra la matriz cargada en su forma numérica. 
 
• Cerrar imagen: debe limpiar la pantalla y la matriz para poder cargar otra. 
• Zoom in: debe permitir escoger un área de la imagen (al menos indicar un cuadrante) y 
hacer un zoom (mostrarlo inmediatamente) sobre esa área. Esta función no modifica la 
matriz. 
• Zoom out: debe permitir retornar la imagen mostrada por medio de zoom in a su tamaño 
normal de despliegue. La matriz no es modificada. 
 
• Rotar a la derecha: esta función realiza la transpuesta (y la muestra) de la matriz actual, la 
cual es modificada. 
 
• Rotar a la izquierda: esta función convierte y muestra la matriz actual, de forma que última 
columna de la matriz se convierte en la última fila de la matriz resultante y así 
sucesivamente. 
 
• Reflejo horizontal: modifica la matriz convirtiendo la columna más a la izquierda en la 
columna más a la derecha, y así sucesivamente, mostrando la imagen resultante. 
 
• Reflejo vertical: muestra la imagen de la matriz modificada, convirtiendo la fila superior 
en la fila inferior, y así sucesivamente. 
 
• Alto contraste: convierte todos los valores entre 0 y 4 en 1 y todos los valores entre 5 y 9 
en 9, modificando la matriz y mostrándola. 
 
• Negativo: Revertir todos los valores en la matriz implica convertir los números más altos 
en sus contrapartes más pequeñas y viceversa. Por ejemplo, el 9 se convierte en 0, el 8 en 
1 y el 7 en 2. 
 
• ASCII-Art: los valores son codificadas, en nuestro caso mediante una tabla de caracteres 
del 0 al 9, donde 0 representa la mayor intensidad de luz (punto más claro) y 9 es la 
representación más oscura. 
"""