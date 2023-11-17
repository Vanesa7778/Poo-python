#Consulte un ejemplo donde se declare una clase con atributos y métodos
#se define la clase Lapiz
class Lapiz:
#se establece un atributo de clase que representa el color del lapiz, establecido como "negro"
    color="negro"
#metodo para simular la accion de dibujar con el lapiz
    def dibujar(self):
        print("el lapiz esta dibujando")
#metodo para simular la accion de borrar con el lapiz
    def borrar(self):
        print("el lapiz esta borrando")
#seb crea instancia cuaderno
cuaderno= Lapiz()
cuaderno.dibujar()#se llama al metodo dibujar
cuaderno.borrar()#se llama al metodo borrar
