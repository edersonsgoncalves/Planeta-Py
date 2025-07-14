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
        self.nivel_energia = 100
class Animal (FormaDeVida):
    def __init__(self, nome: str, especie: str, nivel_energia: float, dieta:str):
        super().__init__(nome, especie, nivel_energia)
        self.dieta = dieta
    
    def __str__(self) -> str:
        return super().__str__() + f"\nDieta: {self.dieta}"
    
    def comer(self, alimento):
        self.alimento = alimento


animal1 = Animal(nome="Lobo", especie="Selvagem",nivel_energia=90.0, dieta="Carnívoro")

print (animal1)