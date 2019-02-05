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

class FuncaoVetorial(object):
    
    def __init__(self, f):
        self.f = f
        
    def avalia(self, v):
        return self.f(v)

    def derivadaParcial(self, v, i):
        eps = [Decimal(0) if vi != i else EPSILON for vi in range(len(v))]
        h2 = self.avalia(v)
        h1 = self.avalia(VetorUtil.subtrai(v, eps))
        delta = VetorUtil.subtrai(h2, h1)
        derivada = VetorUtil.divisaoHadamard(delta, eps)
        return derivada

class Relu(FuncaoVetorial):
    def __init__(self):
        super(Relu, self).__init__(self.funcao)

    def funcao(self, vetor):
        f = lambda v: Decimal(0) if v < 0 else v
        return list(map(f, vetor))

class Identidade(FuncaoVetorial):
    def __init__(self):
        super(Identidade, self).__init__(self.funcao)

    def funcao(self, vetor):
        f = lambda v: v
        return list(map(f, vetor))

class Softmax(FuncaoVetorial):
    def __init__(self):
        super(Softmax, self).__init__(self.funcao)

    def funcao(self, vetor):
        vetor = list(map(lambda x: x.exp(), vetor))
        soma = sum(vetor)
        vetor = list(map(lambda v: v / soma, vetor))
        return vetor

def main():
    fv = Relu()
    print(fv.avalia([Decimal(-3)]))

if __name__ == '__main__':
    main()