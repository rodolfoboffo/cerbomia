from decimal import Decimal

EPSILON = Decimal('0.00000001')

class VetorUtil(object):
    
    @staticmethod
    def soma(v1, v2):
        return VetorUtil.aplica(v1, v2, lambda v1, v2: v1 + v2)
    
    @staticmethod
    def subtrai(v1, v2):
        return VetorUtil.aplica(v1, v2, lambda v1, v2: v1 - v2)
    
    @staticmethod
    def produtoHadamard(v1, v2):
        return VetorUtil.aplica(v1, v2, lambda v1, v2: v1 * v2)
    
    @staticmethod
    def divisaoHadamard(v1, v2):
        return VetorUtil.aplica(v1, v2, lambda v1, v2: v1 / v2)
    
    @staticmethod
    def aplica(v1, v2, f):
        if len(v1) != len(v2):
            raise Exception('Vetores de tamanhos diferentes')
        return [f(v1[i], v2[i]) for i in range(len(v1))]

class FuncaoEscalar(object):
    
    def __init__(self, f):
        self.f = f
        
    def avalia(self, v):
        return self.f(v)

    def derivada(self, v):
        if len(v) != 1:
            raise Exception('derivada está definida apenas para funções de uma variável')
        return self.derivadaParcial(v, 0)

    def derivadaParcial(self, v, i):
        eps = [Decimal(0) if vi != i else EPSILON for vi in range(len(v))]
        h2 = self.avalia(v)
        h1 = self.avalia(VetorUtil.subtrai(v, eps))
        delta = h2 - h1
        derivada = delta / eps
        return derivada
    
    def gradiente(self, v):
        g = []
        for i in range(len(v)):
            g.append(self.derivadaParcial(v, i))
        return g

class Relu(FuncaoEscalar):
    def __init__(self):
        super(Relu, self).__init__(self.funcao)

    def funcao(self, variaveis):
        if len(variaveis) != 1:
            raise Exception('ReLU é função de apenas uma variável')
        return Decimal(0) if variaveis[0] < 0 else variaveis[0]

class Identidade(FuncaoEscalar):
    def __init__(self):
        super(Identidade, self).__init__(self.funcao)

    def funcao(self, variaveis):
        if len(variaveis) != 1:
            raise Exception('Funcao Identidade é função de apenas uma variável')
        return variaveis[0]

class Softmax(FuncaoEscalar):
    def __init__(self, indiceNumerador):
        super(Softmax, self).__init__(self.funcao)
        self.indiceNumerador = indiceNumerador

    def funcao(self, variaveis):
        ex = list(map(lambda x: x.exp(), variaveis))
        soma = sum(ex)
        return variaveis[self.indiceNumerador].exp() / soma

def main():
    fv = Relu()
    print(fv.avalia([Decimal(3)]))

if __name__ == '__main__':
    main()