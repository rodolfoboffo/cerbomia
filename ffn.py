import math
import struct
import random
import logging

CAMADA_RELU = 0
CAMADA_SOFTMAX = 1
CAMADA_ENTRADA = -1

class FFNBuilder(object):
    
    def __init__(self):
        self.camadas = []
        self.formatoStruct = None

    def adicionaCamadaEntrada(self, numeroNeuronios):
        self.camadas.insert(0, (numeroNeuronios, CAMADA_ENTRADA))
        return self
    
    def adicionaCamada(self, numeroNeuronios, tipo):
        self.camadas += [(numeroNeuronios, tipo)]
        return self

    def getTamanhoGenoma(self):
        return struct.calcsize(self.getFormatoStruct())

    def getFormatoStruct(self):
        if self.formatoStruct is None:
            nFloats = 0
            for i in range(1, len(self.camadas)):
                nFloats += self.camadas[i][0] + self.camadas[i][0] * self.camadas[i-1][0]
            self.formatoStruct = 'f' * nFloats
        return self.formatoStruct

    def getFromReprGenetica(self, rep):
        
        intList = []
        for i in range(struct.calcsize(self.getFormatoStruct())):
            intByte = rep & 0xFF
            intList.insert(0, intByte)
            rep >>= 8
        b = bytes(intList)
        floats = list(struct.unpack(self.getFormatoStruct(), b))

        tipos = list(map(lambda camada: camada[1], self.camadas[1:]))
        pesos = []
        desvios = []
        for i in range(1, len(self.camadas)):
            pCamada = []
            for j in range(self.camadas[i][0]):
                pNeuronio = []
                for k in range(self.camadas[i-1][0]):
                    pNeuronio.append(floats.pop(0))
                pCamada.append(pNeuronio)
            pesos.append(pCamada)

        for i in range(1, len(self.camadas)):
            dCamada = []
            for j in range(self.camadas[i][0]):
                dCamada.append(floats.pop(0))
            desvios.append(dCamada)
        return FeedForwardNet(tipos, pesos, desvios)


    def geraAleatorio(self):
        tipos = list(map(lambda camada: camada[1], self.camadas[1:]))
        pesos = []
        desvios = []
        for i in range(1, len(self.camadas)):
            pCamada = []
            dCamada = []
            for j in range(self.camadas[i][0]):
                dCamada.append(random.uniform(-100.0, 100.0))
                pNeuronio = []
                for k in range(self.camadas[i-1][0]):
                    pNeuronio.append(random.uniform(-100.0, 100.0))
                pCamada.append(pNeuronio)
            pesos.append(pCamada)
            desvios.append(dCamada)
        return FeedForwardNet(tipos, pesos, desvios)

    def geraAleatorios(self, n):
        nets = []
        for i in range(n):
            nets.append(self.geraAleatorio())
        return nets


class FeedForwardNet(object):
    
    def __init__(self, tiposCamadas, matrizPesos, matrizDesvios):
        self.tiposCamadas = tiposCamadas
        self.matrizPesos = matrizPesos
        self.matrizDesvios = matrizDesvios

    def __eq__(self, other):
        return self.tiposCamadas == other.tiposCamadas and \
               self.matrizPesos == other.matrizPesos and \
               self.matrizDesvios == other.matrizDesvios

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

    
    def getReprGenetica(self):
        floatsPesos = []
        floatsDesvios = []
        for i in range(len(self.matrizPesos)):
            floatsDesvios += self.matrizDesvios[i]
            for j in range(len(self.matrizPesos[i])):
                floatsPesos += self.matrizPesos[i][j]
        nFloats = len(floatsPesos) + len(floatsDesvios)
        packed = bytearray(struct.pack(nFloats * 'f', *(floatsPesos + floatsDesvios)))
        intRepr = 0
        for i in range(len(packed)):
            intRepr |= packed[i]
            intRepr = intRepr << 8 if i != (len(packed) - 1) else intRepr
        return intRepr
