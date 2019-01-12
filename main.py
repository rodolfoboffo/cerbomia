import terreno
from raizes import Raiz
from genetico import Genetico, MINIMIZACAO

def main():
    # print(terreno.MAPA_DE_TERRENOS)
    f = lambda r: abs((r.f - 1.0)*(r.f - 3.0))
    pop = Raiz.geraRaizesAleatorias(10)
    g = Genetico(f, maxmin=MINIMIZACAO)
    #g.evoluir(pop, 1)
    #print('{0:032b}'.format(g.geraMascaraCruzamento(4, 0.1)))
    #g.fazCruzamentoIndividuos(pop[0], pop[1], 0.1)


if __name__ == '__main__':
    main()