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
        p = list(map(lambda i: i[0], self.getRanking()))
        return p
        
    def __repr__(self):
        s = ''
        for i in range(len(self.getRanking())):
            s += '%d: %s -> %f\n' % (i+1, self.ranking[i][0], self.ranking[i][1])
        return s

class Genetico(object):
    
    def __init__(self, funcaoAdaptacao, proporcaoFilhos=0.2, manterPais=False, maxmin=MAXIMIZACAO, probMutacao=0.05, probCrossover=0.10):
        self.probMutacao = probMutacao
        self.probCrossover = probCrossover
        self.proporcaoFilhos = proporcaoFilhos
        self.maxmin=maxmin
        self.manterPais = manterPais
        self.funcaoAdaptacao = funcaoAdaptacao
        
    def validaAdaptacao(self, populacao, funcaoAdaptacao, maxmin=MAXIMIZACAO):
        rankingAdaptacao = Ranking(maxmin)
        for individuo in populacao:
            valorAdaptacao = funcaoAdaptacao(individuo)
            rankingAdaptacao.adiciona(individuo, valorAdaptacao)
        return rankingAdaptacao

    def geraMascara(self, nBytes, prob):
        mascara = 0
        currentBit = random.randint(0, 1)
        nBits = 8*nBytes
        for i in range(nBits):
            if random.random() < prob:
                currentBit ^= 1
            mascara = mascara | currentBit
            mascara = mascara if i == (nBits - 1) else mascara << 1 
        return mascara
        
        
    def fazCruzamentoPopulacao(self, populacao, probCrossover, proporcaoFilhos, manterPais):
        novaGeracao = []
        for i in range(len(populacao)-1):
            individuoA = populacao[i]
            individuoB = populacao[i+1]
            for j in range(int(len(populacao)*proporcaoFilhos)):
                filhos = self.fazCruzamentoIndividuos(individuoA, individuoB, probCrossover)
                novaGeracao += filhos
                if manterPais:
                    novaGeracao += [individuoA]
            if len(novaGeracao) >= len(populacao):
                break
        return novaGeracao[:len(populacao)]

    def fazCruzamentoIndividuos(self, individuo1, individuo2, probCrossover):
        tamGenoma = individuo1.getTamanhoGenoma()
        mascara = self.geraMascara(tamGenoma, probCrossover)
        rep1 = individuo1.getReprGenetica()
        rep2 = individuo2.getReprGenetica()
        #(!ab)|ac
        #(!ac)|ab
        repFilho1 = (~mascara)&rep1 | mascara&rep2
        repFilho2 = (~mascara)&rep2 | mascara&rep1
        return (individuo1.__class__.getFromReprGenetica(repFilho1),
                individuo1.__class__.getFromReprGenetica(repFilho2))

    def fazMutacaoPopulacao(self, populacao, probMutacao):
        novaPopulacao = []
        for individuo in populacao:
            novaPopulacao.append(self.fazMutacaoIndividuo(individuo, probMutacao))
        return novaPopulacao

    def fazMutacaoIndividuo(self, individuo, probMutacao):
        # !a&b + a&!b
        tamGenoma = individuo.getTamanhoGenoma()
        mascara = self.geraMascara(tamGenoma, probMutacao)
        rep = individuo.getReprGenetica()
        rep = (~mascara)&rep | mascara&(~rep)
        return individuo.__class__.getFromReprGenetica(rep)


    def evoluir(self, populacao, nGeracoes, epsilon=None):
        if len(populacao) < 2:
            raise Exception('Impossivel evoluir populacao de tamanho menor que 2')
        ranking = self.validaAdaptacao(populacao, self.funcaoAdaptacao, maxmin=self.maxmin)
        for i in range(nGeracoes):
            populacao = self.fazCruzamentoPopulacao(ranking.getPopulacao(), self.probCrossover, self.proporcaoFilhos, self.manterPais)
            populacao = self.fazMutacaoPopulacao(populacao, self.probMutacao)
            ranking = self.validaAdaptacao(populacao, self.funcaoAdaptacao, maxmin=self.maxmin)
            if epsilon is not None and epsilon > ranking
        return ranking
