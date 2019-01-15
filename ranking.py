MAXIMIZACAO = 1
MINIMIZACAO = 0

class Ranking(object):

    def __init__(self, maxmin):
        self.ranking = []
        self.rankingOrdenado = []
        self.maxmin = maxmin

    def adiciona(self, individuo, valorAdaptacao):
        self.ranking.append((individuo, valorAdaptacao))
        self.rankingOrdenado = []

    def getRanking(self):
        if not self.rankingOrdenado:
            self.ranking.sort(key=lambda item: item[1] if self.maxmin == MINIMIZACAO else -item[1])
            self.rankingOrdenado = self.ranking[:]
        return self.rankingOrdenado

    def isMelhorQue(self, pontuacaoSatisfatoria):
        r = self.getRanking()
        return pontuacaoSatisfatoria >= r[0][1] if self.maxmin == MINIMIZACAO else pontuacaoSatisfatoria <= r[0][1]

    def getPopulacao(self):
        p = list(map(lambda i: i[0], self.getRanking()))
        return p

    @staticmethod
    def validaInstancias(instancias, funcaoObjetivo, maxmin=MAXIMIZACAO):
        rankingAdaptacao = Ranking(maxmin)
        for instancia in instancias:
            valorObjetivo = funcaoObjetivo(instancia)
            rankingAdaptacao.adiciona(instancia, valorObjetivo)
        return rankingAdaptacao

    def __repr__(self):
        s = ''
        for i in range(len(self.getRanking())):
            s += '%d: %s -> %f\n' % (i + 1, self.ranking[i][0], self.ranking[i][1])
        return s