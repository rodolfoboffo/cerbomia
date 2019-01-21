import random
import logging
from ranking import Ranking, MINIMIZACAO, MAXIMIZACAO

class Genetico(object):
    
    def __init__(self, individuoBuilder, funcaoAdaptacao, proporcaoFilhos=0.2, manterPais=False, maxmin=MAXIMIZACAO, probMutacao=0.05, probCrossover=0.10):
        self.probMutacao = probMutacao
        self.probCrossover = probCrossover
        self.proporcaoFilhos = proporcaoFilhos
        self.maxmin=maxmin
        self.manterPais = manterPais
        self.funcaoAdaptacao = funcaoAdaptacao
        self.individuoBuilder = individuoBuilder

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
        
        
    def fazCruzamentoPopulacao(self, populacao, probCrossover, proporcaoFilhos, manterPais, individuoBuilder):
        novaGeracao = []
        for i in range(len(populacao)-1):
            individuoA = populacao[i]
            individuoB = populacao[i+1]
            for j in range(int(len(populacao)*proporcaoFilhos)):
                filhos = self.fazCruzamentoIndividuos(individuoA, individuoB, probCrossover, individuoBuilder)
                novaGeracao += filhos
                if manterPais:
                    novaGeracao += [individuoA]
            if len(novaGeracao) >= len(populacao):
                break
        return novaGeracao[:len(populacao)]

    def fazCruzamentoIndividuos(self, individuo1, individuo2, probCrossover, individuoBuilder):
        tamGenoma = individuoBuilder.getTamanhoGenoma()
        mascara = self.geraMascara(tamGenoma, probCrossover)
        rep1 = individuo1.getReprGenetica()
        rep2 = individuo2.getReprGenetica()
        #(!ab)|ac
        #(!ac)|ab
        repFilho1 = (~mascara)&rep1 | mascara&rep2
        repFilho2 = (~mascara)&rep2 | mascara&rep1
        return (individuoBuilder.getFromReprGenetica(repFilho1),
                individuoBuilder.getFromReprGenetica(repFilho2))

    def fazMutacaoPopulacao(self, populacao, probMutacao, individuoBuilder):
        novaPopulacao = []
        for individuo in populacao:
            novaPopulacao.append(self.fazMutacaoIndividuo(individuo, probMutacao, individuoBuilder))
        return novaPopulacao

    def fazMutacaoIndividuo(self, individuo, probMutacao, individuoBuilder):
        # !a&b + a&!b
        tamGenoma = individuoBuilder.getTamanhoGenoma()
        mascara = self.geraMascara(tamGenoma, probMutacao)
        rep = individuo.getReprGenetica()
        rep = (~mascara)&rep | mascara&(~rep)
        return individuoBuilder.getFromReprGenetica(rep)


    def evoluir(self, populacao, nGeracoes, pontuacaoSatisfatoria=None):
        if len(populacao) < 2:
            raise Exception('Impossivel evoluir populacao de tamanho menor que 2')
        ranking = Ranking.validaInstancias(populacao, self.funcaoAdaptacao, maxmin=self.maxmin)
        for i in range(nGeracoes):
            populacao = self.fazCruzamentoPopulacao(ranking.getPopulacao(), self.probCrossover, self.proporcaoFilhos, self.manterPais, self.individuoBuilder)
            populacao = self.fazMutacaoPopulacao(populacao, self.probMutacao, self.individuoBuilder)
            ranking = Ranking.validaInstancias(populacao, self.funcaoAdaptacao, maxmin=self.maxmin)
            if pontuacaoSatisfatoria is not None and ranking.isMelhorQue(pontuacaoSatisfatoria):
                logging.info('Número de iterações: %d' % (i+1))
                return ranking
        return ranking
