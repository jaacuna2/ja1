class Vehiculo:
    def __init__(self):
        self.marca = "Toyota"  # Atributo

    def mostrar_marca(self):
        print("La marca del vehículo es:", self.marca)

# Crear un objeto
mi_vehiculo = Vehiculo()
mi_vehiculo.mostrar_marca()
