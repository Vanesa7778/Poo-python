class Fruta:##se define una clase llamada fruta 
    def __init__(self,nombre,color):##se utiliza _init_ un constructor de la clase que inicializa las propiedades nombre y color
        self.nombre=nombre#asigna el nombre de la fruta a la propiedad 'nombre'
        self.color=color#asigna el color de la fruta a la propiedad 'color'
#metodo para mostrar informacion sobre la fruta
    def mostrarInformacion(self):
        print(f"{self.nombre} y es de color  {self.color}")#se imprime un mensaje con el nombre y el color de la fruta
#se crea una instancia llamada miFruta
miFruta = Fruta(nombre="fresa",color="rojo")
##se llama al metodo mostrarInformacion() de la instancia "miFruta"
miFruta.mostrarInformacion()