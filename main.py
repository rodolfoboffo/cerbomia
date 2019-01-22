import random
import logging
from raizes import Raiz, RaizBuilder
from ffn import FFNBuilder, FeedForwardNet, CAMADA_RELU, CAMADA_SOFTMAX, CAMADA_ENTRADA, CAMADA_LINEAR
from aleatorio import Aleatorio
from genetico import Genetico
from ranking import MINIMIZACAO, MAXIMIZACAO

def raizFuncaoObjetivo(r):
    return pow((r.getValor() - 300512.0), 2)

aleatorios = [random.uniform(-100.0, 100.0) for i in range(50)]
def ffnFuncaoObjetivo(ffn):
    f = lambda x: pow(ffn.alimenta([x])[0] - ((6.0*x-1.0)), 2.0)

    erroTotal = 0.0
    for aleatorio in aleatorios:
        erro = f(aleatorio)
        erroTotal += erro
    return erroTotal / 50.0

def main():
    logging.getLogger().setLevel(logging.INFO)

    # builder = RaizBuilder()
    # pop = builder.geraAleatorios(20)
    # g = Genetico(
    #     builder,
    #     raizFuncaoObjetivo,
    #     proporcaoFilhos=0.3,
    #     manterPais=True,
    #     maxmin=MINIMIZACAO,
    #     probMutacao=0.1,
    #     probCrossover=0.7
    #     )
    # ranking = g.evoluir(pop, 10000, pontuacaoSatisfatoria=pow(0.000001, 2))
    # print(ranking.getPopulacao()[0])
    
    builder = FFNBuilder()
    builder.adicionaCamadaEntrada(1) \
        .adicionaCamada(2, CAMADA_RELU) \
        .adicionaCamada(2, CAMADA_RELU) \
        .adicionaCamada(1, CAMADA_LINEAR)
    pop = builder.geraAleatorios(20)
    g = Genetico(
        builder,
        ffnFuncaoObjetivo,
        proporcaoFilhos=0.3,
        manterPais=True,
        maxmin=MINIMIZACAO,
        probMutacao=0.4,
        probCrossover=0.7
        )
    ranking = g.evoluir(pop, 100000, pontuacaoSatisfatoria=10.0)
    print(ranking.getRanking()[0])

if __name__ == '__main__':
    main()