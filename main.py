import terreno
import logging
from raizes import Raiz, RaizBuilder
from aleatorio import Aleatorio
from genetico import Genetico
from ranking import MINIMIZACAO, MAXIMIZACAO

def main():
    logging.getLogger().setLevel(logging.INFO)
    f = lambda r: pow((r.getValor() - 300512.0), 2)

    builder = RaizBuilder()
    pop = builder.geraAleatorios(50)
    g = Genetico(
        builder,
        f,
        proporcaoFilhos=0.3,
        manterPais=True,
        maxmin=MINIMIZACAO,
        probMutacao=0.1,
        probCrossover=0.3
        )
    ranking = g.evoluir(pop, 10000, pontuacaoSatisfatoria=pow(0.000001, 2))
    print(ranking.getPopulacao()[0])

if __name__ == '__main__':
    main()