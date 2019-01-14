import terreno
import logging
from raizes import Raiz
from genetico import Genetico, MINIMIZACAO

def main():
    logging.getLogger().setLevel(logging.INFO)
    # print(terreno.MAPA_DE_TERRENOS)
    f = lambda r: pow((r.f - 3512.0)*(r.f - 8913.0), 4)
    pop = Raiz.geraRaizesAleatorias(50)
    g = Genetico(
        f,
        proporcaoFilhos=0.3, 
        manterPais=True, 
        maxmin=MINIMIZACAO, 
        probMutacao=0.1, 
        probCrossover=0.3
        )
    ranking = g.evoluir(pop, 1000000, pontuacaoSatisfatoria=pow(0.0000001, 4))
    print(ranking.getPopulacao()[0])
    #print('{0:032b}'.format(g.geraMascaraCruzamento(4, 0.1)))
    #g.fazCruzamentoIndividuos(pop[0], pop[1], 0.1)


if __name__ == '__main__':
    main()