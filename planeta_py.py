class FormaDeVida:
    def __init__(self, nome:str, especie:str, nivel_energia:float):
        self.nome = nome
        self.especie = especie
        self.nivel_energia = nivel_energia

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nEspécie: {self.especie}\nNivel de Energia: {self.nivel_energia}"
    
    def ganho_energia (self, valor_atual, incremento, limite=100):
        return min(valor_atual + incremento, limite)
    
    def perda_energia (self, valor_atual, decremento, limite=0):
        return max(valor_atual - decremento, limite)
    
class Planta (FormaDeVida):
    def __init__(self, nome: str, especie: str, nivel_energia: float):
        super().__init__(nome, especie, nivel_energia)

    def fotossintese(self):
        self.nivel_energia += self.nivel_energia*0.6
        print("Fazendo fotossintese")

class Animal (FormaDeVida):
    def __init__(self, nome: str, especie: str, nivel_energia: float, dieta:str, porte=None):
        super().__init__(nome, especie, nivel_energia)
        self.dieta = dieta
        self.porte = porte
    
    def __str__(self) -> str:
        return super().__str__() + f"\nDieta: {self.dieta}"
    
    def comer(self, alimento):
        if alimento.especie == "Planta":
            alimento.nivel_energia = self.perda_energia(valor_atual=alimento.nivel_energia, decremento=30)
            self.nivel_energia = self.ganho_energia(valor_atual=self.nivel_energia, incremento=30)
            return True
        elif alimento.especie == "Animal":
            if alimento.porte > self.porte:
                self.nivel_energia = self.perda_energia(valor_atual=self.nivel_energia, decremento=15)
            else:
                alimento.nivel_energia = self.perda_energia(valor_atual=alimento.nivel_energia, decremento=60)
                self.nivel_energia = self.ganho_energia(valor_atual=self.nivel_energia,incremento=60)

class Planeta:
    def __init__(self):
        animais = [
            # Carnívoros (porte maior → vantagem em confrontos)
            Animal(nome="Leão", especie="Animal", nivel_energia=85.0, dieta="Carnívoro", porte=80),
            Animal(nome="Tigre", especie="Animal", nivel_energia=88.0, dieta="Carnívoro", porte=85),
            Animal(nome="Lobo Guará", especie="Animal", nivel_energia=65.0, dieta="Carnívoro", porte=50),
            Animal(nome="Onça-pintada", especie="Animal", nivel_energia=78.0, dieta="Carnívoro", porte=70),

            # Herbívoros (porte variável)
            Animal(nome="Vaca", especie="Animal", nivel_energia=70.0, dieta="Herbívoro", porte=60),
            Animal(nome="Coelho", especie="Animal", nivel_energia=40.0, dieta="Herbívoro", porte=10),
            Animal(nome="Elefante", especie="Animal", nivel_energia=95.0, dieta="Herbívoro", porte=90),
            Animal(nome="Girafa", especie="Animal", nivel_energia=75.0, dieta="Herbívoro", porte=70),
            Animal(nome="Cervo", especie="Animal", nivel_energia=55.0, dieta="Herbívoro", porte=30),
            Animal(nome="Capivara", especie="Animal", nivel_energia=50.0, dieta="Herbívoro", porte=20)
        ]
        plantas = [
            Planta(nome="Grama", especie="Planta", nivel_energia=15.0),
            Planta(nome="Eucalipto", especie="Planta", nivel_energia=50.0),
            Planta(nome="Bambu", especie="Planta", nivel_energia=30.0),
            Planta(nome="Alface", especie="Planta", nivel_energia=10.0),
            Planta(nome="Cacto", especie="Planta", nivel_energia=20.0),
            Planta(nome="Samambaia", especie="Planta", nivel_energia=12.0),
            Planta(nome="Carvalho", especie="Planta", nivel_energia=70.0),
            Planta(nome="Lavanda", especie="Planta", nivel_energia=8.0),
            Planta(nome="Girassol", especie="Planta", nivel_energia=25.0),
            Planta(nome="Orquídea", especie="Planta", nivel_energia=5.0)
        ]
        habitantes = [] 

   



animal1 = Animal(nome="Lobo", especie="Animal",nivel_energia=90.0, dieta="Carnívoro", porte=60)
animal2 = Animal(nome="Vaca", especie="Animal",nivel_energia=70.0, dieta="Herbívoro", porte=50)
planta1 = Planta(nome="Grama", especie="Planta", nivel_energia=80.0)

# print (planta1)
# planta1.fotossintese()
# print(planta1)
# print ("-"*30)

# print ("-"*10)
# print (animal2, "\n")
# print (planta1)
# print ("-"*30)
print ("Dia 1\n")
print (animal1, "\n")
print (animal2, "\n")
animal1.comer(animal2)
print ("Dia 2\n")
print (animal1, "\n")
print (animal2, "\n")
print ("Dia 3\n")
print (animal2,"\n")
print (planta1,"\n")
animal2.comer(planta1)
print (animal2,"\n")
print (planta1,"\n")
planta1.fotossintese()
print (planta1,"\n")
