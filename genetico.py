import random

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

    def __repr__(self):
        s = ''
        for i in range(len(self.getRanking())):
            s += '%d: %s -> %f\n' % (i+1, self.ranking[i][0], self.ranking[i][1])
        return s

class Genetico(object):
    
    def __init__(self, funcaoAdaptacao, maxmin=MAXIMIZACAO, probMutacao=0.01, probCrossover=0.10):
        self.probMutacao = probMutacao
        self.probCrossover = probCrossover
        self.maxmin=maxmin
        self.funcaoAdaptacao = funcaoAdaptacao
        
    def validaAdaptacao(self, populacao, funcaoAdaptacao, maxmin=MAXIMIZACAO):
        rankingAdaptacao = Ranking(maxmin)
        for individuo in populacao:
            valorAdaptacao = funcaoAdaptacao(individuo)
            rankingAdaptacao.adiciona(individuo, valorAdaptacao)
        return rankingAdaptacao

    def geraMascaraCruzamente(self, nBytes, probCrossover):
        mascaraCruzamento = 0
        currentBit = random.randint(0, 1)
        for i in range(8*nBytes):
            if random.random() < probCrossover:
                currentBit

    def fazCruzamento(self, populacao, probCrossover):
        tamGenoma = populacao[0].getTamanhoGenoma()
        

    def evoluir(self, populacao, nGeracoes):
        if len(populacao) < 2:
            raise Exception('Impossivel evoluir populacao de tamanho menor que 2')
        for i in range(nGeracoes):
            ranking = self.validaAdaptacao(populacao, self.funcaoAdaptacao, maxmin=self.maxmin)
            print(ranking)
            novaPopulacao = self.fazCruzamento(ranking.getPopulacao(), self.probCrossover)

