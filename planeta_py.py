class FormaDeVida:
    def __init__(self, nome:str, especie:str, nivel_energia:float):
        self.nome = nome
        self.especie = especie
        self.nivel_energia = nivel_energia

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nEspécie: {self.especie}\nNivel de Energia: {self.nivel_energia}"
    
class Planta (FormaDeVida):
    def __init__(self, nome: str, especie: str, nivel_energia: float):
        super().__init__(nome, especie, nivel_energia)

    def fotossintese(self):
        self.nivel_energia = 100.0
        print("Fazendo fotossintese")
class Animal (FormaDeVida):
    def __init__(self, nome: str, especie: str, nivel_energia: float, dieta:str, porte=None):
        super().__init__(nome, especie, nivel_energia)
        self.dieta = dieta
        self.porte = porte
    
    def __str__(self) -> str:
        return super().__str__() + f"\nDieta: {self.dieta}"

    def ganho_energia (self, valor_atual, incremento, limite=100):
        return min(valor_atual + incremento, limite)
    
    def perda_energia (self, valor_atual, decremento, limite=0):
        return max(valor_atual - decremento, limite)
    
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
print (animal2)
animal2.comer(planta1)
print (animal2)