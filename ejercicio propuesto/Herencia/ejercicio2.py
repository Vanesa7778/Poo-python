class Comida:
    def __init__(self, nombre):##se utiliza __init_ un constructor de la clase que inicializa la propiedad nombre
        self.nombre = nombre
#metodo para describir comida
    def describir(self):
        print(f"Este postre se llama {self.nombre}")#se imprime este mensaje
#la clase Postre hereda de la clase Comida
class Postre(Comida):
    def __init__(self, nombre, sabor):
        super().__init__(nombre)#se llama al constructor de la clase padre usando super()
        self.sabor = sabor#asigna el sabor al atributo 'sabor'

    def disfrutar(self):#se crea un metodo llamado disfrutar
        print(f"¡Disfruta el postre con sabor a {self.sabor}!")#se imprime este mensaje

# Se crea una instancia llamada miPostre
miPostre = Postre(nombre="Tiramisu", sabor="café")#se pone sus valores a los parametros

miPostre.describir()  # Se llama al metodo describir de la instancia miPostre
miPostre.disfrutar()  # Se llama al metodo disfrutar de la instancia miPostre
