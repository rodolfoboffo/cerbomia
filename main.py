import terreno
from raizes import Raiz
from genetico import Genetico, MINIMIZACAO

def main():
    # print(terreno.MAPA_DE_TERRENOS)
    f = lambda r: abs((r.f - 1.0)*(r.f - 3.0))
    pop = Raiz.geraRaizesAleatorias(10)
    g = Genetico(Raiz.getTamanhoGenoma(), f, pop, maxmin=MINIMIZACAO)
    g.evoluir(1)
    

if __name__ == '__main__':
    main()