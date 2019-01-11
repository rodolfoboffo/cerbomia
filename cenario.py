import terreno
import random

class Cenario(object):
    
    def __init__(self, largura, altura, terrenos):
        self.largura = largura
        self.altura = altura
        self.terrenos = terrenos
    
    @staticmethod
    def geraCenario(largura, altura):
        numTerrenos = largura * altura
        posNascedouro = random.choice(range(numTerrenos))
        posAltar = random.choice(range(numTerrenos))
        while posAltar == posNascedouro:
            posAltar = random.choice(range(numTerrenos))
        

for i in range(90):
    print(random.choice(range(10)))