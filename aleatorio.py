import logging
from ranking import Ranking, MAXIMIZACAO, MINIMIZACAO

class Aleatorio(object):

    def __init__(self, funcaoObjetivo, maxmin=MAXIMIZACAO):
        self.maxmin = maxmin
        self.funcaoObjetivo = funcaoObjetivo

    def iterar(self, populacao, nGeracoes, pontuacaoSatisfatoria=None):
        if len(populacao) < 1:
            raise Exception('Impossivel iterar populacao de tamanho menor que 1')
        ranking = Ranking.validaInstancias(populacao, self.funcaoObjetivo, maxmin=self.maxmin)
        melhorInstancia = ranking.getPopulacao()[0]
        for i in range(nGeracoes):
            populacao = melhorInstancia.__class__.geraAleatorios(len(populacao)-1) + [melhorInstancia]
            ranking = Ranking.validaInstancias(populacao, self.funcaoObjetivo, maxmin=self.maxmin)
            if pontuacaoSatisfatoria is not None and ranking.isMelhorQue(pontuacaoSatisfatoria):
                logging.info('Número de iterações: %d' % (i+1))
                return ranking
        return ranking