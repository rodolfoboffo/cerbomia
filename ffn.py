CAMADA_RELU = 0
CAMADA_SOFTMAX = 1

class FFDBuilder(object):
    
    def __init__(self):
        self.nosEntrada = 1
        self.camadas = []

    def nosEntrada(self, n):
        self.nosEntrada = n
        return self
    
    def adicionaCamada(self, numeroNeuronios, tipo):
        self.camadas += [(nuneroNeuronios, tipo)]
        return self
        
    def constroi(self):
        return FeedForwardNet()

class FeedForwardNet(object):
    
    def __init__(self, tiposCamadas, matrizPesos, matrizDesvios):
        self.tiposCamadas = tiposCamadas
        self.matrizPesos = matrizPesos
        self.matrizDesvios = matrizDesvios

    def alimenta(self, entrada):
        if len(self.tiposCamadas) == 0 or len(self.matrizPesos) != len(self.tiposCamadas):
            raise Excpetion('Rede nao esta bem definida para esta entrada')
        for indiceCamada in range(len(self.tiposCamadas)):
            tipoCamada = tiposCamadas[indiceCamada]
            pesos = self.matrizPesos[indiceCamada]
            desvios = self.matrizDesvios[indiceCamada]
            saida = []
            for indiceNeuronioReceptor in range(len(pesos)):
                elemento = 0.0
                for indiceNeuronioTransm in range(len(pesos[indiceNeuronioReceptor])):
                    elemento += pesos[indiceNeuronioReceptor][indiceNeuronioTransm] * entrada[indiceNeuronioTransm] + desvios[indiceNeuronioTransm]
                elemento = self.funcaoAtivacao(tipoCamada, elemento)
                saida.append(elemento)
            entrada = saida
        return saida