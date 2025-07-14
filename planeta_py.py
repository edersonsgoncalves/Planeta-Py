class FormaDeVida:
    def __init__(self, nome:str, especie:str, nivel_energia:float):
        self.nome = nome
        self.especie = especie
        self.nivel_energia = nivel_energia

    def __str__(self) -> str:
        return f""
    
class Planta (FormaDeVida):
    def __init__(self, nome: str, especie: str, nivel_energia: float):
        super().__init__(nome, especie, nivel_energia)

    def fotossintese(self):
        self.nivel_energia = 100
class Animal (FormaDeVida):
    def __init__(self, nome: str, especie: str, nivel_energia: float):
        super().__init__(nome, especie, nivel_energia)