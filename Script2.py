#Romero Estrada Kenia Surisadahi
#Función que resuelve el problema de los valles

# Inicializamos las variables para empezar a nivel del mar y con 0 valles
def valles(recorrido):
    nivel_actual = 0
    numero_valles = 0

    # Actualizamos el nivel en el que estamos segun los pasos
    for paso in recorrido:
        if paso == 'U':
            nivel_actual += 1
        elif paso == 'D':
            nivel_actual -= 1

        # Verificamos si se recorrio un valle
        if paso == 'U' and nivel_actual == 0:
            numero_valles += 1

    return numero_valles

while True:
    print("¡Hola!")
    recorrido = input("Ingrese el recorrido (Usando solamente 'U' y/o 'D'): ")

    # Verificamos que la lista este conformada unicamente por letras U y D
    if all(paso in {'U', 'D'} for paso in recorrido) and recorrido:
        break
    else:
        print("Entrada no válida. Por favor, no deje el campo vacio e ingrese solo 'U' y/o 'D'.")

resultado = valles(recorrido)
#Mostramos el resultado
print(f"El número de valles es: {resultado}")

#Arbol Binario Ordenado
#Clase que representa a un nodo en un árbol binario.
class Nodo:
    #Inicializa un nodo con el valor dado.
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

#Clase que representa un arbol binario ordenado.
class ArbolBinarioOrdenado:
    #Inicializa el arbol binario
    def __init__(self):
        self.nodo_raiz = None

    #Inserta un nuevo nodo con el valor dado en el arbol binario
    def insertar(self, valor):
        self.nodo_raiz = self._insertar(self.nodo_raiz, valor)

    #Metodo para insertar recursivamente los nodos
    def _insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar(nodo.derecha, valor)

        return nodo

    # Realiza un recorrido pre-orden (raiz, izquierdo, derecho)
    def recorrido_preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.recorrido_preorden(nodo.izquierda)
            self.recorrido_preorden(nodo.derecha)

    # Realiza el recorrido in-orden (raiz, izquierdo, derecho)
    def recorrido_inorden(self, nodo):
        if nodo:
            self.recorrido_inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.recorrido_inorden(nodo.derecha)

    # Realiza el recorrido post-orden (izquierdo, raiz, derecho)
    def recorrido_postorden(self, nodo):
        if nodo:
            self.recorrido_postorden(nodo.izquierda)
            self.recorrido_postorden(nodo.derecha)
            print(nodo.valor, end=" ")


if __name__ == "__main__":
    arbol = ArbolBinarioOrdenado()

    print("Bienvenido al Arbol Binario")
    # Solicitar al usuario que ingrese valores uno por uno
    while True:
        valor = input("Ingrese el nodo a insertar o 'f' para finalizar: ")
        if valor.lower() == 'f':
            break

        try:
            valor = int(valor)
            arbol.insertar(valor)
        except ValueError:
            print("Por favor, ingrese un valor numero valido.")

    # Muestra el recorrido pre-orden (raiz, izquierdo, derecho)
    print("Recorrido Preorden:")
    arbol.recorrido_preorden(arbol.nodo_raiz)

    # Muestra el recorrido in-orden (raiz, izquierdo, derecho)
    print("\nRecorrido Inorden:")
    arbol.recorrido_inorden(arbol.nodo_raiz)

    # Muestra el recorrido post-orden (izquierdo, raiz, derecho)
    print("\nRecorrido Postorden:")
    arbol.recorrido_postorden(arbol.nodo_raiz)
