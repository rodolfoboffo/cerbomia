MAXIMIZACAO = 1
MINIMIZACAO = 0

class Ranking(object):

    def __init__(self, maxmin):
        self.ranking = []
        self.maxmin = maxmin
        
    def adiciona(self, individuo, valorAdaptacao):
        self.ranking.append((individuo, valorAdaptacao))
    
    def getRanking(self):
        self.ranking.sort(key=lambda item: item[1] if self.maxmin == MINIMIZACAO else -item[1])
        return self.ranking[:]
    
    def getPopulacao(self):
        return map(self.getRanking(), lambda i: i[0])

class Genetico(object):
    
    def __init__(self, tamanhoGenoma, funcaoAdaptacao, populacao, maxmin=MAXIMIZACAO, probMutacao=0.01, probCrossover=0.10):
        self.probMutacao = probMutacao
        self.probCrossover = probCrossover
        self.populacao = populacao
        self.tamanhoGenoma = tamanhoGenoma
        self.maxmin=maxmin
        self.funcaoAdaptacao = funcaoAdaptacao
        
    def validaAdaptacao(self, populacao, funcaoAdaptacao, maxmin=MAXIMIZACAO):
        rankingAdaptacao = Ranking(maxmin)
        for individuo in populacao:
            valorAdaptacao = funcaoAdaptacao(individuo)
            rankingAdaptacao.adiciona(individuo, valorAdaptacao)
        return rankingAdaptacao

    def getReprGeneticasPopulacao(self):
        pass

    def fazCruzamento(self, populacao, probCrossover):
        pass

    def evoluir(self, nGeracoes):
        for i in range(nGeracoes):
            ranking = self.validaAdaptacao(self.populacao, self.funcaoAdaptacao, maxmin=self.maxmin)