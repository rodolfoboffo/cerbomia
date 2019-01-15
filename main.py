import terreno
import logging
from raizes import Raiz
from aleatorio import Aleatorio
from genetico import Genetico
from ranking import MINIMIZACAO, MAXIMIZACAO

def main():
    logging.getLogger().setLevel(logging.INFO)
    f = lambda r: pow((r.f - 300512.0), 2)

    pop = Raiz.geraAleatorios(50)
    g = Genetico(
        f,
        proporcaoFilhos=0.3,
        manterPais=True,
        maxmin=MINIMIZACAO,
        probMutacao=0.1,
        probCrossover=0.3
        )
    ranking = g.evoluir(pop, 10000, pontuacaoSatisfatoria=pow(0.000001, 2))
    print(ranking.getPopulacao()[0])

    a = Aleatorio(
        f,
        maxmin=MINIMIZACAO,
        )
    ranking = a.iterar(pop, 10000, pontuacaoSatisfatoria=pow(0.000001, 2))

    print(ranking.getPopulacao()[0])
    #print('{0:032b}'.format(g.geraMascaraCruzamento(4, 0.1)))
    #g.fazCruzamentoIndividuos(pop[0], pop[1], 0.1)


if __name__ == '__main__':
    main()