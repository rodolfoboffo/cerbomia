import math
import struct
import random

CAMADA_RELU = 0
CAMADA_SOFTMAX = 1
CAMADA_ENTRADA = -1

class FFNBuilder(object):
    
    def __init__(self):
        self.camadas = []

    def adicionaCamadaEntrada(self, numeroNeuronios):
        self.camadas.insert(0, (numeroNeuronios, CAMADA_ENTRADA))
        return self
    
    def adicionaCamada(self, numeroNeuronios, tipo):
        self.camadas += [(numeroNeuronios, tipo)]
        return self

    

    def constroi(self):
        tipos = list(map(lambda camada: camada[1]), self.camadas)
        pesos = []
        desvios = []
        return FeedForwardNet()


class FeedForwardNet(object):
    
    def __init__(self, tiposCamadas, matrizPesos, matrizDesvios):
        self.tiposCamadas = tiposCamadas
        self.matrizPesos = matrizPesos
        self.matrizDesvios = matrizDesvios

    def getFuncaoAtivacao(self, tipo):
        if tipo == CAMADA_RELU:
            return FeedForwardNet.relu
        elif tipo == CAMADA_SOFTMAX:
            return FeedForwardNet.softmax
        else:
            raise Exception('Tipo de camada não disponível')

    @staticmethod
    def relu(vetor):
        f = lambda v: 0.0 if v < 0.0 else v
        return list(map(f, vetor))
        
    @staticmethod
    def softmax(vetor):
        vetor = list(map(math.exp, vetor))
        soma = sum(vetor)
        vetor = list(map(lambda v: v / soma, vetor))
        return vetor

    def alimenta(self, entrada):
        if len(self.tiposCamadas) == 0 or len(self.matrizPesos) != len(self.tiposCamadas):
            raise Exception('Rede nao esta bem definida para esta entrada')
        
        for indiceCamada in range(len(self.tiposCamadas)):
            saida = []
            tipoCamada = self.tiposCamadas[indiceCamada]
            funcaoAtivacao = self.getFuncaoAtivacao(tipoCamada)
            pesos = self.matrizPesos[indiceCamada]
            desvios = self.matrizDesvios[indiceCamada]
            for indiceNeuronioReceptor in range(len(pesos)):
                elemento = 0.0
                for indiceNeuronioTransm in range(len(pesos[indiceNeuronioReceptor])):
                    elemento += pesos[indiceNeuronioReceptor][indiceNeuronioTransm] * entrada[indiceNeuronioTransm]
                elemento += desvios[indiceNeuronioReceptor]
                saida.append(elemento)
            saida = funcaoAtivacao(saida)
            entrada = saida
        return saida

if __name__ == '__main__':
