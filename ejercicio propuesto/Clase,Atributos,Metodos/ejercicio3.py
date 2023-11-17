class Persona:#s define clase persona 
    def __init__(self,nombre,edad):#se utiliza _init_ un constructor de la clase que inicializa las propiedades nombre y edad
        self.nombre=nombre#asigna el nombre de persona a la propiedad 'nombre'
        self.edad=edad#asigna edad de persona  a la propiedad 'edad'
#metodo para imprimir un mensaje de presentacion
    def presentarse(self):
        print(f"yo me llamo {self.nombre} y tengo {self.edad} años de edad")##se imprime un mensaje que incluye el nombre y la edad de la persona
#se crea una instancia de la clase Persona llamada "vanesa"
vanesa= Persona(nombre="Vanesa", edad=17)
##se llama al metodo presentarse() de la instancia "vanesa"
vanesa.presentarse()