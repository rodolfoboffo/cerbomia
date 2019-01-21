import random
import logging
from raizes import Raiz, RaizBuilder
from ffn import FFNBuilder, FeedForwardNet, CAMADA_RELU, CAMADA_SOFTMAX, CAMADA_ENTRADA 
from aleatorio import Aleatorio
from genetico import Genetico
from ranking import MINIMIZACAO, MAXIMIZACAO

def raizFuncaoObjetivo(r):
    return pow((r.getValor() - 300512.0), 2)

def ffnFuncaoObjetivo(ffn):
    f = lambda x: pow(ffn.alimenta([x])[0] - ((6*x-1)), 2.0)

    erro = 0.0
    for i in range(50):
        aleatorio = random.uniform(-100.0, 100.0)
        erro += f(aleatorio)
    return erro

def main():
    logging.getLogger().setLevel(logging.INFO)

    # builder = RaizBuilder()
    # pop = builder.geraAleatorios(50)
    # g = Genetico(
    #     builder,
    #     raizFuncaoObjetivo,
    #     proporcaoFilhos=0.3,
    #     manterPais=True,
    #     maxmin=MINIMIZACAO,
    #     probMutacao=0.1,
    #     probCrossover=0.3
    #     )
    # ranking = g.evoluir(pop, 10000, pontuacaoSatisfatoria=pow(0.000001, 2))
    # print(ranking.getPopulacao()[0])
    
    builder = FFNBuilder()
    builder.adicionaCamadaEntrada(1) \
        .adicionaCamada(1, CAMADA_RELU)
    pop = builder.geraAleatorios(50)
    g = Genetico(
        builder,
        ffnFuncaoObjetivo,
        proporcaoFilhos=0.3,
        manterPais=True,
        maxmin=MINIMIZACAO,
        probMutacao=0.1,
        probCrossover=0.3
        )
    ranking = g.evoluir(pop, 100, pontuacaoSatisfatoria=10.0)
    print(ranking.getRanking()[0])

if __name__ == '__main__':
    main()